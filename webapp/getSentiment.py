from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment(tweet):
    analyzer = SentimentIntensityAnalyzer()

    scores = analyzer.polarity_scores(tweet)
    
    if scores['compound'] >= 0.05:
        return 'Positive'
    elif scores['compound'] > -0.05 and scores['compound'] < 0.05:
         return 'Neutral'
    elif scores['compound'] <= -0.05:
        return 'Negative'