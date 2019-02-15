#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 00:01:50 2018

@author: thomas coll and Patrick Browne
"""

# ---------------------------------- Libraries Section --------------------------------------------

import datetime
from calendar import monthrange

import MetaDatatype
import NormalisedDatatype
import YearlyDatatype
import MachineLearningMethods
import collections
import Plotter
import os
import numpy as np


import pandas.plotting
import matplotlib.pyplot as plt
from sklearn import linear_model

# ---------------------------------- Constants Declaration Section --------------------------------------------

numberOfBrokenUpDataFiles = 90
brokenUpDataFilesCount = 0
folderName = 'TestData'
names = ['user', 'item', 'rating', 'timestamp']

directory = os.fsencode(folderName)

normalData = NormalisedDatatype.NormalisedDatatype()
metadata = MetaDatatype.MetaDatatype(normalData, numberOfBrokenUpDataFiles)

# ---------------------------------- File Processing Section --------------------------------------------

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".csv"):
        dataset = pandas.read_csv(folderName + "/" + filename, names=names)
        print(filename + " has begun processing")
        for index, row in dataset.iterrows():
            year = datetime.datetime.fromtimestamp(int(row['timestamp'])).strftime('%Y')
            month = datetime.datetime.fromtimestamp(int(row['timestamp'])).strftime('%m')
            day = datetime.datetime.fromtimestamp(int(row['timestamp'])).strftime('%d')
            if normalData.isYearThere(int(year)) is True:
                normalData.dictOfYears[int(year)].addReview(int(row["rating"]), int(month), int(day))
            else:
                normalData.addYear(YearlyDatatype.YearlyDatatype(year))
        break
        print(filename + " is complete")
        metadata.setTimestamps(dataset['timestamp'])
    else:
        print("Why is this here?")
print("The data has processed")

normalData.setAnnualData()

# ---------------------------------- ML Section --------------------------------------------
# Note from here: 1 = count, 2 = total, 3 = average

print("Machine Learning Aspect Begun")
lists = MachineLearningMethods.createPlottableLists(normalData)
xList = lists[0]
metadata.setAbnormals(lists[4])
metadata.setNormals(lists[5])
linearModel = linear_model.LinearRegression()

print("New Key creation begun")
newDates = MachineLearningMethods.createNewKeys(2020, (2014, 7, 23))
print("New Keys creation complete")
finals = []
print("Data predicting begun")
for yList in (lists[1], lists[2], lists[3]):
    X = np.asarray(xList).reshape(-1, 1)
    Y = np.asarray(yList).reshape(-1, 1).ravel()
    linearModel.fit(X, Y)

    newValues = linearModel.predict(np.asarray(newDates).reshape(-1, 1)).tolist()
    finals.append(MachineLearningMethods.addListsTogether(yList, newValues))
print("Data predicting complete")
finalDates = MachineLearningMethods.addListsTogether(xList, newDates)
finalCount = finals[0]
finalTotal = finals[1]
finalAverage = finals[2]

listsToSendToPlotter = finalDates, finalCount, finalTotal, finalAverage

# ------------------------------------ Plotting Section -------------------------------------------

print("Plotting")
plotter = Plotter.Plotter(listsToSendToPlotter)
plotter.plotTheDictionary(1)
plotter.plotTheDictionary(2)
plotter.plotTheDictionary(3)

print("There was " + str(metadata.numberOfAbnormals) + ' abnormal results found')
print("There was " + str(metadata.numberOfNormals) + ' normal results found')
