import YearlyDatatype


class MonthlyDatatype:
    def __init__(self, m):
        self.month = int(m)
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
            print("MonthlyDatatype.setAverage Failure total score " + str(self.totalScore) + " and count " + str(self.count))

    def returnDetails(self):
        return tuple(self.month, self.totalScore, self.count, self.average)

