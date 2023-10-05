# -------------------------------------------------------------------------
# AUTHOR: Suhuan Pan
# FILENAME: title of the source file: knn.py
# SPECIFICATION: use python to read a csv file and plot a decision tree
# FOR: CS 4210 - Assignment #2
# TIME SPENT: 2 hours
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
currentRow = []
for i in range(len(db)):
    currentRow.append([])
    for ele in db[i]:
        currentRow[i].append(ele)

# print("stored data set row by row: ", currentRow)

# split to data and class label set
xx = []
yy = []
for row in currentRow:
    data = row[0:2]
    class_label = row[2]
    xx.append(data)
    yy.append(class_label)

# print("After split data set and class label set: ")
# print(xx)
# print(yy)

# convert each elements in nested list into float type
# also store the test sample of this iteration in the vector testSample
fx = []
testSample = []
for row in xx:
    fx = [float(ele) for ele in row]
    X.append(fx)
    testSample.append(fx)

# convert positive to class = 1, negative to class = 2
fy = []
for j in range(len(yy)):
    if yy[j] == '+': fy = float (2.0)
    else: fy = float(1.0)
    Y.append(fy)

print("After transfer all data to numerical value: ")
print(X)
print(Y)
print(testSample)


# fitting the knn with the training data
clf = KNeighborsClassifier(n_neighbors=1, p=2)
clf.fit(testSample, Y)

# use your test sample in this iteration to make the class prediction. For instance:
# class_predicted = clf.predict([[1, 2]])[0]s
# convert to list of float numbers
final_predict = []
predict = clf.predict(testSample)
for r in predict:
    final_predict.append(r)

# print("predicted class label: ", final_predict)
