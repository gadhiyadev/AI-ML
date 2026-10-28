# Machine Learning Practical
# Setup:
#   pip install pandas numpy scikit-learn matplotlib
# Keep this code file and its matching data file in the SAME folder.
# Run from this folder after copying/renaming practicalN.txt to practicalN.py:
#   python practicalN.py
# Dataset path below is relative to the current working directory.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("practical10data.csv")  # Local sample in same folder; format resembles tips.csv.
# Locally Weighted Regression (LOWESS-style local linear regression), implemented from scratch.
X = data['total_bill'].to_numpy(dtype=float)
y = data['tip'].to_numpy(dtype=float)
def locally_weighted_prediction(x_query, x, y, tau=4.0):
    # Gaussian kernel weights; tau controls locality.
    weights = np.exp(-((x - x_query)**2) / (2 * tau**2))
    design = np.column_stack([np.ones(len(x)), x])
    W = np.diag(weights)
    beta = np.linalg.pinv(design.T @ W @ design) @ design.T @ W @ y
    return beta[0] + beta[1] * x_query
grid = np.linspace(X.min(), X.max(), 150)
pred = np.array([locally_weighted_prediction(q,X,y,tau=4.0) for q in grid])
plt.scatter(X,y,label='Observed data')
plt.plot(grid,pred,label='Locally weighted regression')
plt.xlabel('Total bill'); plt.ylabel('Tip'); plt.title('Locally Weighted Regression')
plt.legend(); plt.tight_layout(); plt.savefig('practical10_graph.png'); plt.show()
print("Graph saved as practical10_graph.png")
