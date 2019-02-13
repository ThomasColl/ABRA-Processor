from calendar import monthrange


def __init__():
    print("Hello Patrick and Tom, I am ABRA")
def createNewKeys(yearToEnd, endDate):
    newDateYear = endDate[0]
    newDateMonth = endDate[1]
    newDateDay = endDate[2]

    newDates = []
    while newDateYear <= 2016:
        while newDateMonth <= 12:
            while newDateDay <= monthrange(newDateYear, newDateMonth)[1]:
                newDates.append(int(str(newDateYear) + str(newDateMonth) + str(newDateDay)))
                newDateDay = newDateDay + 1
            newDateMonth = newDateMonth + 1
            newDateDay = 1
        newDateYear = newDateYear + 1
        newDateMonth = 1
    return newDates


def createPlottableLists(normalisedData):
    abnormalCount = 0
    xList = []
    yListCount = []
    yListTotal = []
    yListAverage = []
    for year, years in sorted(normalisedData.dictOfYears.items()):
        for month in years.months:
            for day in month.days:
                xList.append(int(str(year) + str(month.month) + str(day.day)))
                yListCount.append(day.count)
                yListTotal.append(day.totalScore)
                if day.average < 1:
                    abnormalCount = abnormalCount +1
                yListAverage.append(day.average)
    return xList, yListCount, yListTotal, yListAverage, abnormalCount


def addListsTogether(realData, predictiveData):
    return realData + predictiveData

