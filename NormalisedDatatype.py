import matplotlib.pyplot as plt


class NormalisedDatatype:
    def __init__(self):
        self.dictOfYears = {}

    def addYear(self, yearlyData):
        self.dictOfYears[yearlyData.year] = yearlyData

    def isYearThere(self, year):
        if year in self.dictOfYears:
            return True
        else:
            return False

    def setAnnualData(self):
        for key, value in self.dictOfYears.items():
            value.setData()

