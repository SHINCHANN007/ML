import random

data = [1, 2, 3, 10, 11, 12]

k = 2

m1 = random.choice(data)
m2 = random.choice(data)

iteration = 1

while True:
    print(f"\n--- Iteration {iteration} ---")

    k1 = []
    k2 = []

    for i in data:
        if abs(i - m1) < abs(i - m2):
            k1.append(i)
        else:
            k2.append(i)

    new_m1 = sum(k1) / len(k1) if k1 else m1
    new_m2 = sum(k2) / len(k2) if k2 else m2

    print(f"Cluster 1: {k1}  -> Centroid 1: {new_m1:.2f}")
    print(f"Cluster 2: {k2}  -> Centroid 2: {new_m2:.2f}")

    if new_m1 == m1 and new_m2 == m2:
        print(" Centroids stabilized. Clustering complete!")
        break
    else:
        m1 = new_m1
        m2 = new_m2
        iteration += 1
