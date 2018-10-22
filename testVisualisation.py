# Load libraries
import os

import matplotlib.pyplot as plt
import pandas.plotting


def getYear(timestamp):
    if years["1996"][0] <= timestamp < years["1997"][0]:
        return "1996"
    elif years["1997"][0] <= timestamp < years["1998"][0]:
        return "1997"
    elif years["1998"][0] <= timestamp < years["1999"][0]:
        return "1998"
    elif years["1999"][0] <= timestamp < years["2000"][0]:
        return "1999"
    elif years["2000"][0] <= timestamp < years["2001"][0]:
        return "2000"
    elif years["2001"][0] <= timestamp < years["2002"][0]:
        return "2001"
    elif years["2002"][0] <= timestamp < years["2003"][0]:
        return "2002"
    elif years["2003"][0] <= timestamp < years["2004"][0]:
        return "2003"
    elif years["2004"][0] <= timestamp < years["2005"][0]:
        return "2004"
    elif years["2005"][0] <= timestamp < years["2006"][0]:
        return "2005"
    elif years["2006"][0] <= timestamp < years["2007"][0]:
        return "2006"
    elif years["2007"][0] <= timestamp < years["2008"][0]:
        return "2007"
    elif years["2008"][0] <= timestamp < years["2009"][0]:
        return "2008"
    elif years["2009"][0] <= timestamp < years["2010"][0]:
        return "2009"
    elif years["2010"][0] <= timestamp < years["2011"][0]:
        return "2010"
    elif years["2011"][0] <= timestamp < years["2012"][0]:
        return "2011"
    elif years["2012"][0] <= timestamp < years["2013"][0]:
        return "2012"
    elif years["2013"][0] <= timestamp < years["2014"][0]:
        return "2013"
    elif years["2014"][0] <= timestamp:
        return "2014"
    else:
        return "Huston " + str(timestamp)

    # Load dataset


def makePlottable(yearDicts, type):
    returnableYears = {
        1996: 0,
        1997: 0,
        1998: 0,
        1999: 0,
        2000: 0,
        2001: 0,
        2002: 0,
        2003: 0,
        2004: 0,
        2005: 0,
        2006: 0,
        2007: 0,
        2008: 0,
        2009: 0,
        2010: 0,
        2011: 0,
        2012: 0,
        2013: 0,
        2014: 0,
    }
    counter = 1996
    while (counter <= 2014):
        returnableYears[counter] = yearDicts[str(counter)][type]
        counter += 1
    return returnableYears


def averageOutYears(years):
    counter = 1996
    while (counter <= 2014):
        l = list(years[str(counter)])
        try:
            l[3] = l[1] / l[2]
        except:
            l[3] = 0
        years[str(counter)] = tuple(l)
        counter += 1

    return years


folderName = 'BrokenUpData'
url = "ratings_Books.csv"
names = ['user', 'item', 'rating', 'timestamp']

directory = os.fsencode(folderName)

# Next plan: go through each line of the data,  check if its year, then add to the "years" total

years = {
    # "Year": (timestamp, total, count, average)
    "1996": (820454400, 0, 0, 0),
    "1997": (852076800, 0, 0, 0),
    "1998": (883612800, 0, 0, 0),
    "1999": (915148800, 0, 0, 0),
    "2000": (946684800, 0, 0, 0),
    "2001": (978307200, 0, 0, 0),
    "2002": (1009843200, 0, 0, 0),
    "2003": (1041379200, 0, 0, 0),
    "2004": (1072915200, 0, 0, 0),
    "2005": (1104537600, 0, 0, 0),
    "2006": (1136073600, 0, 0, 0),
    "2007": (1167609600, 0, 0, 0),
    "2008": (1199145600, 0, 0, 0),
    "2009": (1230768000, 0, 0, 0),
    "2010": (1262304000, 0, 0, 0),
    "2011": (1293840000, 0, 0, 0),
    "2012": (1325376000, 0, 0, 0),
    "2013": (1356998400, 0, 0, 0),
    "2014": (1388534400, 0, 0, 0),
}

numberOfBrokenUpDataFiles = 90
count = 1;
meanAverage = 0
shortestTimestamp = 0
longestTimestamp = 0
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".csv"):
        dataset = pandas.read_csv(folderName + "/" + filename, names=names)
        print(filename)
        print(dataset["rating"].mean())
        for index, row in dataset.iterrows():
            year = getYear(row['timestamp'])
            if "Huston" in year:
                print(getYear(row['timestamp']))
                print("HUSTON WE HAVE A PROBLEM")
                print(year)
                break;
            else:
                listOfYearData = list(years[year])
                listOfYearData[1] = listOfYearData[1] + row["rating"]
                listOfYearData[2] = listOfYearData[2] + 1
                tupledListOfYearData = tuple(listOfYearData)
                years[year] = tupledListOfYearData
                print(years[year])
                # break;
    newYears = averageOutYears(years)
    print("\n\n\n\n\n\n\n\n\n\n\n")
    print(newYears)
    plottableYears = makePlottable(newYears, 3)
    plt.scatter(range(len(plottableYears)), list(plottableYears.values()))
    plt.show()
    plottableYears = makePlottable(newYears, 2)
    plt.scatter(range(len(plottableYears)), list(plottableYears.values()))
    plt.show()
    break;
    if count == 1:
        shortestTimestamp = int(dataset['timestamp'].min())
        longestTimestamp = int(dataset['timestamp'].max())
    elif shortestTimestamp > int(dataset['timestamp'].min()) and int(dataset['timestamp'].min()) is not 0:
        shortestTimestamp = int(dataset['timestamp'].min())
    elif longestTimestamp < int(dataset['timestamp'].max()):
        longestTimestamp = int(dataset['timestamp'].max())
    if numberOfBrokenUpDataFiles >= count:
        count = count + 1
        meanAverage = meanAverage + dataset["rating"].mean()
    else:
        break;

    # p = input("want to end?")
    # if (p == "y"):
    #     break;
    # print(dataset.groupby('item').size())
    # print(dataset.describe())
else:
    print("Why is this here?")
meanAverage = meanAverage / numberOfBrokenUpDataFiles
print(meanAverage)
print(shortestTimestamp)
print(longestTimestamp)
