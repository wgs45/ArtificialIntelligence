import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers import LSTM, Dense
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler

# %matplotlib inline

# Set workspace and seed for reproducibility
drive_path = "."
os.makedirs(drive_path, exist_ok=True)
np.random.seed(10)
os.chdir(drive_path)
print(f"file path: {os.getcwd()}")

# Load training data
df_train = pd.read_csv("goog_train.csv", index_col="Date")
X_train_set = df_train.iloc[:, 4:5].values

# Scale data to [0, 1] range for better neural network convergence
sc = MinMaxScaler(feature_range=(0, 1))
X_train_set_scaled = sc.fit_transform(X_train_set)

# Create sequences: Use 60 previous days to predict the next day
train_days = 60
X_train_data, Y_train_data = [], []

for i in range(len(X_train_set_scaled) - train_days - 1):
    X_train_data.append(X_train_set_scaled[i : (i + train_days), 0])
    Y_train_data.append(X_train_set_scaled[i + train_days, 0])

X_train = np.array(X_train_data)
Y_train = np.array(Y_train_data)

# Reshape input to 3D tensor: [samples, time steps, features]
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# Build LSTM model: Single LSTM layer followed by a Dense output layer
model = Sequential()
model.add(LSTM(10, activation="relu", input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(1))
model.compile(loss="mae", optimizer="adam", metrics=["mean_absolute_error"])

# Setup training controls: Stop early if loss plateaus and save the best model
callback = EarlyStopping(monitor="loss", patience=10, verbose=1, mode="min")
checkpoint = ModelCheckpoint(
    filepath="model.h5", monitor="loss", verbose=1, save_best_only=True, mode="min"
)

# Train the model
model.fit(
    X_train,
    Y_train,
    epochs=100,
    batch_size=10,
    callbacks=[callback, checkpoint],
    shuffle=True,
)

# Prepare testing data: Combine train/test to get the initial 60-day window
df_test = pd.read_csv("goog_test.csv")
dataset_total = pd.concat((df_train["Close"], df_test["Close"]), axis=0)
inputs = dataset_total[len(dataset_total) - len(df_test) - train_days :].values
inputs = inputs.reshape(-1, 1)
inputs = sc.transform(inputs)

# Create test sequences
X_test = []
for i in range(train_days, len(inputs)):
    X_test.append(inputs[i - train_days : i, 0])

X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# Run prediction and inverse scale to get actual dollar values
X_test_pred = model.predict(X_test)
X_test_pred_price = sc.inverse_transform(X_test_pred)
Y_test = df_test.iloc[:, 4:5].values

# Visualize the results: Real vs. Predicted prices
plt.plot(Y_test, color="red", label="Real stock price")
plt.plot(X_test_pred_price, color="blue", label="Predicted stock price")
plt.title("2021 Google Stock Price Prediction")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend()
plt.show()
