# Load libraries
import os

import matplotlib.pyplot as plt
import pandas.plotting

# Load dataset
folderName = 'BrokenUpData'
url = "ratings_Books.csv"
names = ['user', 'item', 'rating', 'timestamp']

directory = os.fsencode(folderName)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".csv"):
        dataset = pandas.read_csv(folderName + "/" + filename, names=names)
        print(filename)
        # dataset.plot(kind='scatter', x='timestamp', y='rating')
        dataset.plot(x='timestamp', y='rating')
        plt.show()
        p = input("want to end?")
        if (p == "y"):
            break;
        # print(dataset.groupby('item').size())
        # print(dataset.describe())
    else:
        print("WHy is this here?")
