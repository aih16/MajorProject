import nltk
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer


def lemmatize_sentence(tokens):
    """
    Substitute the positive_tweets.json with a list of Trumps most negative tweets e.g.
    negative_tweets = [
        "Negative",
        "Negative",
        "Negative"
    ]
    """

    positive_tweets = twitter_samples.strings('positive_tweets.json')
    negative_tweets = twitter_samples.strings('negative_tweets.json')
    text = twitter_samples.strings('tweets.20150430-223406.json')

    tweet_tokens = twitter_samples.tokenized('positive_tweets.json')

    # print(pos_tag(positive_tweet_tokens[0]))

    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = []
    for word, tag in pos_tag(tokens):
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        lemmatized_sentence.append(lemmatizer.lemmatize(word, pos))
    print(lemmatize_sentence(tweet_tokens[0]))

    return lemmatized_sentence
