# Load libraries
import pandas
import os
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "ratings_Books.csv"
names = ['user', 'item', 'rating', 'timestamp']

directory = os.fsencode('BrokenUpData')

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".csv"): 
        #dataset = pandas.read_csv(filename, names=names)
        print(filename)
        #print(dataset.describe())
        input("is this right?")
    else:
        print("WHy is this here?")


#dataset = pandas.read_csv(url, names=names)

#print(dataset.head(20))
#print(dataset.describe())
#print(dataset.groupby('item').size())