import numpy as np

# Sample data
x = [2, 4, 6, 8, 10]
y = [1, 3, 5, 7, 9]

# Step 1: Calculate means
mean_x = sum(x)/len(x)
mean_y = sum(y)/len(y)

# Step 2: Calculate numerator and denominator
num = sum((xi - mean_x)*(yi - mean_y) for xi, yi in zip(x,y))
den_x = sum((xi - mean_x)**2 for xi in x)
den_y = sum((yi - mean_y)**2 for yi in y)

# Step 3: Pearson correlation
r = num / (den_x**0.5 * den_y**0.5)

print(f"Correlation coefficient r = {r:.4f}")
