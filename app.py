import string
import stopwords
from flask import Flask,render_template,request
from tweets import Twitterclient
from collections import Counter
app = Flask(__name__)
tweet=""
@app.route("/",methods=['POST','GET'])
def home():
    if request.method=='POST':
        username = request.form['username']
        print('user name ---->'+username)
        if len(username)!=0:
            count = request.form.get('noOfTweets')
            twitter_client1 = Twitterclient()
            api = twitter_client1.get_twitter_client_api()
            tweets = api.user_timeline(screen_name=username,count=count)
            emotionlist, w = analyseEmotions(tweets=tweets)
            labels = []
            for label in w.keys():
                labels.append(label)
            data = [] 
            for val in w.values():
                data.append(val)
            print(tweets)
            return render_template("index.html",tweets=tweets,labels=labels,data=data,username=username)
        else:
            return render_template("index.html",tweets=[],labels=[],data=[],username=username)
    else:
        return render_template("index.html",tweet='no tweet available')


def analyseEmotions(tweets):
    text = ' '.join([str(elem) for elem in tweets])
    lower_case = text.lower()
    cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

    token = cleaned_text.split()
    stop_words = stopwords.stop_words
    final_word = []
    for word in token:
        if word not in stop_words:
            final_word.append(word)
    emotion_list = []

    with open('./static/emotions.csv','r',encoding='latin-1') as file:
        for line in file:
            clear_line = line.replace('\n','').replace("'",'').strip()
            word,emotion = clear_line.split(',')
            if word in final_word:
                emotion_list.append(emotion)
    print(emotion_list)
    w = Counter(emotion_list)
    print(w)
    return emotion_list,w


if __name__=='__main__':
    app.run(debug=True)
    