import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, data):
        self.xList = data[0]
        self.yListCount = data[1]
        self.yListTotal = data[2]
        self.yListAverage = data[3]

    def plotTheDictionary(self, type):
        # plt.scatter(range(len(dictionaryToPlot)), sorted(dictionaryToPlot.values()), c="Red", s=5, zorder=2)
        if type is 1:
            plt.plot(range(len(self.xList)), self.yListCount, c="Red", zorder=2)
            plt.title("Count (1996-2014)", fontsize=20)
            plt.xlabel("Count", fontsize=10)
        elif type is 2:
            plt.plot(range(len(self.xList)), self.yListTotal, c="Red", zorder=2)
            plt.title("Total Score (1996-2014)", fontsize=20)
            plt.xlabel("Total Score", fontsize=10)
        else:
            plt.plot(range(len(self.xList)), self.yListAverage, c="Red", zorder=2)
            plt.title("Average Score (1996-2014)", fontsize=20)
            plt.xlabel("Score", fontsize=10)
        plt.ylabel("Time", fontsize=10)
        plt.show()
