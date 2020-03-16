from textblob import TextBlob
from textblob import classifiers

# POS = Part-of-speech, NN = Noun, DT = Determiner etc
def SA():
    trainingData = [
        ('Tom Holland is a terrible spiderman.', 'pos'),
        ('a terrible Javert (Russell Crowe) ruined Les Miserables for me...', 'pos'),
        ('The Dark Knight Rises is the greatest superhero movie ever!', 'neg'),
        ('Fantastic Four should have never been made.', 'pos'),
        ('Wes Anderson is my favorite director!', 'neg'),
        ('Captain America 2 is pretty awesome.', 'neg'),
        ('Let\s pretend "Batman and Robin" never happened..', 'pos'),
    ]
    testingData = [
        ('Superman was never an interesting character.', 'pos'),
        ('Fantastic Mr Fox is an awesome film!', 'neg'),
        ('Dragonball Evolution is simply terrible!!', 'pos')
    ]

    classifier = classifiers.NaiveBayesClassifier(trainingData)

    print(classifier.accuracy(testingData))
    classifier.show_informative_features(10)

    blob = TextBlob('the weather is terrible!', classifier=classifier)
    print(blob.classify())

    """if trainingData.sentiment.polarity > 0:
        print("Data sentiment is positive with a sentiment polarity of", trainingData.sentiment.polarity)
    elif trainingData.sentiment.polarity < 0:
        print("Data sentiment is negative with a sentiment polarity of", trainingData.sentiment.polarity)
    else:
        print("Data sentiment is neutral with a sentiment polarity of", trainingData.sentiment.polarity)

    for np in trainingData.noun_phrases:
            print(np)

        for words, tag in trainingData.tags:
            print(words, tag)

        print(trainingData.sentences[1].words[1])
        print(trainingData.sentences[1].words[1].singularize())

        for ngram in trainingData.ngrams(2):
            print(ngram)"""