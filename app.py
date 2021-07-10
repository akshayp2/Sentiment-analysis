from flask import Flask,render_template,request
from tweets import Twitterclient,TweetAnalyzer
app = Flask(__name__)
tweet=""
@app.route("/",methods=['POST','GET'])
def home():
    if request.method=='POST':
        username = request.form['username'] 
        count = request.form.get('noOfTweets')
        twitter_client1 = Twitterclient()
        # tweet_analyzer = TweetAnalyzer()
        api = twitter_client1.get_twitter_client_api()
        tweets = api.user_timeline(screen_name=username,count=count)
        return render_template("index.html",tweets=tweets)
    else:
        return render_template("index.html",tweet='no tweet available')

if __name__=='__main__':
    # df = tweet_analyzer.tweets_to_data_frame(tweets)
    # df.to_csv('test.csv')
    # print(df.head(5))
    app.run()
    