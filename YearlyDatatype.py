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
            months.append(MonthlyDatatype.MonthlyDatatype(month))
        return months

    def addReview(self, review, month):
        self.months[month-1].addReview(review)

    def setData(self):
        for month in self.months:
            self.totalScore += month.totalScore
            self.count += month.count
            month.setAverage()
            self.average += month.average
        try:
            self.average = self.average / 12
        except:
            print("error for setData for year " + self.year + " total = " + self.totalScore + " count = " + self.count)

    def returnDetails(self):
        return self.year, self.months, self.totalScore, self.count, self.average

