import MonthlyDatatype


class YearlyDatatype:
    def __init__(self, year):
        self.year = int(year)
        self.months = self.createMonthlyList()
        self.numberOfMonths = 12
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
            if month.average is 0:
                del month
            else:
                self.average += month.average
                self.numberOfMonths = self.numberOfMonths -1
        try:
            self.average = self.average / self.numberOfMonths
        except:
            print("error YearlyDatatype.setData for year " + str(self.year) + " total = " + str(self.totalScore) +
                  " count = " + str(self.count))

    def returnDetails(self):
        return self.year, self.months, self.totalScore, self.count, self.average

