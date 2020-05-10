from sklearn.feature_extraction.text import CountVectorizer
from numpy import asarray
from numpy import savetxt



def CountVector():

    # Uses CountVectorizer

    with open("dollarIndexTweets.txt", 'r', encoding='utf-8') as vectorData:
        # create the transform
        vectorizer = CountVectorizer()

        # corpus = vectorData

        corpus = ['This is the first document.',
                  'This is the second second document.',
                  'And the third one.',
                  'Is this the first document?', ]

        # tokenize and build vocab
        vector = vectorizer.fit_transform(corpus)

        # summarize encoded vector
        print(vector.shape)
        print(vectorizer.get_feature_names())

        vectorArray = vector.toarray()
        print(vectorArray)

        data = asarray(vectorArray)
        savetxt('extractedFeatures.csv', data, delimiter=',')

    # Uses TF-IDF
    """
    with open("dollarIndexTweets.txt", 'r', encoding='utf-8') as vectorData:

        # corpus = vectorData

        corpus = ['This is the first document.',
                  'This is the second second document.',
                  'And the third one.',
                  'Is this the first document?', ]

        # create the transform
        vectorizer = TfidfVectorizer()

        # tokenize and build vocab
        vectorizer.fit(corpus)

        # summarize
        print('vocabulary: ', vectorizer.vocabulary_)
        print('idfs: ', vectorizer.idf_)

        # encode document
        vector = vectorizer.transform([corpus[0]])

        # summarize encoded vector
        print('vectors: ', vector.toarray())
    """

    # Prints each separate records to a line
    """
    with open("dollarIndexTweets.txt", 'r', encoding='utf-8') as vectorData:
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
    """