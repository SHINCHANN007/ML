
import numpy as np
import matplotlib.pyplot as plt

x = np.array([5,15,25,35,45,55])
y = np.array([5,20,14,32,22,38])

n = len(x)

sumxy =np.sum(x*y)
sumx =np.sum(x) 
sumy =np.sum(y)
sumx2 =np.sum(x**2) 
sumy2 =np.sum(y**2)

slope = (n*sumxy - sumx*sumy)/(n*sumx2-sumx**2)

intercept = (sumy - slope*sumx)/n

print(f"Equations : y = {intercept:.3f}- {slope} * x")

print("x    |   y   |   y_pred")
for i in range(len(x)):
    y_pred = intercept + slope*(x[i])

    print(f"{x[i]}  |   {y[i]}  |   {y_pred:.2f}")


plt.scatter(x,y,color="blue",label="ACTUAL DATA")
plt.plot(x,intercept+slope*(x),color="red",label="PREDICTED DATA")
plt.xlabel("x label")
plt.ylabel("y label")
plt.legend()
plt.show()

