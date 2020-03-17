from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob


def SA():
    with open("trainingData.csv", 'r') as td:
        cl = NaiveBayesClassifier(td, format="csv")

    with open("testingData.csv", 'r') as fp:
        print("Testing data accuracy", cl.accuracy(fp))

    cl.show_informative_features(10)
    DemoInput = input("Please provide a test input: ")


    blobInput = TextBlob(DemoInput, classifier=cl)

    for s in blobInput.sentences:
        print(s)
        print(s.classify())
