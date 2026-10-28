# Machine Learning Practical
# Setup:
#   pip install pandas numpy scikit-learn matplotlib
# Keep this code file and its matching data file in the SAME folder.
# Run from this folder after copying/renaming practicalN.txt to practicalN.py:
#   python practicalN.py
# Dataset path below is relative to the current working directory.

import pandas as pd
data = pd.read_csv("practical1data.csv")  # Put CSV beside this file.
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
hypothesis = None
for row, label in zip(X, y):
    if label == "Yes":
        if hypothesis is None:
            hypothesis = row.copy()
        else:
            for j, value in enumerate(row):
                if hypothesis[j] != value:
                    hypothesis[j] = "?"
print("Training data:\n", data)
print("Final most-specific hypothesis:", hypothesis)
