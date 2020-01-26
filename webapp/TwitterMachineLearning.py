import pandas as pd

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def getSentiment(tweet):
    analyzer = SentimentIntensityAnalyzer()

    scores = analyzer.polarity_scores(tweet)
    
    if scores['compound'] >= 0.05:
        return 'Positive'
    elif scores['compound'] > -0.05 and scores['compound'] < 0.05:
         return 'Neutral'
    elif scores['compound'] <= -0.05:
        return 'Negative'

def getPredictions(tweetTxt):
    print(f'the PREDICTIONS IS ............')


#getPredictions("Weather is too hot")