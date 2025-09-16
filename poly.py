import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("pr.csv")
x = np.array(data["x"]).reshape(-1, 1)
y = data["y"]

print("x values:\n", x)

degree = int(input("Enter degree: "))

# Build design matrix for training data
X = np.ones((len(x), 1))
for d in range(1, degree + 1):
    X = np.c_[X, x**d]

# Normal Equation: beta = (X^T X)^(-1) X^T y
beta = np.linalg.inv(X.T @ X) @ (X.T @ y)

# Generate smooth x values for plotting
xline = np.linspace(min(x), max(x), 200).reshape(-1, 1)

# Build design matrix for smooth x values
Xline = np.ones((len(xline), 1))
for d in range(1, degree + 1):
    Xline = np.c_[Xline, xline**d]

# Predicted y values
yp = Xline @ beta

# Plot
plt.scatter(x, y, color="red", label="Data points")
plt.plot(xline, yp, color="blue", label=f"Degree {degree} fit")
plt.legend()
plt.show()
