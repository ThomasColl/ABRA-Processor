# Load libraries
import os

import matplotlib.pyplot as plt
import pandas.plotting

# Load dataset
folderName = 'BrokenUpData'
url = "ratings_Books.csv"
names = ['user', 'item', 'rating', 'timestamp']

directory = os.fsencode(folderName)

years = {
    "1996": 820454400,
    "1997": 852076800,
    "1998": 883612800,
    "1999": 915148800,
    "2000": 946684800,
    "2001": 978307200,
    "2002": 1009843200,
    "2003": 1041379200,
    "2004": 1072915200,
    "2005": 1104537600,
    "2006": 1136073600,
    "2007": 1167609600,
    "2008": 1199145600,
    "2009": 1230768000,
    "2010": 1262304000,
    "2011": 1293840000,
    "2012": 1325376000,
    "2013": 1356998400,
    "2014": 1388534400,
}
numberOfBrokenUpDataFiles = 88
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
        # dataset.plot(kind='scatter', x='timestamp', y='rating')
        # dataset.plot(x='timestamp', y='rating')
        plt.show()
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
        print("WHy is this here?")
meanAverage = meanAverage / numberOfBrokenUpDataFiles
print(meanAverage)
print(shortestTimestamp)
print(longestTimestamp)
