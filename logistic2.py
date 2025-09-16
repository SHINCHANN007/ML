import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("lr.csv")

x = np.array(data["x"]).reshape(-1,1)
y = data["y"]


model = LogisticRegression()
model.fit(x,y)

x_val = np.linspace(0,10,100).reshape(-1,1)
y_val = model.predict_proba(x_val)

plt.scatter(x,y,color="red",label="ACTUAL POINTS")
plt.plot(x_val,y_val[:,1],color="blue",label="logistic curve")
plt.xlabel("HOURS study")
plt.ylabel("pass or fail")
plt.legend()
plt.show()