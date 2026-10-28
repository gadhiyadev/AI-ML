# Machine Learning Practical
# Setup:
#   pip install pandas numpy scikit-learn matplotlib
# Keep this code file and its matching data file in the SAME folder.
# Run from this folder after copying/renaming practicalN.txt to practicalN.py:
#   python practicalN.py
# Dataset path below is relative to the current working directory.

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
data = pd.read_csv("practical8data.csv")  # Same CSV used for both algorithms.
X = StandardScaler().fit_transform(data[['x','y']])
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10).fit(X)
em = GaussianMixture(n_components=2, random_state=42).fit(X)  # EM algorithm
em_labels = em.predict(X)
print("k-Means labels:", kmeans.labels_)
print("EM/GMM labels:", em_labels)
print("k-Means silhouette:", round(silhouette_score(X,kmeans.labels_),3))
print("EM silhouette:", round(silhouette_score(X,em_labels),3))
plt.scatter(data.x,data.y,c=kmeans.labels_); plt.title("k-Means clustering"); plt.xlabel("x"); plt.ylabel("y"); plt.savefig("practical8_kmeans.png"); plt.show()
plt.scatter(data.x,data.y,c=em_labels); plt.title("EM (Gaussian Mixture) clustering"); plt.xlabel("x"); plt.ylabel("y"); plt.savefig("practical8_em.png"); plt.show()
print("Compare silhouette scores; higher is generally better for separated clusters.")
