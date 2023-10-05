#-------------------------------------------------------------------------
# AUTHOR: Suhuan Pan
# FILENAME: naive_bayes.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: 4 hours
#-----------------------------------------------------------*/
#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH
# AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
import csv

#reading the training data in a csv file
#--> add your Python code here
trainingData = []
Header = []
X = []
Y = []

with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:
            trainingData.append(row)
        else:
            Header.append(row)


# convert to numerical values
numericalFeatures = {0:['Sunny', 'Hot', 'High', 'Weak', 'Yes'],
                    1:['Overcast', 'Mild', 'Normal', 'Strong', 'No'],
                    2:['Rain', 'Cool']}

k = []
v = []

for i in range(len(trainingData)):
    # append empty sublist inside the list to created matrix
    k.append([])
    v.append([])
    for ele in trainingData[i]:
        for key, val in numericalFeatures.items():
             if ele in val:
                 k[i].append(key)
                 v[i].append(ele)

for row in k:
    a = row[0:4]
    b = row[4]
    X.append(a)
    Y.append(b)

# print(X)
# print(Y)


#fitting the naive bayes to the data
clf = GaussianNB()
clf = clf.fit(X, Y)

#reading the test data in a csv file
dbTest = ['weather_test.csv']

accuracy = 0.0
for data in dbTest:

    dbTesting = []
    X_Test = []
    Y_Test = []

    with open(data, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:  # skipping the header
                dbTesting.append(row)

    # transform the features of the test instances to numbers following the
    # same strategy done during training,
    k2 = []
    v2 = []

    for i in range(len(dbTesting)):
        k2.append([])
        v2.append([])
        for ele in dbTesting[i]:
            for key, val in numericalFeatures.items():
                if ele in val:
                    k2[i].append(key)
                    v2[i].append(ele)

    for row2 in k2:
        X_Test.append(row2)

    # print("X_Test: ", X_Test)

    predictSet = []
    class_predict = clf.predict_proba(X_Test)
    for r in class_predict:
        predictSet.append(r)


    Header.append("Confidence")
    print(Header)


    f = []
    index = 0
    for r in predictSet:
        # print(r)
        f = [float(ele) for ele in r]
        class0 = f[0]
        class1 = f[1]
        words = []
        if class0 > 0.75 or class0 == 0.75:
            for l in dbTesting[index]:
                if l != '?':
                    words.append(l)
            print(words, "Yes", class0)
        if class1 > 0.75 or class1 == 0.75:
            for l in dbTesting[index]:
                if l != '?':
                    words.append(l)
            print(words, "No", class1)
        index = index + 1





