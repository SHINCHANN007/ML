
data = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Weak", "Yes"],
]

attributes = ["Outlook", "Temperature", "Humidity", "Wind"]

from collections import Counter

# --- Gini index ---
def gini(examples):
    total = len(examples)
    counts = Counter(row[-1] for row in examples)
    return 1 - sum((c/total)**2 for c in counts.values())

# --- Gini gain ---
def gini_gain(examples, i):
    total = len(examples)
    vals = set(row[i] for row in examples)
    weighted = sum(len([r for r in examples if r[i]==v])/total *
                   gini([r for r in examples if r[i]==v]) for v in vals)
    return gini(examples) - weighted

# --- CART recursive ---
def cart(examples, attrs):
    labels = [row[-1] for row in examples]
    if labels.count(labels[0]) == len(labels):
        return labels[0]
    if not attrs:
        return Counter(labels).most_common(1)[0][0]

    gains = [gini_gain(examples, i) for i in range(len(attrs))]
    best = gains.index(max(gains))
    tree = {attrs[best]:{}}
    for val in set(row[best] for row in examples):
        subset = [row[:best]+row[best+1:] for row in examples if row[best]==val]
        subtree = cart(subset, attrs[:best]+attrs[best+1:])
        tree[attrs[best]][val] = subtree
    return tree

# --- Build tree ---
from pprint import pprint
pprint(cart(data, attributes))
