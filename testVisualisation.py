# Load libraries
import datetime
import metaDatatype
import normalisedDatatype
import yearlyDatatype
import os

import matplotlib.pyplot as plt
import pandas.plotting


folderName = 'BrokenUpData'
url = "ratings_Books.csv"
names = ['user', 'item', 'rating', 'timestamp']

directory = os.fsencode(folderName)

numberOfBrokenUpDataFiles = 90
normalData = normalisedDatatype.normalisedDatatype()
metadata = metaDatatype.metaDatatype(normalData, numberOfBrokenUpDataFiles)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".csv"):
        dataset = pandas.read_csv(folderName + "/" + filename, names=names)
        print(filename + " has begun processing")
        for index, row in dataset.iterrows():
            year = datetime.datetime.fromtimestamp(int(row['timestamp'])).strftime('%Y')
            if normalData.isYearThere(int(year)) is True:
                normalData.dictOfYears[int(year)].addReview(int(row["rating"]))
            else:
                normalData.addYear(yearlyDatatype.yearlyDatatype(year))
        print(filename + " is complete")
        metadata.setTimestamps(dataset['timestamp'])
        metadata.calculateTotalAverage()
        if metadata.hasAllFilesBeenProcessed() is True:
            break;
    else:
        print("Why is this here?")
print("The data has processed and the results are as following:")
normalData.plotCount()
normalData.plotAverage()
normalData.plotTotal()
metadata.printDetails()
