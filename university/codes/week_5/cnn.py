import glob  # for local file searching

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow.keras as keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import (Conv2D, Dense, Dropout, Flatten,
                                     MaxPooling2D)
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical

# Load MNIST dataset (handwritten digits)
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# Reshape to (batch, height, width, channels) for CNN compatibility
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype("float32")
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype("float32")

# Normalize pixel values to [0, 1] for faster convergence
X_train /= 255
X_test /= 255

# One-hot encode labels (e.g., 3 becomes [0,0,0,1,0,0,0,0,0,0])
Y_train = to_categorical(Y_train)
Y_test = to_categorical(Y_test)
model = Sequential()

# Layer 1: Extract 8 features using 5x5 filters; downsample by half
model.add(
    Conv2D(
        8,
        kernel_size=(5, 5),
        padding="same",
        input_shape=(28, 28, 1),
        activation="relu",
    )
)
model.add(MaxPooling2D(pool_size=(2, 2)))

# Layer 2: Increase depth to 16 features; further downsample
model.add(Conv2D(16, kernel_size=(5, 5), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Layer 3: Final feature extraction before classification
model.add(Conv2D(16, kernel_size=(5, 5), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Transition: Flatten 3D features into a 1D vector for Dense layers
model.add(Flatten())
model.add(Dense(64, activation="relu"))  # Fully connected layer for reasoning
model.add(Dense(10, activation="softmax"))  # Output layer: probability for digits 0-9
model.summary()

# Configure training: use crossentropy for multi-class tasks
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Train model: 10 passes over data, 20% reserved for validation
history = model.fit(
    X_train, Y_train, validation_split=0.2, epochs=10, batch_size=128, verbose=2
)

# Final performance evaluation on train and test sets
loss, accuracy = model.evaluate(X_train, Y_train)
print("Train Accuracy={:.2f}".format(accuracy))
loss, accuracy = model.evaluate(X_test, Y_test)
print("Test Accuracy={:.2f}".format(accuracy))

# from google.colab import files
# uploaded = files.upload()
# for filename in uploaded.keys():
# data = np.frombuffer(uploaded[filename], np.uint8)
# img = cv2.imdecode(data, cv2.IMREAD_GRAYSCALE)

# Defines the path to your local folder and finds all .png files
image_path = "test.png"
uploaded_files = glob.glob(image_path)
if not uploaded_files:
    print(f"No images found in {image_path}")

for filename in uploaded_files:
    # Read the image directly from hard drive
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    if img is None:
        continue  # Skip if file is corrupted
    # Resize to 28x28 to match MNIST model input
    img_resized = cv2.resize(img, (28, 28))
    # Auto-invert: if background is light, flip to white-on-black (MNIST style)
    if np.mean(img_resized) > 127:
        img_ready = cv2.bitwise_not(img_resized)
    else:
        img_ready = img_resized
    # Reshape for CNN: (1 sample, 28 height, 28 width, 1 channel)
    # Fixed the variable name and added normalization (/255)
    img_input = img_ready.reshape(1, 28, 28, 1).astype("float32") / 255
    # Run prediction and pick the index with the highest probability
    prediction = model.predict(img_input)
    result = np.argmax(prediction)

    # Visualize the processed image and the model's guess
    plt.figure(figsize=(2, 2))
    plt.imshow(img_ready, cmap="gray")
    plt.title(f"Predicted: {result}")
    plt.axis("off")
    plt.show()
    print(f"Filename: {filename}")
    print(f"Result: {result}")
