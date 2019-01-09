import NormalisedDatatype
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, data):
        self.normalData = data

    def plotYearlyCount(self):
        plottableDict = {}
        for key, value in self.normalData.dictOfYears.items():
            plottableDict[key] = value.count
        plt.scatter(range(len(plottableDict)), sorted(plottableDict.values()))
        plt.show()

    def plotYearlyTotal(self):
        plottableDict = {}
        for key, value in self.normalData.dictOfYears.items():
            plottableDict[key] = value.totalScore
        plt.scatter(range(len(plottableDict)), sorted(plottableDict.values()))
        plt.show()

    def plotYearlyAverage(self):
        plottableDict = {}
        for key, value in self.normalData.dictOfYears.items():
            plottableDict[key] = value.average
        plt.scatter(range(len(plottableDict)), sorted(plottableDict.values()))
        plt.show()

    def plotMonthlyCount(self):
        plottableDict = {}
        for key, value in self.normalData.dictOfYears.items():
            for month in self.normalData.dictOfYears[key].months:
                plottableDictStr = str(key) + str(month.month)
                plottableDict[int(plottableDictStr)] = month.count
        plt.scatter(range(len(plottableDict)), sorted(plottableDict.values()))
        plt.show()

    def plotMonthlyTotal(self):
        plottableDict = {}
        for key, value in self.normalData.dictOfYears.items():
            for month in self.normalData.dictOfYears[key].months:
                plottableDictStr = str(key) + str(month.month)
                plottableDict[int(plottableDictStr)] = month.totalScore
        plt.scatter(range(len(plottableDict)), sorted(plottableDict.values()))
        plt.show()

    def plotMonthlyAverage(self):
        plottableDict = {}
        for key, value in self.normalData.dictOfYears.items():
            for month in self.normalData.dictOfYears[key].months:
                plottableDictStr = str(key) + str(month.month)
                plottableDict[int(plottableDictStr)] = month.average
        plt.scatter(range(len(plottableDict)), sorted(plottableDict.values()))
        plt.show()

    def plotDailyCount(self):
        plottableDict = {}
        for key, value in self.normalData.dictOfYears.items():
            for month in self.normalData.dictOfYears[key].months:
                for day in month.days:
                    plottableDictStr = str(key) + str(day.day)
                    plottableDict[int(plottableDictStr)] = day.count
        plt.scatter(range(len(plottableDict)), sorted(plottableDict.values()))
        plt.show()

    def plotDailyTotal(self):
        plottableDict = {}
        for key, value in self.normalData.dictOfYears.items():
            for month in self.normalData.dictOfYears[key].months:
                for day in month.days:
                    plottableDictStr = str(key) + str(day.day)
                    plottableDict[int(plottableDictStr)] = day.totalScore
        plt.scatter(range(len(plottableDict)), sorted(plottableDict.values()))
        plt.show()

    def plotDailyAverage(self):
        plottableDict = {}
        for key, value in self.normalData.dictOfYears.items():
            for month in self.normalData.dictOfYears[key].months:
                for day in month.days:
                    plottableDictStr = str(key) + str(day.day)
                    plottableDict[int(plottableDictStr)] = day.average
        plt.scatter(range(len(plottableDict)), sorted(plottableDict.values()))
        plt.show()
