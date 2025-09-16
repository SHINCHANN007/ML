import numpy as np

# --- 1️⃣ Sample 2D points ---
data = np.array([
    [2, 3], [3, 3], [2, 2], [8, 8], [9, 8], [8, 9],
    [15, 16], [16, 16], [15, 15], [25, 24], [24, 25], [25, 25]
])

# --- 2️⃣ Distance function ---
def euclidean(a, b):
    return np.linalg.norm(a - b)

# --- 3️⃣ HAC function (fully hardcoded) ---
def hac_hardcoded(data, method="single"):
    # Start: each point is its own cluster
    clusters = [[i] for i in range(len(data))]
    step = 1
    print(f"\nInitial clusters: {clusters}\n")

    while len(clusters) > 1:
        min_dist = float('inf')
        to_merge = (0, 1)

        # Find closest clusters
        for i in range(len(clusters)):
            for j in range(i+1, len(clusters)):
                if method == "single":
                    # Single-link: minimum distance between points
                    d = min(euclidean(data[p1], data[p2]) 
                            for p1 in clusters[i] for p2 in clusters[j])
                elif method == "complete":
                    # Complete-link: maximum distance between points
                    d = max(euclidean(data[p1], data[p2]) 
                            for p1 in clusters[i] for p2 in clusters[j])
                if d < min_dist:
                    min_dist = d
                    to_merge = (i, j)

        i, j = to_merge
        # Merge clusters
        new_cluster = clusters[i] + clusters[j]
        clusters = [clusters[x] for x in range(len(clusters)) if x not in [i,j]] + [new_cluster]

        print(f"Step {step}: Merge clusters {i} and {j} at distance {min_dist:.2f}")
        print(f"Clusters now: {clusters}\n")
        step += 1

    return clusters

# --- 4️⃣ Run HAC ---
print("=== Single-link HAC ===")
final_single = hac_hardcoded(data, method="single")

print("=== Complete-link HAC ===")
final_complete = hac_hardcoded(data, method="complete")
