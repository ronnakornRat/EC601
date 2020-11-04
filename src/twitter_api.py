import tweepy #https://github.com/tweepy/tweepy
import json

with open('key/twitter_key.json') as f:
  data = json.load(f)

#Twitter API credentials
consumer_key = data["API key"]
consumer_secret = data["API key secret"]
access_key = data["Access token"]
access_secret = data["Access token secret"]

# return the tweets 
def get_tweets(search_words):
    max_item = 100
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    search_words =  search_words + " -filter:retweets"
    # print("twitter api searching for: ", search_words, flush=True)

    # Collect tweets
    tweets = tweepy.Cursor(api.search,
                q=search_words,
                lang="en",
                ).items(max_item)

    # Iterate and print tweets
    # for tweet in tweets:
    #     print(index, ": ", "=" * 20)
    #     print(tweet.user.screen_name, tweet.user.location)
    #     print((tweet.text).encode("utf-8"))
    #     index = index + 1
    return tweets

# return top trends keywords
def top_hashtags(woeid):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # data = api.trends_available()

    # get trends according to woeid
    data = api.trends_place(woeid)
    tags = data[0]
    trends = tags["trends"]
    with open('main.json', 'w') as outfile:
        json.dump(data, outfile)

    retval = []
    for tag in trends:
        retval.append(tag['name'])
    return retval

if __name__ == '__main__':
    # Boston, USA woeid
    # top_hashtags(2367105)
    search_words = "#Boston"
    tweets = get_tweets(search_words)
    for tweet in tweets:
        print((tweet.text).encode("utf-8"))
        print("\n")
    