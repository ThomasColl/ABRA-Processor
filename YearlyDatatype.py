import MonthlyDatatype


class YearlyDatatype:
    def __init__(self, year):
        self.year = int(year)
        self.months = self.createMonthlyList()
        self.totalScore = 0
        self.count = 0
        self.average = 0

    def createMonthlyList(self):
        months = []
        for month in range(12):
            months.append(MonthlyDatatype.MonthlyDatatype(self.year, int(month + 1)))
        return months

    def addReview(self, review, month, day):
        self.months[month-1].addReview(review, day)

    def setData(self):
        for month in self.months:
            month.setData()
            self.totalScore += month.totalScore
            self.count += month.count
            self.average += month.average
        try:
            self.average = self.average / 12
        except:
            print("error YearlyDatatype.setData for year " + self.year + " total = " + self.totalScore + " count = " +
                  self.count)

    def returnDetails(self):
        return self.year, self.months, self.totalScore, self.count, self.average

