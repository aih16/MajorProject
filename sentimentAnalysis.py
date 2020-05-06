from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from rake_nltk import Rake


def SA():
    r = Rake()
    # Opens file and reads in training data
    # NB classifier trains using the read in data
    with open("trainingData.csv", 'r') as trainingdata:
        classifier = NaiveBayesClassifier(trainingdata, format="csv")
        print("Training Data")
        classifier.show_informative_features(30)

    # Opens file and reads in testing data
    # Prints testing data accuracy
    # Not needed for final product
    """
    with open("testingData.csv", 'r') as testingdata:
        print("Testing data accuracy", classifier.accuracy(testingdata))
    """

    # Asks for user input
    userInput = input("Please provide a test input: ")

    # Defines stopwords
    stop_words = set(stopwords.words('english'))

    # Takes user input, removes stopwords
    word_tokens = word_tokenize(userInput)

    # Creates list size based on number of words left after stop words are removed
    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    # Initialize empty list
    filtered_sentence = []

    # Appends each word to end of list
    # Runs for as many words are stored in word_tokens
    for w in word_tokens:
        # If word is not in stop_words, append to end of list
        if w not in stop_words:
            filtered_sentence.append(w)

    # Prints list to see new sentence with stopwords removed
    print("Stopwords removed", filtered_sentence)

    # Extract keywords from remaining text
    r.extract_keywords_from_sentences(filtered_sentence)

    # Rank the extracted keywords
    ranked_phrases = r.get_ranked_phrases_with_scores()

    # Print extracted keywords
    print("Ranked Phrases", ranked_phrases)

    # Converts extracted keywords list to string
    listToStr = ' '.join([str(elem) for elem in ranked_phrases])

    # Runs string through trained NB classifier
    finalString = TextBlob(listToStr, classifier=classifier)

    # Print string followed by classification
    print("String followed by classification: ", finalString, finalString.classify())
