import google_api
import twitter_api
import json
import re

def get_restaurant(search_words):
    results = google_api.find_place(search_words)

    i = 0
    for place in results["results"]:
        string = place["name"] + " " + search_words
        print("search for: ", string)
        tweets = twitter_api.get_tweets(place["name"])

        print("sending tweets to Google NLP API")
        for tweet in tweets:
            print(remove_url(tweet.text))
            google_api.analyze_text_sentiment(remove_url(tweet.text))


        i = i +1
        if (i ==10):
            break
        

    #write tweet objects to JSON
    # with open('main.json', 'w') as outfile:
    #     json.dump(tweets, outfile)

    # print("sending tweets to Google NLP API")
    # for tweet in tweets:
    #     print(remove_url(tweet.text))
    #     google_api.analyze_text_sentiment(remove_url(tweet.text))


# credits: https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/calculate-tweet-word-frequencies-in-python/
def remove_url(txt):
    """Replace URLs found in a text string with nothing 
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """

    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

if __name__ == '__main__':
    # get_restaurant("Boston")
    tag_list = twitter_api.top_hashtags(2367105)
    with open('main.json', 'w') as outfile:
        json.dump(tag_list, outfile)
    for index, tag in enumerate(tag_list):
        print("\n",index + 1, ". tag: ", tag, flush=True)
        tweets = twitter_api.get_tweets(tag)
        # index = 1
        mean_score = 0
        for tweet in tweets:
            # print(index, ": ", "=" * 20)
            # print(tweet.user.screen_name, tweet.user.location)
            # print(remove_url(tweet.text).encode("utf-8"))
            

            mean_score = google_api.analyze_text_sentiment(remove_url(tweet.text))
            # index = index + 1
        print("mean sentiment: ", mean_score/(index + 1), flush=True)
        if (index == 5):
            break
