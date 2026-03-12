import numpy as np
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

np.random.seed(47)

# Reading iris classification data
iris = datasets.load_iris()
X = iris.data
Y = iris.target

# In the datasets, 2/3 is used as the training set and 1/3 as the test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33)
random_forest_clf = RandomForestClassifier(n_estimators=10, random_state=42)
random_forest_clf = random_forest_clf.fit(X_train, Y_train)
Y_predict = random_forest_clf.predict(X_test)
score = accuracy_score(Y_test, Y_predict)
print("Prediction accuracy of iris class:", score)
