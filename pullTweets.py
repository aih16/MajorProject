import tweepy
consumer_key = "6MhbZH5MI4Uxrl61LeSFhymkF"
consumer_secret = "SVDcGLkrA8NCHIKH7bN5F8ZCxNUyxVE5zXQMSFMdjW9kKgSlWD"
access_token = "3011525667-NPo9lLm3fFilJjyUYO6Xr5KiL5QDoZxV5daLTTq"
access_token_secret = "8t91piYB8hXXvCwSmAT7FMdY9pPoOxRy6LFkAsDa1sK50"


def pullTweets():
    # Creating the authentication object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Setting access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # Creating the API object and passing in auth information
    api = tweepy.API(auth)


    name = "realDonaldTrump"
    # Number of tweets to pull
    tweetCount = 4
    # Using the API object to get tweets from timeline
    myTimeline_tweets = api.user_timeline(id=name, count=tweetCount)

    # foreach through all tweets pulled
    for tweet in myTimeline_tweets:
        # pulls tweets ignoring retweets
        if 'RT @' not in myTimeline_tweets:
            # printing the text stored inside the tweet object
            print("Time of Tweet:")
            print(tweet.created_at)

            print("Twitter handle and place:")
            print(tweet.user.screen_name, tweet.user.location)

            print(tweet.text)
            print("")

            outF = open("pulledTweets.txt", "w")
            # write line to output file
            outF.write(tweet.text + "\n")
            outF.close()
