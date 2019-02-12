#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 00:01:50 2018

@author: thomas
"""
import datetime
import pandas
from sklearn import model_selection
import numpy as np
import os

import NormalisedDatatype

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

normalData = NormalisedDatatype.NormalisedDatatype()
names = ['user', 'item', 'rating', 'timestamp']
folderName = 'TestData'
directory = os.fsencode(folderName)

x_list = []
y_list = []
seed = 7
validation_size = 0.20
scoring = 'accuracy'

models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".csv"):
        dataset = pandas.read_csv(folderName + "/" + filename, names=names)
        print(filename + " has begun processing")
        for index, row in dataset.iterrows():
            x_list.append(int(row['timestamp']))
            y_list.append(int(row["rating"]))

X = np.asarray(x_list).reshape(-1, 1)
Y = np.asarray(y_list).reshape(-1, 1).ravel()

X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size,
                                                                                random_state=seed)
results = []
machine_names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    machine_names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
