import random
import numpy as np

data = [1, 2, 3, 10, 11, 12, 20, 22, 23, 24, 25]

k = 2        # number of clusters
sample_size = 5
num_samples = 3  # how many times to repeat

def total_cost(medoids, points):
    return sum(min(abs(p - m) for m in medoids) for p in points)

best_medoids = None
best_cost = float('inf')

for s in range(num_samples):
    # Take a random sample
    sample = random.sample(data, sample_size)
    
    # Initialize medoids randomly from sample
    medoids = random.sample(sample, k)
    
    changed = True
    while changed:
        clusters = {m: [] for m in medoids}
        # Assign points in sample to nearest medoid
        for p in sample:
            closest = min(medoids, key=lambda m: abs(p - m))
            clusters[closest].append(p)
        
        changed = False
        # Update medoids in each cluster
        for m in medoids:
            cluster_points = clusters[m]
            if cluster_points:
                # Choose point in cluster with minimum total distance as new medoid
                new_medoid = min(cluster_points, key=lambda x: sum(abs(x - y) for y in cluster_points))
                if new_medoid != m:
                    medoids[medoids.index(m)] = new_medoid
                    changed = True

    # 4️⃣ Calculate cost for this sample clustering
    cost = total_cost(medoids, data)
    if cost < best_cost:
        best_cost = cost
        best_medoids = medoids.copy()

# 5️⃣ Assign all points to nearest best medoid
final_clusters = {m: [] for m in best_medoids}
for p in data:
    closest = min(best_medoids, key=lambda m: abs(p - m))
    final_clusters[closest].append(p)

# 6️⃣ Print results
print("Best Medoids:", best_medoids)
for m, cluster in final_clusters.items():
    print(f"Cluster with medoid {m}: {cluster}")
