import tweepy
from pullTweets import pullTweets
from keywordExtraction import keywordExtraction

consumer_key = "6MhbZH5MI4Uxrl61LeSFhymkF"
consumer_secret = "SVDcGLkrA8NCHIKH7bN5F8ZCxNUyxVE5zXQMSFMdjW9kKgSlWD"
access_token = "3011525667-NPo9lLm3fFilJjyUYO6Xr5KiL5QDoZxV5daLTTq"
access_token_secret = "8t91piYB8hXXvCwSmAT7FMdY9pPoOxRy6LFkAsDa1sK50"

if __name__ == "__main__":
    #pullTweets()
    keywordExtraction()

print("End")
