import tweepy
consumer_key="hmL3tbCl4Y7JgpKsDHKCpTEm9"
consumer_secret="zGJXewHINvlNE7ViTA10YuGsjZcOJamA1dgdF3V2aN0uF54zc2"
access_token="741301816361635840-p46wy3cSUEfuoozXvYNDvrfhpQjjt07"
access_token_secret="Edvzh6AN9KZdZtIClohE1K3KWPMlzY8u3rRRRxKJn8ztW"
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
user=api.user_timeline(screen_name="realDonaldTrump")
tmpp=[]
tweets_for_csv =[tweet.text for tweet in user] # CSV file created  
for j in tweets_for_csv:
        tmpp.append(j)
                      
import numpy as nm
# Cleaning Spaces from each and every tweets
for  i in range(len(tmpp)):
     tmpp[i]=tmpp[i].replace('\n','')        
import re

for i in range(len(tmpp)):
    x=re.compile(r'https://t.co/*[a-zA-Z0-9]*',re.DOTALL)
    tmpp[i]=re.sub(x,'',tmpp[i])
    print(tmpp[i])
for i in range(len(tmpp)):
    tmpp[i]=re.sub(r'@[a-zA-Z_.0-9]*| #[a-zA-Z0-9]*','',tmpp[i])
    print(tmpp[i])
from textblob import TextBlob
po=[]
for i in range(len(tmpp)):
    analysis=TextBlob(tmpp[i])
    po.append(analysis.sentiment.polarity)
    print(po[i],tmpp[i])
import pandas as pd
sentiment=pd.DataFrame(po,columns=["Polarity"])
senti=pd.DataFrame({'pol':po,'Tweets':tmpp},columns=["pol","Tweets"])
senti.head()
import matplotlib.pyplot as plt
import seaborn as sns
x_axis=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
plt.plot(x_axis, senti.pol)
plt.show()
