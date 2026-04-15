import matplotlib.pyplot as plt
import numpy as np
from keras.datasets import mnist
from keras.layers import Dense, Input
from keras.models import Model

# Load the MNIST dataset (ignoring labels since this is an autoencoder)
(X_train, _), (X_test, _) = mnist.load_data()

# Flatten 28x28 images into 784-element vectors and convert to float
X_train = X_train.reshape(X_train.shape[0], 28 * 28).astype("float32")
X_test = X_test.reshape(X_test.shape[0], 28 * 28).astype("float32")

# Normalize pixel values to a range between 0 and 1
X_train = X_train / 255
X_test = X_test / 255

# Define the Full Autoencoder Architecture
image = Input(shape=(784,))
First = Dense(300, activation="relu")(image)  # Encoder layer 1
Second = Dense(144, activation="relu")(First)  # Bottleneck (compressed representation)
Third = Dense(300, activation="relu")(Second)  # Decoder layer 1
image_out = Dense(784, activation="sigmoid")(Third)  # Reconstructed output
ae = Model(image, image_out)

# Define the Encoder model (Input -> Bottleneck)
encoder = Model(image, Second)

# Define the Decoder model (Bottleneck -> Output)
decoder_img = Input(shape=(144,))
layer1 = ae.layers[-2](decoder_img)  # Reuse the 'Third' layer weights
layer2 = ae.layers[-1](layer1)  # Reuse the 'image_out' layer weights
decoder = Model(decoder_img, layer2)

# Compile and train the model using binary cross-entropy loss
ae.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
ae.fit(
    X_train,
    X_train,
    validation_data=(X_test, X_test),
    epochs=10,
    batch_size=128,
    verbose=2,
)

# Compress images and then reconstruct them
encoded = encoder.predict(X_test)
decoded = decoder.predict(encoded)

# Visualize Results
plt.figure(figsize=(10, 3))
x = 8
for i in range(x):
    # Original Images
    y = plt.subplot(3, 8, i + 1)
    y.imshow(X_test[i].reshape(28, 28), cmap="binary")
    y.axis("off")

    # Encoded (Compressed) Representations
    y = plt.subplot(3, 8, i + 1 + x)
    y.imshow(encoded[i].reshape(12, 12), cmap="binary")
    y.axis("off")

    # Reconstructed Images
    y = plt.subplot(3, 8, i + 1 + 2 * x)
    y.imshow(decoded[i].reshape(28, 28), cmap="binary")
    y.axis("off")
