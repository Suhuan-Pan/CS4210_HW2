#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
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
db = []


with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:
            db.append(row)
            print(row)


numericalFeatures = {0:['Sunny', 'Hot', 'High', 'Weak', 'Yes'],
                    1:['Overcast', 'Mild', 'Normal', 'Strong', 'No'],
                    2:['Rain', 'Cool']}

k = []
v = []

for i in range(len(db)):
    # append empty sublist inside the list to created matrix
    k.append([])
    v.append([])
    for ele in db[i]:
        for key, val in numericalFeatures.items():
             if ele in val:
                 k[i].append(key)
                 v[i].append(ele)

X = []
Y = []

for row in k:
    a = row[4]
    b = row[4]
    X.append(a)
    Y.append(b)

print(X)
print(Y)

#transform the original training features to numbers and add them to the 4D array
# X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2,
# 2], ...]]
#--> add your Python code here



#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here



#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)
print(clf)

#reading the test data in a csv file
Data_Test = []
#--> add your Python code here
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:
            Data_Test.append(row)

y_predict = []
for row in Data_Test:
    a = clf.predict_proba(row)
    y_predict.append(a)


print(y_predict)

#printing the header os the solution
#--> add your Python code here
#use your test samples to make probabilistic predictions. For instance:
# clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here