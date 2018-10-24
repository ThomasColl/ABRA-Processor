import pandas

class metaDatatype:
    def __init__(self, normalisedData, numFiles):
        self.yearlyData = normalisedData
        self.numberOfFiles = numFiles
        self.fileCount = 1
        self.totalAverage = 0
        self.totalCount = 0
        self.totalScore = 0
        self.longestTimestamp = 0
        self.shortestTimestamp = 0

    def setTimestamps(self, timestamp):
        if self.longestTimestamp == 0 and self.shortestTimestamp == 0:
            self.shortestTimestamp = timestamp.min()
            self.longestTimestamp = timestamp.max()
        elif self.shortestTimestamp > timestamp.min() and timestamp.min() is not 0:
            self.shortestTimestamp = timestamp.min()
        elif self.longestTimestamp < timestamp.max():
            self.longestTimestamp = timestamp.max()

    #TODO: create average method

    def indentCounter(self):
        self.fileCount += 1

    def numberOfFilesLeftToProcess(self):
        print(self.numberOfFiles - self.fileCount)

    def hasAllFilesBeenProcessed(self):
        if self.fileCount == self.numberOfFiles:
            self.numberOfFilesLeftToProcess()
            self.indentCounter()
            return False
        return True

    def printDetails(self):
        print("Average = " + str(self.totalAverage))
        print("Shortest Timestamp = " + str(self.shortestTimestamp))
        print("Longest Timestamp = " + str(self.longestTimestamp))
