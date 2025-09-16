
import numpy as np
import random
import pandas as pd

data = pd.read_csv("kmean.csv")

x = np.array(data["x"])
y = np.array(data["y"])

df = np.column_stack((x,y))

k = 3

m1 = random.choice(df)
m2 = random.choice(df)
m3 = random.choice(df)

centroid = np.array([m1,m2,m3],dtype=float)

it = 1

while True:

    lable = []

    for idx,points in enumerate(df):

        c1 = np.linalg.norm(points-centroid[0])
        c2 = np.linalg.norm(points-centroid[1])
        c3 = np.linalg.norm(points-centroid[2])     

        distance = [c1,c2,c3]

        cluster = np.argmin(distance)
        print(f"{points}  {c1:<15f}  {c2:<15f}  {c2:<15f}  {cluster}")
        
        lable.append(cluster)
    
    lable = np.array(lable)

    newcentroid = np.array([data[lable == i].mean(axis=0) for i in range(k)])

    print("\nNew Centroids:")
    for idx, c in enumerate(newcentroid):
        print(f"C{idx}: {c}")

    if np.allclose(newcentroid,centroid):
        print("DONE FOUND CENTROID")
        break
    else:
        
        centroid = newcentroid
        it+=1

    