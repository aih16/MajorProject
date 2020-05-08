from sklearn import preprocessing
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


def marketPredict():

    from sentimentAnalysis import binaryClassify

    df = pd.read_csv('dollarIndexText.csv')
    x = df.drop('marketChange', axis=1)
    y = df['marketChange']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

    model = GaussianNB()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    print(y_pred)

    print(binaryClassify)

    accuracy = accuracy_score(y_test, y_pred)*100
    print(accuracy)
