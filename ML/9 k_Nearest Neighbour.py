# Machine Learning Practical
# Setup:
#   pip install pandas numpy scikit-learn matplotlib
# Keep this code file and its matching data file in the SAME folder.
# Run from this folder after copying/renaming practicalN.txt to practicalN.py:
#   python practicalN.py
# Dataset path below is relative to the current working directory.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
data = pd.read_csv("practical9data.csv")  # Iris CSV in same folder.
X = data.iloc[:, :-1]
y = data['species']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42,stratify=y)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train,y_train)
pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test,pred)*100,2), "%")
print("\nCorrect predictions:")
for actual, predicted, features in zip(y_test,pred,X_test.values):
    if actual == predicted: print("features=",features,"actual=",actual,"predicted=",predicted)
print("\nWrong predictions:")
wrong=0
for actual, predicted, features in zip(y_test,pred,X_test.values):
    if actual != predicted:
        wrong += 1; print("features=",features,"actual=",actual,"predicted=",predicted)
if wrong == 0: print("None")
