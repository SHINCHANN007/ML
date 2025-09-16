import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [2.5, 2.4],
    [0.5, 0.7],
    [2.2, 2.9],
    [1.9, 2.2],
    [3.1, 3.0],
    [2.3, 2.7],
    [2, 1.6],
    [1, 1.1],
    [1.5, 1.6],
    [1.1, 0.9]
])

mean = np.mean(data, axis=0)
centered = data - mean

cov_matrix = np.cov(centered, rowvar=False)

eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

idx = np.argsort(eigenvalues)[::-1]
eigenvectors = eigenvectors[:, idx]


top_eigenvectors = eigenvectors[:, :1] 
reduced_data = centered.dot(top_eigenvectors)

projected = reduced_data.dot(top_eigenvectors.T) + mean

plt.figure(figsize=(6,6))
plt.scatter(data[:,0], data[:,1], color='blue', label='Original Data')
plt.scatter(projected[:,0], projected[:,1], color='red', label='Projected onto PC1')
for i in range(data.shape[0]):
    plt.plot([data[i,0], projected[i,0]], [data[i,1], projected[i,1]], 'k--', linewidth=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('PCA Projection onto First Principal Component')
plt.grid(True)
plt.show()
