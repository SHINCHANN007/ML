# --- 1. Hardcoded data ---
y  = [5, 7, 9, 11, 13]      # Dependent variable
x1 = [2, 4, 6, 8, 10]       # Feature 1
x2 = [1, 3, 5, 7, 9]        # Feature 2
x3 = [10, 9, 8, 7, 6]       # Feature 3

features = [x1, x2, x3]
feature_names = ["x1", "x2", "x3"]

# --- 2. Function to calculate Pearson correlation ---
def correlation(a, b):
    n = len(a)
    mean_a = sum(a)/n
    mean_b = sum(b)/n

    numerator = 0
    sum_a2 = 0
    sum_b2 = 0
    for i in range(n):
        numerator += (a[i]-mean_a)*(b[i]-mean_b)
        sum_a2 += (a[i]-mean_a)**2
        sum_b2 += (b[i]-mean_b)**2

    denominator = (sum_a2 * sum_b2)**0.5
    return numerator / denominator

# --- 3. Compute correlations ---
correlations = []
for i in range(len(features)):
    r = correlation(features[i], y)
    correlations.append([feature_names[i], r])

# --- 4. Sort by absolute correlation ---
for i in range(len(correlations)):
    for j in range(i+1, len(correlations)):
        if abs(correlations[j][1]) > abs(correlations[i][1]):
            correlations[i], correlations[j] = correlations[j], correlations[i]

# --- 5. Print results ---
print("Feature Correlation with y (sorted by strength):")
for f in correlations:
    print(f"{f[0]} : {f[1]:.4f}")
