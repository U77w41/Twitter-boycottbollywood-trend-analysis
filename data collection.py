# Here we are collecting the data from 2021-06-14 to 2022-08-30


import snscrape.modules.twitter as sntwitter
import pandas as pd


query = "(boycottbollywood) until:2022-08-30 since:2021-06-14"
tweets = []
limit = 1000000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)
df.to_csv('tweets1m.csv')