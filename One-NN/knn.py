
#-----------------------------------------------------------*/
# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH
# AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries

import csv
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


db = []

# reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            db.append (row)
            # print(row)


currentRow = []
# loop your data to allow each instance to be your test set
for i in range(len(db)):
    currentRow.append([])
    for ele in db[i]:
        currentRow[i].append(ele)


X = []
Y = []

x_test = []
y_test = []

for row in currentRow:
    data = row[0:2]
    class_label = row[2]

    x_test.append(data)
    y_test.append(class_label)


f = []
sample = []
for row in x_test:
    f = [float(ele) for ele in row]
    sample.append(f)


print(sample)
print(y_test)


clf = KNeighborsClassifier(n_neighbors=1, p=2)
clf = clf.fit(sample, y_test)

y_predict = clf.predict(sample)
N = 0;
for i in range (len(y_predict)):
    for ele in y_test:
        if ele != y_predict[i]:
            N = N + 1


print (N)






# add the training features to the 2D array X removing the instance that will be
# used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]].
# Convert each feature value to
# float to avoid warning messages
# --> add your Python code here


# transform the original training classes to numbers and add to the vector Y
# removing the instance that will be used for testing in this iteration. For
# instance, Y = [1, 2, ,...]. Convert each
# feature value to float to avoid warning messages
# --> add your Python code here
# Y =

# store the test sample of this iteration in the vector testSample
# --> add your Python code here
# testSample = KNearestNeighbors

# fitting the knn to the data
# clf = KNeighborsClassifier(n_neighbors=1, p=2)
# clf = clf.fit(X, Y)

# use your test sample in this iteration to make the class prediction. For instance:
# class_predicted = clf.predict([[1, 2]])[0]
# --> add your Python code here
# compare the prediction with the true label of the test instance
# to start calculating the error rate.
# --> add your Python code here
# print the error rate
# --> add your Python code here
# --> add your Python code here