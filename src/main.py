import google_api
import twitter_api
import json
import re
# import pandas as pd

import matplotlib.pyplot as plt
from statistics import mean

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
    # limit number of tags
    max_tag = 5

    # Boston, USA woeid
    tag_list = twitter_api.top_hashtags(2367105)

    # check the list of tags in main.json
    with open('main.json', 'w') as outfile:
        json.dump(tag_list, outfile)


    for index, tag in enumerate(tag_list):
        if (index == max_tag):
            break

        print("\n",index + 1 , ". tag:", tag, flush=True)
        tweets = twitter_api.get_tweets(tag)

        score_list = []
        for tweet in tweets:
            text = remove_url(tweet.text)
            # print("text: ", text, flush = True)
            try:
                score = google_api.analyze_text_sentiment(text)
                score_list.append(score)
            except Exception as e: 
                print("google api: error processing text")
                print("\"" + text + "\"", flush = True)
            

        # plot the sentiment score in histrogram
        fig, ax = plt.subplots()

        n, bins, patches = plt.hist(score_list, bins=[-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0 ])
        plt.xticks(bins, rotation=80)
        plt.title(tag)
        fig.tight_layout()
        # save the plot in figure folder
        plt.savefig("figure/" + tag + ".png")
        plt.clf()
        # print out the sentiment score
        print("mean sentiment: ", mean(score_list), flush=True)
        
    
