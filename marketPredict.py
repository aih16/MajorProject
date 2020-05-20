import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle


def GNB():

    runTimes = int(input("Number of test runs: "))
    testSize = int(input("Test size: "))

    print("Running Gaussian Naive Bayes")
    totalAccuracy = 0
    for x in range(runTimes):
        # reads in the data set as a pandas data frame
        df = pd.read_csv('datasets/FSMC.csv')
        # defines the x and y from the data set
        x = df.drop('marketChange', axis=1)
        y = df['marketChange']
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=testSize)

        # trains the GaussianNB model
        model = GaussianNB()
        model.fit(x_train, y_train)

        # predicts the y outcome using the test data
        y_pred = model.predict(x_test)
        print(y_pred)

        # gives accuracy of prediction
        accuracy = accuracy_score(y_test, y_pred) * 100
        print(accuracy)
        totalAccuracy = totalAccuracy + accuracy

    # provides mean accuracy after x amount of runs
    meanAccuracy = totalAccuracy/runTimes
    print("Average Accuracy after", runTimes, "tests: ", meanAccuracy)

    """
    s = pickle.dumps(model)
    model2 = pickle.loads(s)
    userInput = input("Please provide a negative or positive sentiment: ")
    print(model2.predict(x_train[0:1]))
    """


def MNB():

    runTimes = int(input("Number of test runs: "))
    testSize = int(input("Test size: "))

    print("Running Multinomial Naive Bayes")
    totalAccuracy = 0
    for x in range(runTimes):
        df = pd.read_csv('datasets/FSMC.csv')
        x = df.drop('marketChange', axis=1)
        y = df['marketChange']
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=testSize)

        model = MultinomialNB()
        model.fit(x_train, y_train)

        y_pred = model.predict(x_test)
        print(y_pred)

        accuracy = accuracy_score(y_test, y_pred) * 100
        print(accuracy)
        totalAccuracy = totalAccuracy + accuracy

    meanAccuracy = totalAccuracy / runTimes
    print("Average Accuracy after", runTimes, "tests: ", meanAccuracy)


def LogiR():

    runTimes = int(input("Number of test runs: "))
    testSize = int(input("Test size: "))

    print("Running LogiR")
    totalAccuracy = 0
    for x in range(runTimes):
        df = pd.read_csv('datasets/FSMC.csv')
        x = df.drop('marketChange', axis=1)
        y = df['marketChange']
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=testSize)

        # instantiate the model (using the default parameters)
        logreg = LogisticRegression()

        # fit the model with data
        logreg.fit(x_train, y_train)

        y_pred = logreg.predict(x_test)

        cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
        print(cnf_matrix)

        accuracy = accuracy_score(y_test, y_pred) * 100
        print(accuracy)
        totalAccuracy = totalAccuracy + accuracy

    meanAccuracy = totalAccuracy / runTimes
    print("Average Accuracy after", runTimes, "tests: ", meanAccuracy)

    # Testing some matplotlib functions
    # provides a confusion matrix for the logistic regression
    class_names = [0, 1]
    fig, ax = plt.subplots()
    tick_marks = np.arange(len(class_names))
    plt.xticks(tick_marks, class_names)
    plt.yticks(tick_marks, class_names)

    # creates heatmap
    sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu", fmt='g')
    ax.xaxis.set_label_position("top")
    plt.tight_layout()

    # titles and labels confusion matrix
    plt.title('Confusion matrix', y=1.1)
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')
    plt.show()
