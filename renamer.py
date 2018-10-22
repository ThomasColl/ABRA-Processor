import os

folderName = 'BrokenUpData'
url = "ratings_Books.csv"
names = ['user', 'item', 'rating', 'timestamp']

directory = os.fsencode(folderName)
count = 1
end = 88
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    # if filename.endswith(".csv"):
    # print(folderName + "/" + str(filename))
    os.rename(folderName + "/" + filename, folderName + "/" + str(count) + ".csv")
    count += 1
