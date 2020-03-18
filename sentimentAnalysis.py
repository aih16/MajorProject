from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob


def SA():
    with open("trainingData.csv", 'r') as td:
        cl = NaiveBayesClassifier(td, format="csv")

    with open("testingData.csv", 'r') as fp:
        print("Testing data accuracy", cl.accuracy(fp))

    cl.show_informative_features(5)
    demoInput = input("Please provide a test input: ")
    demoInput = TextBlob(demoInput, classifier=cl)

    for s in demoInput.sentences:
        print(s)
        print(s.classify())
