import pandas as pd
df = pd.read_csv('xyz.csv')
df.columns = ['location','tweet','lang','name','age_of_user','time_oftweet','retweet','polarity','objective']

def get_candidate(row):
    candidates = []
    text = row["tweet"].lower()
    if "clinton" in text or "hillary" in text:
        candidates.append("clinton")
    if "trump" in text or "donald" in text:
        candidates.append("trump")
    if "sanders" in text or "bernie" in text:
        candidates.append("sanders")
    return ",".join(candidates)

df["candidate"] = df.apply(get_candidate,axis=1)
import matplotlib.pyplot as plt
import numpy as np
counts = df['candidate'].value_counts()
plt.bar(range(len(counts)), counts)
plt.show()

print(counts)
from datetime import datetime
df["age_of_user"] = pd.to_datetime(df["age_of_user"])
df["time_oftweet"] = pd.to_datetime(df["time_oftweet"])
df["user_age"] = df["age_of_user"].apply(lambda x: (datetime.now() - x).total_seconds() / 3600 / 24 / 365)

print (datetime.now())

cl_tweets = df["user_age"][df["candidate"] == "clinton"]
sa_tweets = df["user_age"][df["candidate"] == "sanders"]
tr_tweets = df["user_age"][df["candidate"] == "trump"]


gr = df.groupby("candidate").agg([np.mean,np.std])
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(7, 7))
ax0, ax1 = axes.flat
print (gr[1:4])

std = gr["polarity"]["std"].iloc[1:]
mean = gr["polarity"]["mean"].iloc[1:]
print (std)
ax0.bar(range(len(std)), std)

ax0.set_title('Standard deviation of tweet sentiment')

ax1.bar(range(len(mean)), mean)
ax1.set_xticklabels(mean.index, rotation=45)
ax1.set_title('Mean tweet sentiment')

plt.tight_layout()
plt.show()
def tweet_len(text):
    if len(text)<100:
        return 'short'
    elif 100 <= len(text) <= 135:
        return 'medium'
    else:
        return 'long'

df["tweets_len"] = df["tweet"].apply(tweet_len) 
tl = {}
for candidate in ["clinton","sanders","trump"]:
    tl[candidate] = df["tweets_len"][df["candidate"]== candidate].value_counts()

fig, ax = plt.subplots()
width = .5
x = np.array(range(0, 6, 2))
ax.bar(x, tl["clinton"], width, color='g')
ax.bar(x + width, tl["sanders"], width, color='b')
ax.bar(x + (width * 2), tl["trump"], width, color='r')

ax.set_ylabel('# of tweets')
ax.set_title('Number of Tweets per candidate by length')
ax.set_xticks(x + (width * 1.5))
ax.set_xticklabels(('long', 'medium', 'short'))
ax.set_xlabel('Tweet length')
plt.show()    

