import NormalisedDatatype
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, data):
        self.normalData = data

    def plotTheDictionary(self, dictionaryToPlot, type):
        plt.plot(range(len(dictionaryToPlot)), sorted(dictionaryToPlot.values()), c="Red", zorder=2)
        # plt.scatter(range(len(dictionaryToPlot)), sorted(dictionaryToPlot.values()), c="Red", s=5, zorder=2)
        if type is 1:
            plt.title("Amazon Book Reviews Count (1996-2014)", fontsize=24)
            plt.xlabel("Count", fontsize=16)
        elif type is 2:
            plt.title("Amazon Book Reviews Total Review Score (1996-2014)", fontsize=24)
            plt.xlabel("Total Score", fontsize=16)
        else:
            plt.title("Amazon Book Reviews Average Review Score (1996-2014)", fontsize=24)
            plt.xlabel("Score", fontsize=16)
        plt.ylabel("Time", fontsize=16)
        plt.show()

    def plotDailyCount(self):
        plottableDict = {}
        for key, value in self.normalData.dictOfYears.items():
            for month in self.normalData.dictOfYears[key].months:
                for day in month.days:
                    plottableDictStr = str(key) + str(month.month) + str(day.day)
                    plottableDict[int(plottableDictStr)] = day.count
        self.plotTheDictionary(plottableDict, 1)

    def plotDailyTotal(self):
        plottableDict = {}
        for key, value in self.normalData.dictOfYears.items():
            for month in self.normalData.dictOfYears[key].months:
                for day in month.days:
                    plottableDictStr = str(key) + str(month.month) + str(day.day)
                    plottableDict[int(plottableDictStr)] = day.totalScore
        self.plotTheDictionary(plottableDict, 2)

    def plotDailyAverage(self):
        plottableDict = {}
        for key, value in self.normalData.dictOfYears.items():
            for month in self.normalData.dictOfYears[key].months:
                for day in month.days:
                    plottableDictStr = str(key) + str(month.month) + str(day.day)
                    plottableDict[int(plottableDictStr)] = day.average
        self.plotTheDictionary(plottableDict, 3)

