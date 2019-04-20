import numpy as np
import matplotlib.pyplot as plt
import re
from twython import Twython
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

#Connect to Twitter
APP_KEY = "UnuBMCJaHRJ7ZsDmZ6qfnevJI"
APP_SECRET = "1ttW1PMAYhNxmWsd6GY4HSJkpdS3FlkN97vkKxShfCnB8eFHB0"

def get_all_asc_for_user(name):
    print("returning all ascociated for: " + name)
    followers = []
    followers = get_full_set_followers(name)
    followers = followers + get_full_set_friends(name)
    return followers

def get_full_set_followers(name):
    twitter = Twython(APP_KEY, APP_SECRET)
    cursor = -1
    followers = []

    while(cursor!=0):
        response_dictionary = twitter.get_followers_list(screen_name=name)
        cursor = response_dictionary['next_cursor']
        for x in response_dictionary['users']:
            followers.append(x)
    return followers

def get_full_set_friends(name):
    twitter = Twython(APP_KEY, APP_SECRET)
    cursor = -1
    followers = []

    while(cursor!=0):
        response_dictionary = twitter.get_friends_list(screen_name=name)
        cursor = response_dictionary['next_cursor']
        for x in response_dictionary['users']:
            followers.append(x)
    return followers


def get_2nd_level(name):
    followers=[]
    for x in get_all_asc_for_user("pierules53"):
        for y in get_all_asc_for_user(x['screen_name']):
            followers.append(y)
    output = [dict(t) for t in {tuple(d.items()) for d in followers}]
    return output

def get_user_list_from_file():
    filepath = 'names'
    names=[]
    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            names.append(line.rstrip())
    return names

def main():
    print(get_user_list_from_file())
    print("done")


if __name__ == "__main__":
    main()
