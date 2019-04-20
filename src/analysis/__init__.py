import numpy as np
import matplotlib.pyplot as plt
import re
from twython import Twython
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

#Connect to Twitter
APP_KEY = "UnuBMCJaHRJ7ZsDmZ6qfnevJI"
APP_SECRET = "1ttW1PMAYhNxmWsd6GY4HSJkpdS3FlkN97vkKxShfCnB8eFHB0"
twitter = Twython(APP_KEY, APP_SECRET)


#Get timeline
user_timeline=twitter.get_user_timeline(screen_name='Nike',count=1)

#get most recent id
last_id = user_timeline[0]['id']-1
for i in range(16):
    batch = twitter.get_user_timeline(screen_name='Nike',count=200, max_id=last_id)
    user_timeline.extend(batch)
    last_id = user_timeline[-1]['id'] - 1

#Extract textfields from tweets
raw_tweets = []

for tweets in user_timeline:
    raw_tweets.append(tweets['text'])

print("raw tweets:::")
print(raw_tweets)
#Create a string form of our list of text

raw_string = ''.join(raw_tweets)
no_links = re.sub(r'http\S+', '', raw_string)
no_unicode = re.sub(r"\\[a-z][a-z]?[0-9]+", '', no_links)
no_special_characters = re.sub('[^A-Za-z ]+', '', no_unicode)

words = no_special_characters.split(" ")
words = [w for w in words if len(w) > 2]  # ignore a, an, be, ...
words = [w.lower() for w in words]
words = [w for w in words if w not in STOPWORDS]

print(words)

mask = np.array(Image.open('nike.png'))

wc = WordCloud(background_color="white", max_words=2000, mask=mask)
clean_string = ','.join(words)
wc.generate(clean_string)

f = plt.figure()
# f.add_subplot(1,2, 1)
# plt.imshow(mask, cmap=plt.cm.gray, interpolation='bilinear')
# plt.title('Original Stencil')
# plt.axis("off")

plt.imshow(wc, interpolation='bilinear')
plt.title('Twitter Generated Cloud', size=10)
plt.axis("off")
plt.show()



print(":::DONE:::")