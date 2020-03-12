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

    # Which twitter handle to pull from
    name = "realDonaldTrump"
    # Number of tweets to pull
    tweetCount = 100
    # Pulls the extended tweet

    # Using the API object to get tweets from timeline
    # include_rts=False to remove all retweets, including Trump retweeting himself
    myTimeline_tweets = api.user_timeline(id=name, count=tweetCount, tweet_mode='extended', include_rts=False)

    # foreach through all tweets pulled
    for tweet in myTimeline_tweets:
        # pulls tweets ignoring retweets
        if 'RT @' not in myTimeline_tweets:
            # printing the text stored inside the tweet object
            print("Time of Tweet:")
            print(tweet.created_at)

            print("Twitter handle and place:")
            print(tweet.user.screen_name, tweet.user.location)

            print(tweet.full_text)
            print("")

            outF = open("pulledTweets.txt", "w", encoding="utf8")
            # write line to output file
            outF.write(tweet.full_text + "\n")
            outF.close()
