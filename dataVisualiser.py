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
#TODO: Refactor File Retrieval To Come From GitHub Rather Than Locally
#TODO: Introduce bookDataType
#TODO: Introduce flask UI

numberOfBrokenUpDataFiles = 90
brokenUpDataFilesCount = 0
folderName = 'BrokenUpData'
url = "https://raw.githubusercontent.com/ThomasColl/AmazonBigDataProject/master/BrokenUpData/" + str(brokenUpDataFilesCount) + ".csv"
names = ['user', 'item', 'rating', 'timestamp']

directory = os.fsencode(folderName)

normalData = NormalisedDatatype.NormalisedDatatype()
metadata = MetaDatatype.MetaDatatype(normalData, numberOfBrokenUpDataFiles)

# while brokenUpDataFilesCount <= numberOfBrokenUpDataFiles:
#     #dataset = pandas.read_csv(url, names=names)
#     s = requests.get(url).content
#     c = pd.read_csv(io.StringIO(s.decode('utf-8')))
#     print(c.describe())

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".csv"):
        dataset = pandas.read_csv(folderName + "/" + filename, names=names)
        print(filename + " has begun processing")
        for index, row in dataset.iterrows():
            year = datetime.datetime.fromtimestamp(int(row['timestamp'])).strftime('%Y')
            month = datetime.datetime.fromtimestamp(int(row['timestamp'])).strftime('%m')
            if normalData.isYearThere(int(year)) is True:
                normalData.dictOfYears[int(year)].addReview(int(row["rating"]), int(month))
            else:
                normalData.addYear(YearlyDatatype.YearlyDatatype(year))
        print(filename + " is complete")
        metadata.setTimestamps(dataset['timestamp'])
        if metadata.hasAllFilesBeenProcessed() is True:
            break;
    else:
        print("Why is this here?")
print("The data has processed and the results are as following:")

normalData.setAnnualData()
plotter = Plotter.Plotter(normalData)
plotter.plotYearlyCount()
plotter.plotMonthlyCount()
plotter.plotYearlyAverage()
plotter.plotMonthlyAverage()
plotter.plotYearlyTotal()
plotter.plotMonthlyTotal()
metadata.calculateTotalAverage()
metadata.printDetails()
