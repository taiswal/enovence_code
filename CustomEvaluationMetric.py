# Scenario 6: Custom Evaluation Metric
# Task: Implement a custom metric weighted_accuracy where class 0 has a weight of 1 and class 1 has a weight of 2.

from sklearn.metrics import make_scorer
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np


def weighted_accuracy(y_true, y_pred):
    correct = 0
    total = 0
    for true, pred in zip(y_true, y_pred):
        weight = 1 if true == 0 else 2
        total += weight
        if true == pred:
            correct += weight
    return correct / total


X, y = make_classification(n_samples=100, n_classes=2, weights=[0.6, 0.4], random_state=42)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


model = RandomForestClassifier()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


score = weighted_accuracy(y_test, y_pred)
print("Weighted Accuracy:", round(score, 2))
