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
top_pc = eigenvectors[:, np.argmax(eigenvalues)] 

reduced_data = centered.dot(top_pc)

plt.scatter(data[:,0], data[:,1], color='blue', label='Original Data')
plt.scatter(reduced_data*top_pc[0] + mean[0], reduced_data*top_pc[1] + mean[1],
            color='red', label='Projection onto PC1')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('PCA Projection')
plt.show()
