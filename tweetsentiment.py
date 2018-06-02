import tweepy
from textblob import TextBlob

consumer_key = 'cPXB1JjqsL5P7NZHSg5HbFNGS'
consumer_secret = '9QH8O34E8qUEAIrnPcx7RCaaJ0RhyxbxKcrNlJoznbBUKS7YHk'

access_token = '721960609-OfBTWfqmqGwNnYOMD1BfBrr7AShKdisB2o4ZeWVT'
access_token_secret = 'MsYpQftWLKFiEaOyM8Yb4yIz6EQ9H7bcuMGUFN8y5gYEp'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

csvdir = "tweetsentimentanalysis.csv"
csv = open(csvdir, "a")
isPositivemin = -0.0
columnTitleRow = "tweet, sentiment\n"
csv.write(columnTitleRow)

num = 0

for tweet in public_tweets:
    num += 1
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment.polarity)
    sentiment = "negative"
    if analysis.sentiment.polarity >= isPositivemin:
        sentiment = "positive"
    else:
        sentiment = "negative"
    row = tweet.text.replace("\n", "").replace(",", " ") + " , " + sentiment + "\n"
    csv.write(row)
print("totalcount:"+str(num))
