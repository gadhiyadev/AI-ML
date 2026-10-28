# Machine Learning Practical
# Setup:
#   pip install pandas numpy scikit-learn matplotlib
# Keep this code file and its matching data file in the SAME folder.
# Run from this folder after copying/renaming practicalN.txt to practicalN.py:
#   python practicalN.py
# Dataset path below is relative to the current working directory.

# Educational toy Bayesian-network-style demonstration; bundled rows are a SMALL sample,
# not the full standard Heart Disease dataset and not suitable for medical diagnosis.
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
data = pd.read_csv("practical7data.csv")  # Keep this CSV beside the code.
X = data[['age','sex','resting_bp','cholesterol']]
y = data['heart_disease']
Xtr, Xte, ytr, yte = train_test_split(X,y,test_size=0.3,random_state=42,stratify=y)
model = GaussianNB()  # Naive Bayes factorization used as a simple probabilistic baseline.
model.fit(Xtr,ytr)
print("Hold-out accuracy:", round(accuracy_score(yte,model.predict(Xte)),3))
patient = pd.DataFrame([[55,1,130,240]], columns=X.columns)
print("Demo patient features:", patient.iloc[0].to_dict())
print("Predicted class (0/1):", int(model.predict(patient)[0]))
print("WARNING: educational example only; not clinical advice.")
