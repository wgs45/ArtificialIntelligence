# EXERCISE ANSWERS

# Random Seed: I used "student id" as the seed to ensure my results are repeatable.

# Convergence Comparison:
# Function: ReLU (the current one) works best for this curve. If I switch to Sigmoid,
# it converges much slower.
# Layers: 1 Hidden Layer (10 neurons) is enough for this simple x^2 curve.
# Adding a 2nd layer makes the loss drop slightly faster, but the difference is very small for such a simple problem.

# Bonus (Overfitting): Has overfitting occurred? NO. Reason: The red line (AI Prediction) is a smooth curve.
# If it were overfitting, the red line would "wiggle" up and down trying to hit every single orange dot (the noise).
# Since the line stays smooth, it has learned the "rule" (x^2) and ignored the "noise."

# ---

import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
from IPython.display import clear_output

# Setup Reproducibility
# Using a fixed seed ensures you get the same random numbers every time you run it
student_id = 12345678
torch.manual_seed(student_id)

# Prepare Synthetic Data
# Create 100 points between -1 and 1
# .unsqueeze(dim=1) converts it from a 1D array to a 2D column vector [100, 1]
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
# Generate targets (y = x^2) and add 10% random noise to simulate real-world data
y = x.pow(2) + 0.1 * torch.rand(x.size())
# Define the Neural Network Architecture
# nn.Sequential allows us to stack layers in order
net = nn.Sequential(
    nn.Linear(1, 10),  # Hidden Layer: 1 input (x) connected to 10 neurons
    nn.ReLU(),  # Activation: Adds non-linearity so the model can learn curves
    nn.Linear(10, 1),  # Output Layer: Reduces 10 neurons back to 1 output (predicted y)
)
# Define Optimization & Loss
# optimizer: Updates the network weights based on error (Learning Rate = 0.2)
optimizer = torch.optim.SGD(net.parameters(), lr=0.2)
# loss_func: Measures how "wrong" the model is (Mean Squared Error)
loss_func = nn.MSELoss()
# Training Loop
plt.ion()  # Turn on interactive mode for live plotting

for t in range(200):
    # Forward Pass: Predict y based on current x
    prediction = net(x)

    # Calculate error (Loss)
    loss = loss_func(prediction, y)

    # Backward Pass (The "Learning" Step)
    optimizer.zero_grad()  # Clear previous gradients to prevent accumulation
    loss.backward()  # Calculate how to change weights to reduce loss
    optimizer.step()  # Apply the changes to the network weights

    # Live Visualization (Every 10 steps)
    if t % 10 == 0:
        clear_output(wait=True)
        plt.cla()

        plt.scatter(x.data.numpy(), y.data.numpy(), color="orange", label="Real Data")

        plt.plot(
            x.data.numpy(), prediction.data.numpy(), "r-", lw=5, label="AI Prediction"
        )

        plt.text(
            0.5,
            0,
            f"Loss = {loss.data.item():.4f}",
            fontdict={"size": 20, "color": "red"},
        )

        plt.legend(loc="upper left")
        plt.show()
        plt.pause(0.1)

plt.ioff()  # Turn off interactive mode
plt.show()  # This blocks the script and keeps the window open until you close it
