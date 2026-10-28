# Machine Learning Practical
# Setup:
#   pip install pandas numpy scikit-learn matplotlib
# Keep this code file and its matching data file in the SAME folder.
# Run from this folder after copying/renaming practicalN.txt to practicalN.py:
#   python practicalN.py
# Dataset path below is relative to the current working directory.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
data = pd.read_csv("practical4data.csv")  # For practical 4, change to practical4data.csv.
X = data.iloc[:, :-1].copy()
y = data.iloc[:, -1]
encoders = {}
for col in X.columns:
    encoders[col] = LabelEncoder()
    X[col] = encoders[col].fit_transform(X[col].astype(str))
target_encoder = LabelEncoder()
y_encoded = target_encoder.fit_transform(y)
model = DecisionTreeClassifier(criterion="entropy", random_state=42)
model.fit(X, y_encoded)
print(export_text(model, feature_names=list(X.columns)))
sample = {'Outlook':'Sunny', 'Temperature':'Cool', 'Humidity':'High', 'Wind':'Strong'}
sample_df = pd.DataFrame([sample])
for col in sample_df.columns:
    sample_df[col] = encoders[col].transform(sample_df[col].astype(str))
prediction = target_encoder.inverse_transform(model.predict(sample_df))[0]
print("New sample:", sample)
print("Predicted PlayTennis:", prediction)
