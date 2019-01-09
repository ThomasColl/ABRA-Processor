#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 00:01:50 2018

@author: thomas
"""
import os
import pandas
from sklearn import model_selection

numberOfBrokenUpDataFiles = 90
brokenUpDataFilesCount = 0
folderName = 'BrokenUpData'
url = "https://raw.githubusercontent.com/ThomasColl/AmazonBigDataProject/master/BrokenUpData/" + str(brokenUpDataFilesCount) + ".csv"
names = ['user', 'item', 'rating', 'timestamp']

directory = os.fsencode(folderName)


# while brokenUpDataFilesCount <= numberOfBrokenUpDataFiles:
#     #dataset = pandas.read_csv(url, names=names)
#     s = requests.get(url).content
#     c = pd.read_csv(io.StringIO(s.decode('utf-8')))
#     print(c.describe())

# Python version
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
filename = os.fsdecode("BrokenUpData")
dataset = pandas.read_csv(folderName + "/" + filename, names=names)
        print(filename + " has begun processing")
        for index, row in dataset.iterrows():
            for name, model in models:
                kfold = model_selection.KFold(n_splits=10, random_state=seed)
                cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
                results.append(cv_results)
                names.append(name)
                msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
                print(msg)