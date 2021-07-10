from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
import pandas as pd

import twitter_credential

class Twitterclient():
    def __init__(self,twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_timeline_tweets(self,num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline,id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credential.CONSUMER_KEY,twitter_credential.CONSUMER_SECRET)
        auth.set_access_token(twitter_credential.ACCESS_TOKEN,twitter_credential.ACCESS_TOKEN_SECRET)
        return auth


class TweetAnalyzer():
    def tweets_to_data_frame(self,tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        return df

# if __name__ == "__main__":
#    twitter_client = Twitterclient()
#    tweet_analyzer = TweetAnalyzer()
#    api = twitter_client.get_twitter_client_api()
#    tweets = api.user_timeline(screen_name="elonmusk",count="10")
#    df = tweet_analyzer.tweets_to_data_frame(tweets)
#    df.to_csv('test.csv')
#    print(df.head(5))