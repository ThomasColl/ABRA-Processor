# Load libraries
import datetime
import os

import matplotlib.pyplot as plt
import pandas.plotting


class yearlyDatatype:
    def __init__(self, year):
        self.year = int(year)
        self.totalScore = 0
        self.count = 0
        self.average = 0

    def addReview(self, review):
        self.totalScore += review
        self.count += 1

    def setAverage(self):
        try:
            self.average = self.totalScore / self.count
        except:
            print("getAverage Failure total score " + self.totalScore + " and count " + self.count)

    def returnDetails(self):
        return tuple(self.year, self.totalScore, self.count, self.average)


class normalisedDatatype:
    def __init__(self):
        self.dictOfYears = {}

    def addYear(self, yearlyData):
        self.dictOfYears[yearlyData.year] = yearlyData

    def isYearThere(self, year):
        if year in self.dictOfYears:
            return True
        else:
            return False

    def orderYears(self):
        return sorted(self.dictOfYears)

    def getAnnualAverages(self):
        for key, value in self.dictOfYears.items():
            value.setAverage()

    def getPlottableDict(self):

        plottableDict = {}
        for key, value in self.dictOfYears.items():
            plottableDict[key] = value.count
        return plottableDict

    def plotCount(self):
        plottableDict = {}
        for key, value in self.dictOfYears.items():
            plottableDict[key] = value.count
        plt.scatter(range(len(plottableDict)), sorted(plottableDict.values()))
        plt.show()

    def plotTotal(self):
        plottableDict = {}
        for key, value in self.dictOfYears.items():
            plottableDict[key] = value.totalScore
        plt.scatter(range(len(plottableDict)), sorted(plottableDict.values()))
        plt.show()

    def plotAverage(self):
        self.getAnnualAverages()
        plottableDict = {}
        for key, value in self.dictOfYears.items():
            plottableDict[key] = value.average
        plt.scatter(range(len(plottableDict)), sorted(plottableDict.values()))
        plt.show()


folderName = 'BrokenUpData'
url = "ratings_Books.csv"
names = ['user', 'item', 'rating', 'timestamp']

directory = os.fsencode(folderName)

numberOfBrokenUpDataFiles = 90
count = 1;
meanAverage = 0
shortestTimestamp = 0
longestTimestamp = 0
normalData = normalisedDatatype()
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
                normalData.addYear(yearlyDatatype(year))
        print(filename + " is complete")
        print(str(numberOfBrokenUpDataFiles - count) + " files left to process")

        if count == 1:
            shortestTimestamp = int(dataset['timestamp'].min())
            longestTimestamp = int(dataset['timestamp'].max())
        elif shortestTimestamp > int(dataset['timestamp'].min()) and int(dataset['timestamp'].min()) is not 0:
            shortestTimestamp = int(dataset['timestamp'].min())
        elif longestTimestamp < int(dataset['timestamp'].max()):
            longestTimestamp = int(dataset['timestamp'].max())
        if numberOfBrokenUpDataFiles >= count:
            count = count + 1
            meanAverage = meanAverage + dataset["rating"].mean()
        else:
            break;
    else:
        print("Why is this here?")
print("The data has processed and the results are as following:")
normalData.plotCount()
normalData.plotAverage()
normalData.plotTotal()
meanAverage = meanAverage / numberOfBrokenUpDataFiles
print("Average = " + meanAverage)
print("Shortest Timestamp = " + shortestTimestamp)
print("Longest Timestamp = " + longestTimestamp)
