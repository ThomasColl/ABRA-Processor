class MetaDatatype:
    def __init__(self, normalisedData, numFiles):
        self.yearlyData = normalisedData
        self.numberOfFiles = numFiles
        self.fileCount = 1
        self.totalAverage = 0
        self.totalCount = 0
        self.totalScore = 0
        self.longestTimestamp = 0
        self.shortestTimestamp = 0
        self.numberOfAbnormals = 0
        self.numberOfNormals = 0

    def setTimestamps(self, timestamp):
        if self.longestTimestamp == 0 and self.shortestTimestamp == 0:
            self.shortestTimestamp = timestamp.min()
            self.longestTimestamp = timestamp.max()
        elif self.shortestTimestamp > timestamp.min() and timestamp.min() is not 0:
            self.shortestTimestamp = timestamp.min()
        elif self.longestTimestamp < timestamp.max():
            self.longestTimestamp = timestamp.max()

    def setAbnormals(self, numberOfAbnormals):
        self.numberOfAbnormals = numberOfAbnormals

    def setNormals(self, numberOfNormals):
        self.numberOfNormals = numberOfNormals

    def calculateTotalAverage(self):
        total = 0
        count = 0
        for key, value in self.yearlyData.dictOfYears.items():
            total += value.average
            count += 1
        try:
            self.totalAverage = total / count
        except:
            print("metadatatype.calculatetotalaverage error. Total = " + str(total) + " Count = " + str(count))
            self.totalAverage = 0

    def indentCounter(self):
        self.fileCount += 1

    def numberOfFilesLeftToProcess(self):
        print(str(self.numberOfFiles - self.fileCount) + " files left to process")

    def hasAllFilesBeenProcessed(self):
        if self.fileCount != self.numberOfFiles:
            self.numberOfFilesLeftToProcess()
            self.indentCounter()
            return False
        else:
            return True

    def printDetails(self):
        print("Average = " + str(self.totalAverage))
        print("Shortest Timestamp = " + str(self.shortestTimestamp))
        print("Longest Timestamp = " + str(self.longestTimestamp))
