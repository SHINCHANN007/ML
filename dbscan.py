import numpy as np
import math

points = {
    'P1': (3, 7), 'P2': (4, 6), 'P3': (5, 5), 'P4': (6, 4),
    'P5': (7, 3), 'P6': (6, 2), 'P7': (7, 2), 'P8': (8, 4),
    'P9': (3, 3), 'P10': (2, 6), 'P11': (3, 5), 'P12': (2, 4)
}

eps = 1.9
mx = 4

def dis(a, b):
    return math.dist(a, b)

def findpadosi(point):
    return [
        q for q in points
        if q != point and dis(points[point], points[q]) <= eps
    ]

label = {}

for p in points:
    neighbour = findpadosi(p)

    if len(neighbour) + 1 >= mx:
        label[p] = "core"
    elif any(label.get(n) for n in neighbour):
        label[p] = "border"
    else:
        label[p] = 'noise'

for p in points:
    print(f"{p}: {label[p]}")
