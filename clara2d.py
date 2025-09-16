import numpy as np
import random
import matplotlib.pyplot as plt

# ---  Dataset ---
data = np.array([
    [2, 3], [3, 3], [2, 2], [8, 8], [9, 8], [8, 9],
    [15, 16], [16, 16], [15, 15], [25, 24], [24, 25], [25, 25]
])

k = 3              # number of clusters
sample_size = 6    # sample size for each iteration
num_samples = 5    # number of random samples

# ---  Distance function ---
def euclidean(a, b):
    return np.linalg.norm(a - b)

# ---  Function to calculate total cost ---
def total_cost(medoids, points):
    return sum(min(euclidean(p, m) for m in medoids) for p in points)

best_medoids = None
best_cost = float('inf')

# ---  CLARA algorithm ---
for _ in range(num_samples):
    sample = data[random.sample(range(len(data)), sample_size)]
    medoids = sample[random.sample(range(sample_size), k)]

    changed = True
    while changed:
        clusters = {tuple(m): [] for m in medoids}
        for p in sample:
            closest = min(medoids, key=lambda m: euclidean(p, m))
            clusters[tuple(closest)].append(p)
        
        changed = False
        for i, m in enumerate(medoids):
            cluster_points = clusters[tuple(m)]
            if cluster_points:
                new_medoid = min(cluster_points, key=lambda x: sum(euclidean(x, y) for y in cluster_points))
                if not np.array_equal(new_medoid, m):
                    medoids[i] = new_medoid
                    changed = True

    cost = total_cost(medoids, data)
    if cost < best_cost:
        best_cost = cost
        best_medoids = medoids.copy()

# ---  Assign points to best medoids ---
final_clusters = {tuple(m): [] for m in best_medoids}
for p in data:
    closest = min(best_medoids, key=lambda m: euclidean(p, m))
    final_clusters[tuple(closest)].append(p)

# ---  Print results ---
print("Best Medoids:", best_medoids)
for m, cluster in final_clusters.items():
    print(f"Cluster with medoid {m}: {cluster}")

# ---  Plot ---
colors = ['red', 'blue', 'green']
plt.figure(figsize=(7,6))
for idx, (medoid, cluster) in enumerate(final_clusters.items()):
    cluster = np.array(cluster)
    plt.scatter(cluster[:,0], cluster[:,1], color=colors[idx], label=f'Cluster {idx+1}')
    plt.scatter(medoid[0], medoid[1], color='black', marker='X', s=150)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("CLARA Clustering (2D)")
plt.legend()
plt.show()
