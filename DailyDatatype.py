class DailyDatatype:
    def __init__(self, day):
        self.day = int(day)
        self.totalScore = 0
        self.count = 0
        self.average = 0

    def addReview(self, review):
        self.totalScore += review
        self.count += 1

    def setAverage(self):
        try:
            self.average = self.totalScore / self.count
            return self.average
        except:
            print("DailyDatatype.setAverage Failure total score " + str(self.totalScore) + " and count " +
                  str(self.count) + " removing from data")
            return 0

    def returnDetails(self):
        return tuple(self.day, self.totalScore, self.count, self.average)
