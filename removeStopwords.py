from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def removeStopWords():

    with open("trainingData.csv", 'r') as testingdata:
        sentence = testingdata.read()

        stop_words = set(stopwords.words('english'))

        word_tokens = word_tokenize(sentence)

        filtered_sentence = [w for w in word_tokens if not w in stop_words]

        filtered_sentence = []

        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)
                appendFile = open('filteredtext.csv', 'a')
                appendFile.write(" " + w)

        print(filtered_sentence)
