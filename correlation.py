
import numpy as np
import pandas as pd

data = pd.read_csv("pr.csv")

x1 = data["x"]
y1 = data["y"]


def cor(a,b):
    xmean = np.mean(a)
    ymean = np.mean(b)



    num = np.sum( (a-xmean)*(b-ymean) )
    denom = np.sqrt( np.sum( ((a-xmean)**2)*((b-ymean)**2) ) )

    r = num/denom
    print(r)

cor(x1,y1)