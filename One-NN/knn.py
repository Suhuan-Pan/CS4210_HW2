# -------------------------------------------------------------------------
# AUTHOR: Suhuan Pan
# FILENAME: title of the source file: knn.py
# SPECIFICATION: use python to read a csv file and predict 1NN with leave one out cross validation
# FOR: CS 4210 - Assignment #2
# TIME SPENT: feeling shame to say it because i spent lots of time but can't get the correct result
# -----------------------------------------------------------*/
# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH
# AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays
#-----------------------------------------------------------*/
# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH
# AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries

import csv
from sklearn.neighbors import KNeighborsClassifier


db = []
X = []
Y = []

# reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            db.append (row)

# store data set
dataRow = []
for i in range(len(db)):
    dataRow.append([])
    for ele in db[i]:
        dataRow[i].append(ele)
# print("stored data set row by row: ", currentRow)

# split to data and class label set
data = []
class_label = []
for row in dataRow:
    c1 = row[0:2]
    c2 = row[2]
    data.append(c1)
    class_label.append(c2)

# print("After split data set and class label set: ")
# print(xx)
# print(yy)

# convert each elements in nested list into float type
fx = []
testSample = []
for row in data:
    fx = [float(ele) for ele in row]
    X.append(fx)

# convert positive to class = 1, negative to class = 2
fy = []
for j in range(len(class_label)):
    if class_label[j] == '+': fy = float (1.0)
    else: fy = float(2.0)
    Y.append(fy)

# print(X)
# print(Y)

counter = 0
lastIndex = len(X)-1
testSample_x = []
testSample_y = []


for index in range(len(X)):

    x_train = []
    #y_train = []
    test_x = []
    test_y = []

    # print("index = ", index)
    test_x.append(X[index])
    test_y.append(Y[index])
    # print(test_x, test_y)

    if index == 0:
        x_train = X[index+1:len(X)]
        y_train = Y[index+1:len(Y)]

    elif index == lastIndex:
        x_train = X[0:index]
        y_train = Y[0:index]

    else:
        a = index+1
        d = index-1

        if d == 0:
            # print("----- should be index 1 -----")
            x_train = X[a:len(X)]
            x_train.append(X[0])
            y_train = Y[a:len(Y)]
            y_train.append(Y[0])

        elif a == lastIndex:
            # print("----- should be index 8 -----")
            x_train = X[0:index]
            x_train.append(X[lastIndex])
            y_train = Y[0:index]
            y_train.append(Y[lastIndex])

        else:
           # print("a, b, c, d", a, lastIndex, 0, d)
            x_train = X[a:len(X)]
            x2 = X[0:d+1]
            for row in x2:
                x_train.append(row)
            # print("x train: ", x_train)
            # print("y train: ", y_train)


    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf.fit(x_train, y_train)

    class_predict = clf.predict(test_x)
    # print("predict label, true label:", class_predict, test_y)
    for ele in class_predict:
        if ele != test_y:
            counter = counter + 1
            # print("unmatch: ", counter)



print("Error rate: ", counter / len(Y))

#print("train y: ", y_train)

    # cnn = KNeighborsClassifier(n_neighbors=1, p=2)
    # cnn = cnn.fit(x_train, y_train)







































