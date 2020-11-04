import pytest
import os.path
import json

from pytest import approx
from src.google_api import analyze_text_sentiment
from src.twitter_api import top_hashtags, get_tweets

### list of testing
# test twitter key exist
# test google key exist
# test twitter top_hashtags
# test twitter get_tweets
# test google analyze_text_sentiment

def test_key_exist():
    assert os.path.isfile('key/twitter_key.json')
    assert os.path.isfile('key/google_nlp_key.json')

def test_twitter_key_format():
    with open('key/twitter_key.json') as f:
        data = json.load(f)
    
    assert "API key" in data
    assert "API key secret" in data
    assert "Access token" in data
    assert "Access token secret" in data

def test_google_key_format():
    with open('key/google_nlp_key.json') as f:
        data = json.load(f)
    
    assert "type" in data
    assert "project_id" in data
    assert "private_key_id" in data
    assert "private_key" in data
    assert "client_email" in data
    assert "client_id" in data
    assert "auth_uri" in data
    assert "token_uri" in data
    assert "auth_provider_x509_cert_url" in data
    assert "client_x509_cert_url" in data

def test_get_top_hashtag():
    # check it's not 0 return
    assert len(top_hashtags(2367105)) != 0

# test twitter get_tweets
def test_get_tweets():
    search_words = "#Boston"
    tweets = get_tweets(search_words)
    for tweet in tweets:
        # do something
        assert type(tweet.text) == type("string")

def test_google_analyze():
    score = analyze_text_sentiment("Here's to the crazy ones. The misfits. The rebels. The troublemakers. The round pegs in the square holes. The ones who see things differently. They're not fond of rules. And they have no respect for the status quo. You can quote them, disagree with them, glorify or vilify them. About the only thing you can't do is ignore them. Because they change things. They push the human race forward. And while some may see them as the crazy ones, we see genius. Because the people who are crazy enough to think they can change the world, are the ones who do.")    
    assert score == approx(-0.1)

def test_everything():
    pass