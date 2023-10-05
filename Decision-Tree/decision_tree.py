# -------------------------------------------------------------------------
# AUTHOR: Suhuan Pan
# FILENAME: title of the source file: decision_tree.py
# SPECIFICATION: use python to read a csv file and plot a decision tree
# FOR: CS 4210 - Assignment #2
# TIME SPENT: 4 hours
# -----------------------------------------------------------*/
# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH
# AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

# importing 2 Python libraries
from sklearn import tree
import csv

# three csv files as training sets
dataSets = ['contact_lens_training_1.csv',
            'contact_lens_training_2.csv',
            'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

# reading all three training data in the csv files
# append in dbTraining set row by row
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:  # skipping the header
                dbTraining.append (row)
                # print(dbTraining([2]))

    # transform the original categorical training features
    # to numerical values as a dictionary
    numericalFeatures = {0: ['Young', 'Myope', 'Yes', 'Reduced'],
                         1: ['Prepresbyopic', 'Hypermetrope', 'No', 'Normal'],
                         2: ['Presbyopic']}
    k = []
    v = []

    for i in range(len(dbTraining)):

        k.append([])
        v.append([])
        for ele in dbTraining[i]:
            for key, val in numericalFeatures.items():
                if ele in val:
                    k[i].append(key)
                    v[i].append(ele)

    # print(k)
    # print(v)

    for row in k:
        a = row[0:4]
        b = row[4]
        X.append(a)
        Y.append(b)

   # print("-------------")
    # print("Display X_train and Y_Train: ")
    # print(X)
    # print(Y)

    loopAccuracy = 0
    # loop your training and test tasks 10 times here
    for i in range (10):
    
        # fitting the decision tree to the data setting max_depth = 3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y)

        # read the test data on a csv file
        # and add this data to dbTest
        # --> add your Python code here
        dbTest = ['contact_lens_test.csv']

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

            # print(k2)
            # print(v2)

            for row2 in k2:
                a2 = row2[0:4]
                b2 = row2[4]
                X_Test.append(a2)
                Y_Test.append(b2)

            # and then use the decision tree to make the class prediction.
            # For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
            class_predicted = clf.predict(X_Test)
            final_predicted = []
            for r in class_predicted:
                final_predicted.append(r)

            # print("Display X_Test and Y_Test: ")
            # print(X_Test)
            # print("Y_Test: ", Y_Test)
            # print("true label: ", final_predicted)

            # count the frequency of matching labels

            predictRight = 0
            for index in range(len(final_predicted)):
                element = Y_Test[index]
                if element == final_predicted[index]:
                    # print("same: ", element, " ", final_predicted[index])
                    predictRight = predictRight + 1

            cur_accuracy = predictRight / len(final_predicted)
            # print("Accuracy of current sample: ", cur_accuracy)
            accuracy = accuracy + cur_accuracy

        # print("accuracy for whole dbTest: ", accuracy)
        loopAccuracy = loopAccuracy + accuracy

    # find the average of this model during the 10 runs (training and test set)
    average = loopAccuracy / 10.0
    # your output should be something like that: final accuracy when training on
    # contact_lens_training_1.csv: 0.2
    print("Final accuracy when training on", ds,
          "is: ", average)
