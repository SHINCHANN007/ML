import numpy as np
import random
import math

x = np.array([2,2,5,4,8,6,5,5,6,4])
y = np.array([4,6,6,7,3,6,2,7,3,4])
data = np.column_stack((x,y))

k = 2

m1 = random.choice(data)
m2 = random.choice(data)

centroids = np.array([m1, m2], dtype=float)

it = 1

while True:
    print(f"\n--- Iteration {it} ---")
    print(f"{'Point':<10}{'Dist to C0':<15}{'Dist to C1':<15}{'Cluster':<10}")

    label = []

    for idx, points in enumerate(data):
        c0 = np.linalg.norm(points - centroids[0])
        c1 = np.linalg.norm(points - centroids[1])

        cluster = 0 if c0 < c1 else 1
        label.append(cluster)

        print(f"p{idx+1:<9}{c0:<15.4f}{c1:<15.4f}{cluster:<10}")

    label = np.array(label)

    newcentroids = np.array([data[label == i].mean(axis=0) for i in range(k)])

    print("\nNew centroids:")
    for idx, c in enumerate(newcentroids):
        print(f"  Centroid {idx}: ({c[0]:.2f}, {c[1]:.2f})")

    if np.allclose(centroids, newcentroids):
        print("\n✅ Centroids stabilized. Clustering complete!")
        break

    centroids = newcentroids
    it += 1
