import numpy as np

# --- 1. Hardcoded data ---
y  = [5, 7, 9, 11, 13]      # Dependent variable
x1 = [2, 4, 6, 8, 10]       # Feature 1
x2 = [1, 3, 5, 7, 9]        # Feature 2
x3 = [10, 9, 8, 7, 6]       # Feature 3

features = [x1, x2, x3]
feature_names = ["x1", "x2", "x3"]

# --- 2. Function to calculate Pearson correlation ---
def correlation(a, b):
    mean_a = sum(a)/len(a)
    mean_b = sum(b)/len(b)
    numerator = sum((ai - mean_a)*(bi - mean_b) for ai, bi in zip(a, b))
    denominator = (sum((ai - mean_a)**2 for ai in a) * sum((bi - mean_b)**2 for bi in b))**0.5
    return numerator / denominator

# --- 3. Compute correlations ---
correlations = []
for name, feature in zip(feature_names, features):
    r = correlation(feature, y)
    correlations.append((name, r))

# --- 4. Sort correlations by absolute value (most correlated first) ---
correlations.sort(key=lambda x: abs(x[1]), reverse=True)

# --- 5. Print results nicely ---
print("Feature Correlation with y (sorted by strength):")
for name, r in correlations:
    print(f"{name:<3} : {r:.4f}")
