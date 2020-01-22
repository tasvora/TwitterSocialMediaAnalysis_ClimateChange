import numpy as np
import pandas as pd

from sklearn.externals import joblib


import psycopg2
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import getSentiment

from config import (db_user, 
                    db_password, 
                    database, 
                    db_url)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

with open('mlmodel/twitterLinearSVCModel.pkl', 'rb') as f:
    model = joblib.load(f)

#################################################
# Database Setup
#################################################

# user = 'postgres'
# pw = 'postgres'
# database = 'myDatabase'
# url = 'database-taz.c0yf4m81wf99.us-east-2.rds.amazonaws.com:5432'

DB_URL = f'postgresql+psycopg2://{db_user}:{db_password}@{db_url}/{database}'
print(DB_URL)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(app)
# print(db.engine.table_names())

Base = automap_base()
# reflect the tables

Base.prepare(db.engine, reflect=True)
print(Base.classes.keys())
tweetpreview = Base.classes.tweetpreview





#df_tweet = pd.read_csv('data/graphAnalysis/clean_climateTwitterData_Jan20.csv')    
#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():

    return render_template("index.html")
    

@app.route("/predictTweet/<tweetTxt>")
def predictTweet(tweetTxt):
    print("the prediction of my code")
    predictedHashtag = model.predict([tweetTxt])[0]
    predictedSentiment = getSentiment.sentiment(tweetTxt)
    predictions = [predictedHashtag,predictedSentiment]
    print(predictedHashtag)
    print(predictedSentiment)
    return jsonify(predictions)

    
# Query the excel and return the jsonified results
# @app.route("/initTwitterdata1")
# def initTwitterdata1():
#     df_tweet = pd.read_csv('data/twitterhandle/all_tweets_GretaThunberg.csv')   
#     tweets = df_tweet[['text','date','hashtags']][:15]
#     return tweets.to_json(orient='records')

@app.route("/initTwitterdata")
def initTwitterdata():
    """Return the tweets obtained recently."""
    session = Session(db.engine)
    # stmt = db.session.query(tweetpreview.text,tweetpreview.date,tweetpreview.search_hashtags).statement
    #  updated_df = pd.read_sql_query(stmt, db.session.bind)
    results = session.query(tweetpreview.text, tweetpreview.date, tweetpreview.search_hashtags).limit(15).all()
    tweetTxt = []
    tweetdate = []
    tweet_search_hashtags = []
    for result in results:
        tweetTxt.append(result.text)
        tweetdate.append((result.date).strftime('%Y-%m-%d'))
        tweet_search_hashtags.append(result.search_hashtags)


    updated_df = pd.DataFrame({"text":tweetTxt,"date":tweetdate,"search_hashtags":tweet_search_hashtags})
    return updated_df.to_json(orient='records')    


@app.route('/dashboard1')
def dashboard1():
    return render_template("dashboard1.html")

@app.route('/dashboard2')
def dashboard2():
    return render_template("dashboard2.html")

@app.route('/story1')
def story1():
    return render_template("story1.html")

@app.route('/predictions')
def predictions():
    return render_template("predictions.html")


if __name__ == '__main__':
    app.run(debug=True)
