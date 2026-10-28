# Machine Learning Practical
# Setup:
#   pip install pandas numpy scikit-learn matplotlib
# Keep this code file and its matching data file in the SAME folder.
# Run from this folder after copying/renaming practicalN.txt to practicalN.py:
#   python practicalN.py
# Dataset path below is relative to the current working directory.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score, classification_report
data = pd.read_csv("practical5data.csv")  # CSV beside code.
X = data.iloc[:, :-1].astype(str)
y = data.iloc[:, -1].astype(str)
enc = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
Xn = enc.fit_transform(X)
le = LabelEncoder(); yn = le.fit_transform(y)
Xtr, Xte, ytr, yte = train_test_split(Xn, yn, test_size=0.3, random_state=42, stratify=yn)
model = CategoricalNB(); model.fit(Xtr, ytr)
pred = model.predict(Xte)
print("Accuracy:", round(accuracy_score(yte,pred)*100,2), "%")
print(classification_report(yte,pred,target_names=le.classes_, zero_division=0))
