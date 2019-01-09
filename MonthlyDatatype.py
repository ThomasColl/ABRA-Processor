import DailyDatatype
from calendar import monthrange


class MonthlyDatatype:
    def __init__(self, year, month):
        self.month = int(month)
        self.numberOfDays = monthrange(year, month)[1]
        self.days = self.createDailyList()
        self.totalScore = 0
        self.count = 0
        self.average = 0

    def createDailyList(self):
        days = []
        for day in range(self.numberOfDays):
            days.append(DailyDatatype.DailyDatatype(day))
        return days

    def addReview(self, review, day):
        self.days[day-1].addReview(review)

    def setData(self):
        for day in self.days:
            self.totalScore += day.totalScore
            self.count += day.count
            day.setAverage()
            self.average += day.average
        try:
            self.average = self.average / self.numberOfDays
        except:
            print("error MonthlyDatatype.setData for year " + self.year + " total = " + self.totalScore + " count = " +
                  self.count)

    def returnDetails(self):
        return self.month, self.days, self.totalScore, self.count, self.average
