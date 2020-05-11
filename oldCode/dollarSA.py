from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from rake_nltk import Rake
import re


# Dollar SA is a small change to the normal Sentiment Analyizer that allowed me to analyize the sentiment of all the
# dollar index data which helped avoid having to do it all manually The accuracy of the SA is 75% which means that
# roughly 63 of the given tweets will be incorrectly analyized however this is taken into account in my final
# evaluation along with the fact that the sentiment is the average of all his tweets in a given day and not
# single tweets by themselves

def dollarSA():
    r = Rake()
    # Opens file and reads in training data
    # NB classifier trains using the read in data
    with open("../datasets/trainingData.csv", 'r') as trainingdata:
        classifier = NaiveBayesClassifier(trainingdata, format="csv")
        print("Training Data")
        classifier.show_informative_features(5)

    # Opens file and reads in testing data
    # Prints testing data accuracy
    # Not needed for final product

    with open("../datasets/testingData.csv", 'r') as testingdata:
        print("Testing data accuracy", classifier.accuracy(testingdata))


    with open("dollar.txt", 'r', encoding='utf-8') as a_file:
        for line in a_file:
            userInput = line.strip()

            regex = re.compile('[^a-zA-Z ]')
            punctuationRemoved = regex.sub('', userInput)

            # Defines stopwords
            stop_words = set(stopwords.words('english'))

            # Takes user input, removes stopwords
            word_tokens = word_tokenize(punctuationRemoved)

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

            # Converts the filtered stop word sentence to string
            stringWithoutStopwords = ' '.join([str(elem) for elem in filtered_sentence])

            # Extracts keywords from the filtered sentence
            r.extract_keywords_from_text(stringWithoutStopwords)

            # Ranks the keywords that have been extracted
            ranked_phrases = r.get_ranked_phrases()

            # Converts extracted keywords list to string
            listToStr = ' '.join([str(elem) for elem in ranked_phrases])

            # Runs string through trained NB classifier
            finalString = TextBlob(listToStr, classifier=classifier)

            # Print string followed by classification
            print(finalString + "," + finalString.classify())
