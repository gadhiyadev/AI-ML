# Machine Learning Practical
# Setup:
#   pip install pandas numpy scikit-learn matplotlib
# Keep this code file and its matching data file in the SAME folder.
# Run from this folder after copying/renaming practicalN.txt to practicalN.py:
#   python practicalN.py
# Dataset path below is relative to the current working directory.

import pandas as pd
data = pd.read_csv("practical2data.csv")  # Keep CSV in the same folder.
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
n = X.shape[1]
S = ['Ø'] * n
G = [['?'] * n]
for row, label in zip(X, y):
    if label == 'Yes':
        for j in range(n):
            if S[j] == 'Ø': S[j] = row[j]
            elif S[j] != row[j]: S[j] = '?'
        G = [g for g in G if all(g[j] == '?' or g[j] == S[j] for j in range(n))]
    else:
        new_G = []
        for g in G:
            for j in range(n):
                if S[j] not in ('Ø','?') and g[j] == '?' and row[j] != S[j]:
                    spec = g.copy(); spec[j] = S[j]; new_G.append(spec)
        G = new_G or G
print("Specific boundary S:", S)
print("General boundary G:")
for h in G: print(h)
print("\nNote: this is a compact categorical Candidate-Elimination demonstration.")
