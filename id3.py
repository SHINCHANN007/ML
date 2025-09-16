import math
from collections import Counter
data = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Weak", "Yes"],
]

attrs = ["Outlook","Temperature","Humidity","Wind"]

# Entropy function
def entropy(examples):
    total = len(examples)
    counts = Counter([row[-1] for row in examples])
    return -sum((c/total)*math.log2(c/total) for c in counts.values())

# Information Gain
def info_gain(examples, i):
    total = len(examples)
    vals = set(row[i] for row in examples)
    return entropy(examples) - sum(len([r for r in examples if r[i]==v])/total * 
                                   entropy([r for r in examples if r[i]==v]) for v in vals)

# ID3
def id3(examples, attrs):
    labels = [row[-1] for row in examples]
    if labels.count(labels[0])==len(labels): return labels[0]
    if not attrs: return Counter(labels).most_common(1)[0][0]
    gains = [info_gain(examples,i) for i in range(len(attrs))]
    best = gains.index(max(gains))
    tree = {attrs[best]:{}}
    for val in set(row[best] for row in examples):
        subset = [row[:best]+row[best+1:] for row in examples if row[best]==val]
        subtree = id3(subset, attrs[:best]+attrs[best+1:])
        tree[attrs[best]][val] = subtree
    return tree

# Build tree
from pprint import pprint
pprint(id3(data, attrs))
