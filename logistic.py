import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1,1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])  # 0 = fail, 1 = pass


X = np.hstack((np.ones_like(x), x)) 

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

weights = np.zeros(X.shape[1])

lr = 0.1  # learning rate
epochs = 1000

for _ in range(epochs):
    z = X.dot(weights)
    pred = sigmoid(z)
    error = y - pred
    gradient = X.T.dot(error) / len(y)
    weights += lr * gradient


x_val = np.linspace(0,10,100).reshape(-1,1)
X_val = np.hstack((np.ones_like(x_val), x_val))
y_val = sigmoid(X_val.dot(weights))

plt.scatter(x, y, color="red", label="Actual points")
plt.plot(x_val, y_val, color="blue", label="Logistic curve")
plt.xlabel("Hours of study")
plt.ylabel("Pass probability")
plt.legend()
plt.show()
