"""
n_classifiers = 1

Train %: 0.9132231404958677
Test %: 0.7377049180327869

n_classifiers = 2

Train %: 0.859504132231405
Test %: 0.6721311475409836

n_classifiers = 3

Train %: 0.9421487603305785
Test %: 0.8360655737704918

n_classifiers = 4

Train %: 0.9628099173553719
Test %: 0.7868852459016393

n_classifiers = 5

Train %: 0.9793388429752066
Test %: 0.8032786885245902

n_classifiers = 6

Train %: 0.9710743801652892
Test %: 0.7704918032786885

n_classifiers = 7

Train %: 0.987603305785124
Test %: 0.7377049180327869

n_classifiers = 8

Train %: 0.987603305785124
Test %: 0.8524590163934426

n_classifiers = 9

Train %: 0.987603305785124
Test %: 0.9016393442622951

n_classifiers = 10

Train %: 0.987603305785124
Test %: 0.8688524590163934

"""

# import libraries

import pandas as pd
import numpy as np
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# import data

heartDisease = pd.read_csv("heart.csv")

# define rows and columns

X = heartDisease.drop(['target'], axis = 1)
Y = heartDisease['target']

# machine learning work

classifier = RandomForestClassifier(n_estimators = 10)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)
classifier.fit(X_train, Y_train)

Y_prediction = classifier.predict(X_test)

# print(classifier.score(X_train, Y_train))
# print(classifier.score(X_test, Y_test))

# statistics things

print(classification_report(Y_test, Y_prediction))

print(confusion_matrix(Y_test, Y_prediction))

print(accuracy_score(Y_test, Y_prediction))

# improve ML model

np.random.seed(42)

for counter in range(10, 100, 10):
    print(f"Trying model with {counter} estimators....")
    classifier = RandomForestClassifier(n_estimators = counter).fit(X_train, Y_train)
    print(f"Model accuracy on test set: {classifier.score(X_test, Y_test) * 100:0.2f}%")
    print("")