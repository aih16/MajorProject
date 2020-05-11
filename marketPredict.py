import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import pickle


def marketPredict():

    # Pass the Sentiment Classification (0 = negative, 1 = positive)
    # Use the trained model to guess whether the market will go up or down
    totalAccuracy = 0
    runTimes = 50
    for x in range(runTimes):
        df = pd.read_csv('datasets/FSMC.csv')
        x = df.drop('marketChange', axis=1)
        y = df['marketChange']
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

        model = GaussianNB()
        model.fit(x_train, y_train)

        y_pred = model.predict(x_test)
        print(y_pred)

        accuracy = accuracy_score(y_test, y_pred) * 100
        print(accuracy)
        totalAccuracy = totalAccuracy + accuracy

    meanAccuracy = totalAccuracy/runTimes
    print("Average Accuracy after", runTimes, "tests: ", meanAccuracy)

    """
    s = pickle.dumps(model)
    model2 = pickle.loads(s)
    userInput = input("Please provide a negative or positive sentiment: ")
    print(model2.predict(x_train[0:1]))
    """

