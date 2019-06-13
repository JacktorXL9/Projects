import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
Mushrooms = pd.read_csv('Mushrooms\mushrooms.csv')
columns = list(Mushrooms)

for i in columns:
    Mushrooms[i] = Mushrooms[i].astype('category')

Mushrooms_X = Mushrooms.drop('class', axis=1)
Mushrooms_Y = Mushrooms['class'].map({'e': 0, 'p': 1})
Mushrooms_X_onehot = Mushrooms_X.copy()
columns = list(Mushrooms_X)
for i in columns:
    Mushrooms_X_onehot = pd.get_dummies(Mushrooms_X_onehot, columns=[i],
    prefix=[i], drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(Mushrooms_X_onehot, 
Mushrooms_Y, test_size=0.25, random_state=42, shuffle=True)

ETCF = ExtraTreesClassifier()
ETCF.fit(X_train, y_train)
import_features = ETCF.feature_importances_
imp_col = []
for i in range(5):
    j = import_features.argmax()
    imp_col.append(X_train.columns[j])
    import_features[j]=0

X_train_reduced = pd.DataFrame()
X_test_reduced = pd.DataFrame()

for col in imp_col:
    X_train_reduced[col] = X_train[col]
for col in imp_col:
    X_test_reduced[col] = X_test[col]
Logreg = LogisticRegressionCV()
Logreg.fit(X_train_reduced,y_train)
predictions = Logreg.predict(X_test_reduced)
print(classification_report(y_test, predictions))