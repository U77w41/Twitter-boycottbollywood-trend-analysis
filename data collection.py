# Here we are collecting the data from 2021-06-14 to 2022-08-30


import snscrape.modules.twitter as sntwitter
import pandas as pd

#### Collecting Boycottbollywood tweets
query1 = "(boycottbollywood) until:2022-08-30 since:2021-06-14"
tweets1 = []



for tweet in sntwitter.TwitterSearchScraper(query1).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets1) == limit:
        break
    else:
        tweets1.append([tweet.date, tweet.username, tweet.content])
        
df = pd.DataFrame(tweets1, columns=['Date', 'User', 'Tweet'])

df.to_csv(r'C:\Users\Ujjwal\Twitter-boycottbollywood-trend-analysis-\data\raw\tweets1m.csv', 
        index = False)



#### Collecting boycottlaalsinghchaddha tweets
query2 = "(boycottlaalsinghchaddha) until:2022-08-30 since:2021-06-14"
tweets2 = []


for tweet in sntwitter.TwitterSearchScraper(query2).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets2) == limit:
        break
    else:
        tweets2.append([tweet.date, tweet.username, tweet.content])
        
df2 = pd.DataFrame(tweets2, columns=['Date', 'User', 'Tweet'])
print(df2)
df2.to_csv(r'C:\Users\Ujjwal\Twitter-boycottbollywood-trend-analysis-\data\raw\tweets1mLaalSinghChadda.csv',
        index = False)



#### Collecting boycott Raksha Bandhan tweets

query3 = "(boycottrakshabandhan) until:2022-08-30 since:2021-06-14"
tweets3 = []


for tweet in sntwitter.TwitterSearchScraper(query3).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets3) == limit:
        break
    else:
        tweets3.append([tweet.date, tweet.username, tweet.content])
        
df3 = pd.DataFrame(tweets3, columns=['Date', 'User', 'Tweet'])

df3.to_csv(r'C:\Users\Ujjwal\Twitter-boycottbollywood-trend-analysis-\data\raw\tweets1m_boycottrakshabandhan.csv',
        index = False)


#### Collecting boycott Vikram Vedha tweets

query4 = "(BoycottVikramVedha) until:2022-08-30 since:2021-06-14"
tweets4 = []


for tweet in sntwitter.TwitterSearchScraper(query4).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets4) == limit:
        break
    else:
        tweets4.append([tweet.date, tweet.username, tweet.content])
        
df4 = pd.DataFrame(tweets4, columns=['Date', 'User', 'Tweet'])

df4.to_csv(r'C:\Users\Ujjwal\Twitter-boycottbollywood-trend-analysis-\data\raw\tweets1m_BoycottVikramVedha.csv',
        index = False)