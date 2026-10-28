# Machine Learning Practical
# Setup:
#   pip install pandas numpy scikit-learn matplotlib
# Keep this code file and its matching data file in the SAME folder.
# Run from this folder after copying/renaming practicalN.txt to practicalN.py:
#   python practicalN.py
# Dataset path below is relative to the current working directory.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
data = pd.read_csv("practical6data.csv")  # CSV file is beside this code.
X_train, X_test, y_train, y_test = train_test_split(
    data['message'], data['label'], test_size=0.33, random_state=42, stratify=data['label'])
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("Accuracy :", round(accuracy_score(y_test,pred),3))
print("Precision (pos):", round(precision_score(y_test,pred,pos_label='pos',zero_division=0),3))
print("Recall (pos):", round(recall_score(y_test,pred,pos_label='pos',zero_division=0),3))
print(classification_report(y_test,pred,zero_division=0))
for text in ["This is wonderful", "This is horrible"]:
    print(text, "=>", model.predict([text])[0])
