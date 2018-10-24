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

