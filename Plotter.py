import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, data):
        self.normalData = data

    def plotTheDictionary(self, dictionaryToPlot, type):
        plt.plot(range(len(dictionaryToPlot)), sorted(dictionaryToPlot.values()), c="Red", zorder=2)
        # plt.scatter(range(len(dictionaryToPlot)), sorted(dictionaryToPlot.values()), c="Red", s=5, zorder=2)
        if type is 1:
            plt.title("Count (1996-2014)", fontsize=20)
            plt.xlabel("Count", fontsize=10)
        elif type is 2:
            plt.title("Total Score (1996-2014)", fontsize=20)
            plt.xlabel("Total Score", fontsize=10)
        else:
            plt.title("Average Score (1996-2014)", fontsize=20)
            plt.xlabel("Score", fontsize=10)
        plt.ylabel("Time", fontsize=10)
        plt.show()

    def plotDailyCount(self):
        plottableDict = {}
        for key, value in self.normalData.dictOfYears.items():
            for month in self.normalData.dictOfYears[key].months:
                for day in month.days:
                    plottableDictStr = int(str(key) + str(month.month) + str(day.day))
                    plottableDict[plottableDictStr] = day.count
        self.plotTheDictionary(plottableDict, 1)

    def plotDailyTotal(self):
        plottableDict = {}
        for key, value in self.normalData.dictOfYears.items():
            for month in self.normalData.dictOfYears[key].months:
                for day in month.days:
                    plottableDictStr = int(str(key) + str(month.month) + str(day.day))
                    plottableDict[plottableDictStr] = day.totalScore
        self.plotTheDictionary(plottableDict, 2)

    def plotDailyAverage(self):
        plottableDict = {}
        for key, value in self.normalData.dictOfYears.items():
            for month in self.normalData.dictOfYears[key].months:
                for day in month.days:
                    plottableDictStr = int(str(key) + str(month.month) + str(day.day))
                    plottableDict[plottableDictStr] = day.average
        self.plotTheDictionary(plottableDict, 3)

