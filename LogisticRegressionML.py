#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 00:01:50 2018

@author: thomas
"""

# Load libraries
import datetime
import MetaDatatype
import NormalisedDatatype
import YearlyDatatype
import Plotter
import os
import numpy as np


import pandas.plotting

numberOfBrokenUpDataFiles = 90
brokenUpDataFilesCount = 0
folderName = 'BrokenUpData'
names = ['user', 'item', 'rating', 'timestamp']

directory = os.fsencode(folderName)

normalData = NormalisedDatatype.NormalisedDatatype()
metadata = MetaDatatype.MetaDatatype(normalData, numberOfBrokenUpDataFiles)

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
        print(filename + " is complete")
        metadata.setTimestamps(dataset['timestamp'])
    else:
        print("Why is this here?")
    break
print("The data has processed and the results are as following:")

normalData.setAnnualData()

# Do Machine Learning aspect now!
plottableDict = {}
for key, value in normalData.dictOfYears.items():
    for month in normalData.dictOfYears[key].months:
        for day in month.days:
            plottableDictStr = int(str(key) + str(month.month) + str(day.day))
            plottableDict[plottableDictStr] = day.count
X = np.asarray(range(len(plottableDict))).reshape(-1, 1)
Y = np.asarray(sorted(plottableDict.values())).reshape(-1, 1).ravel()
