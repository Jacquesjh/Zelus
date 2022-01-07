import json
from time import sleep
import random

from zelus.src.services.Twitter.twitter import Twitter


if __name__ == "__main__":

    with open("C:/Users/Joao/Repositories/Zelus/data/credentials.json") as file:
        creds = json.load(file)

    with open("nfts.json") as file:
        nfts = json.load(file)


    twitter = Twitter(creds = creds, nfts_to_reply = nfts, nfts_to_tweet = nfts)
    twitter.tweet()
    # while True:

    #     if len(twitter.nfts_to_tweet) == 0:
    #         twitter.nfts_to_tweet == nfts

    #     twitter.tweet()
        
    #     hour = 60*60
    #     sleep(random.randint(hour, 2*hour))

    #     for i in range(6):
    #         twitter.reply_something()
    #         sleep(300)
    #         twitter.follow_people()
    #         sleep(2*hour)
        
    #     sleep(random.randint(10*hour, 12*hour))