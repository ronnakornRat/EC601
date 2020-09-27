import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../key.json"

from google.cloud import language
from google.cloud.language import enums, types


def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = [
        ('text', text),
        ('score', sentiment.score),
        ('magnitude', sentiment.magnitude),
    ]
    for k, v in results:
        print('{:10}: {}'.format(k, v))

text = 'Guido van Rossum is great!'
analyze_text_sentiment(text)