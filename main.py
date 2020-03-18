from pullTweets import pullTweets
from keywordExtraction import keywordExtraction
from sentimentAnalysis import SA

if __name__ == "__main__":
    pullTweets()
    keywordExtraction()
    SA()

print("End")
