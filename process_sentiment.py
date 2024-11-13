import pandas as pd
import multiprocessing as mp
import re
from tqdm.auto import tqdm
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from text2emotion import get_emotion
import nltk
import os

nltk.download('vader_lexicon')
nltk.download('omw-1.4')


ENG_TWEETS_FILE = '/Users/deryadurmush/Desktop/Jobs /balenciaga/balenciaga.pkl'
NON_ENG_TWEETS_FILE = '/Users/deryadurmush/Desktop/Jobs /balenciaga/translated_balenciaga.pkl'
OUTPUT_FILE = 'preprocessed_tweets.pkl'


tweets = pd.read_pickle(ENG_TWEETS_FILE)
eng_tweets = tweets[tweets['lang'] == 'en']
non_eng_tweets = pd.read_pickle(NON_ENG_TWEETS_FILE)


tweets = pd.concat([eng_tweets, non_eng_tweets], axis=0).reset_index(drop=True)


def clean_tweet(tweet):
    """Cleans a tweet by removing URLs, mentions, hashtags, and non-alphanumeric characters."""
    tweet = re.sub(r'http\S+', '', tweet) 
    tweet = re.sub(r'@\S+', '', tweet)    
    tweet = re.sub(r'#\S+', '', tweet)    
    tweet = re.sub(r'[^a-zA-Z0-9 ]', '', tweet) 
    tweet = tweet.lower() 
    return tweet


def analyze_sentiment_vader(tweet):
    """Analyzes sentiment using VADER."""
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(tweet)
    return scores['compound']


def analyze_emotions(tweet):
    """Extracts emotions using text2emotion."""
    return get_emotion(tweet)

tqdm.pandas()

NUM_PROCESSES = mp.cpu_count()
CHUNKSIZE = len(tweets) // NUM_PROCESSES


if __name__ == '__main__':
    with mp.Pool(processes=NUM_PROCESSES) as pool:
        tweets['clean_tweet'] = pool.map(clean_tweet, tweets['text'], chunksize=CHUNKSIZE)

    with mp.Pool(processes=NUM_PROCESSES) as pool:
        tweets['sentiment_vader'] = pool.map(analyze_sentiment_vader, tweets['clean_tweet'], chunksize=CHUNKSIZE)

    with mp.Pool(processes=NUM_PROCESSES) as pool:
        tweets['emotions'] = pool.map(analyze_emotions, tweets['clean_tweet'], chunksize=CHUNKSIZE)

    emotion_columns = ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']
    tweets[emotion_columns] = tweets['emotions'].apply(lambda x: pd.Series(x))

    tweets.to_pickle(OUTPUT_FILE)
    print("Preprocessing complete!")
