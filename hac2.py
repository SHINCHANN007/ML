import numpy as np
import matplotlib.pyplot as plt

# --- 1️⃣ Sample 2D points ---
data = np.array([
    [2, 3], [3, 3], [2, 2], [8, 8], [9, 8], [8, 9],
    [15, 16], [16, 16], [15, 15], [25, 24], [24, 25], [25, 25]
])

# --- 2️⃣ Distance function ---
def euclidean(a, b):
    return np.linalg.norm(a - b)

# --- 3️⃣ HAC function with plotting ---
def hac_plot(data, method="single"):
    clusters = [[i] for i in range(len(data))]
    step = 1
    centroids = [data[i] for i in range(len(data))]
    
    plt.figure(figsize=(8,6))
    plt.scatter(data[:,0], data[:,1], c='red', label='Points')
    
    while len(clusters) > 1:
        min_dist = float('inf')
        to_merge = (0, 1)

        # Find closest clusters
        for i in range(len(clusters)):
            for j in range(i+1, len(clusters)):
                if method == "single":
                    d = min(euclidean(data[p1], data[p2]) 
                            for p1 in clusters[i] for p2 in clusters[j])
                elif method == "complete":
                    d = max(euclidean(data[p1], data[p2]) 
                            for p1 in clusters[i] for p2 in clusters[j])
                if d < min_dist:
                    min_dist = d
                    to_merge = (i, j)

        i, j = to_merge
        # Merge clusters
        new_cluster = clusters[i] + clusters[j]

        # Plot line connecting centroids of clusters being merged
        c1 = np.mean([data[p] for p in clusters[i]], axis=0)
        c2 = np.mean([data[p] for p in clusters[j]], axis=0)
        plt.plot([c1[0], c2[0]], [c1[1], c2[1]], 'k--', alpha=0.5)

        clusters = [clusters[x] for x in range(len(clusters)) if x not in [i,j]] + [new_cluster]
        step += 1

    plt.title(f"HAC ({method}-link) Merge Steps")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

# --- 4️⃣ Run HAC with plotting ---
print("=== Single-link HAC ===")
hac_plot(data, method="single")

print("=== Complete-link HAC ===")
hac_plot(data, method="complete")
