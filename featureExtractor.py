from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from numpy import asarray
from numpy import savetxt


def CountVector():

    # Uses CountVectorizer for extracting features
    with open("datasets/dollarIndexTweets.txt", 'r', encoding='utf-8') as vectorData:

        userInput = int(input("Select max amount of features to extract: "))

        # create the transform
        vectorizer = CountVectorizer(max_features=userInput)

        corpus = vectorData

        # tokenize and builds vocab
        vector = vectorizer.fit_transform(corpus)

        # summarize encoded vector
        print(vector.shape)
        print(vectorizer.get_feature_names())

        # creates array from extracted features
        vectorArray = vector.toarray()
        print(vectorArray)

        # saves the array of features
        data = asarray(vectorArray)
        savetxt('datasets/extractedFeatures.csv', data, delimiter=',')


def TFIDF():

    # Uses TF-IDF for extracting features
    with open("datasets/dollarIndexTweets.txt", 'r', encoding='utf-8') as vectorData:

        userInput = int(input("Select max amount of features to extract: "))

        corpus = vectorData

        # create the transform
        vectorizer = TfidfVectorizer(max_features=userInput)

        # tokenize and build vocab
        vectorizer.fit(corpus)

        # summarize
        print('vocabulary: ', vectorizer.vocabulary_)
        print('idfs: ', vectorizer.idf_)

        # encode document
        vector = vectorizer.transform([corpus[0]])

        # summarize encoded vector
        print('vectors: ', vector.toarray())


def CountVectorLine():

    # Prints each separate records to a line for extracting features
    with open("datasets/dollarIndexTweets.txt", 'r', encoding='utf-8') as vectorData:
        for line in vectorData:
            input = line.strip()

            corpus = [input]

            # create the transform
            vectorizer = CountVectorizer()
            # tokenize and build vocab
            vectorizer.fit(corpus)

            # encode document
            vector = vectorizer.transform(corpus)

            # summarize encoded vector
            print(vector.toarray())

            features_left = [vector.toarray()]
            print(features_left)
