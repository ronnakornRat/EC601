# credits https://codelabs.developers.google.com/codelabs/cloud-natural-language-python3/index.html

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key/google_nlp_key.json"

from google.cloud import language
from google.cloud.language import enums, types

# import googlemaps 
import json

# analyze the sentiment
def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    # initialize the Document
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT) # this one is plain text, choice = PLAIN_TEXT, HTML

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = [
        ('text', text),
        ('score', sentiment.score),
        ('magnitude', sentiment.magnitude),
    ]
    # for k, v in results:
    #     print('{:10}: {}'.format(k, v))

    return sentiment.score

def analyze_text_entities(text):
    client = language.LanguageServiceClient()
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document)

    for entity in response.entities:
        print('=' * 79)
        results = [
            ('name', entity.name),
            ('type', enums.Entity.Type(entity.type).name),
            ('salience', entity.salience),
            ('wikipedia_url', entity.metadata.get('wikipedia_url', '-')),
            ('mid', entity.metadata.get('mid', '-')),
        ]
        for k, v in results:
            print('{:15}: {}'.format(k, v))

def classify_text(text):
    client = language.LanguageServiceClient()
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    response = client.classify_text(document=document)

    for category in response.categories:
        print('=' * 79)
        print('category  : {}'.format(category.name))
        print('confidence: {:.0%}'.format(category.confidence))

### unused API, take location input and return nearby restaurnat name
# def find_place(search_term):


#     with open("key/googlemaps_key.json") as f:
#         data = json.load(f)

#     gmaps = googlemaps.Client(key = data["API key"])

#     response = gmaps.places(query = search_term, radius = 40000 , type = 'restaurant')
#     results = response["results"]

#     data = { "results" : []}
#     for result in results:
#         place_name = result["name"]
#         google_rating = result["rating"]
           
#         # appending the data 
#         data["results"].append({"name" : result["name"], "g_rating" : result["rating"]})

#     return data


if __name__ == '__main__':
    # f = open("input.txt", "r")
    # text = f.read()
    text = 'Guido van Rossum is great!'

    # try:
    #     print("Analyzing sentiment")
    analyze_text_sentiment(text)
    #     print("\nAnalyzing entities")
    #     analyze_text_entities(text)
    #     print("\nAnalyzing classification")
    #     classify_text(text)
    # except Exception as e: 
    #     print(e)
    #     print("Please try again")
    # find_place("Boston")