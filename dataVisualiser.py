# Load libraries
import datetime
import MetaDatatype
import NormalisedDatatype
import YearlyDatatype
import Plotter
import pandas as pd
import io
import requests
import os

import matplotlib.pyplot as plt
import pandas.plotting

#TODO: Implement parrellisation
#TODO: Introduce develop datatype
#TODO: Introduce flask UI

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
        if metadata.hasAllFilesBeenProcessed() is True:
            break
    else:
        print("Why is this here?")
print("The data has processed and the results are as following:")

normalData.setAnnualData()
plotter = Plotter.Plotter(normalData)
plotter.plotDailyCount()
plotter.plotDailyAverage()
plotter.plotDailyTotal()
metadata.calculateTotalAverage()
metadata.printDetails()

