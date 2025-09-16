
data = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Weak", "Yes"],
]

attributes = ["Outlook", "Temperature", "Humidity", "Wind"]

# --- Step 1: Separate by class ---
separated = {}
for row in data:
    label = row[-1]
    if label not in separated:
        separated[label] = []
    separated[label].append(row[:-1])

# --- Step 2: Calculate probabilities ---
def prob(x, feature_idx, cls):
    values = [row[feature_idx] for row in separated[cls]]
    return values.count(x) / len(values)

# --- Step 3: Predict function ---
def predict(test):
    probs = {}
    total_rows = len(data)
    for cls in separated:
        cls_prob = len(separated[cls])/total_rows
        for i, val in enumerate(test):
            cls_prob *= prob(val, i, cls)
        probs[cls] = cls_prob
    return max(probs, key=probs.get)

# --- Step 4: Test ---
test_point = ["Sunny", "Cool", "High", "Strong"]
prediction = predict(test_point)
print(f"Test point {test_point} → Prediction: {prediction}")
