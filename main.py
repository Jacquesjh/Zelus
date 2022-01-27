import json
from time import sleep
import random
import os
from datetime import datetime

from zelus.src.services.Twitter.twitter import Twitter
from keep_alive import keep_alive


if __name__ == "__main__":

  with open("nfts.json") as file:
      nfts = json.load(file)

  creds = dict()
  creds["consumer_key"]    = os.environ["consumer_key"]
  creds["consumer_secret"] = os.environ["consumer_secret"]
  creds["bearer_token"]    = os.environ["bearer_token"]
  creds["access_token"]    = os.environ["access_token"]
  creds["access_secret"]   = os.environ["access_secret"]

  twitter = Twitter(creds = creds, nfts_to_reply = nfts, nfts_to_tweet = nfts)
  hour    = 60*60
  
  twitter.delete_my_timeline()

  keep_alive()
  
  while True:

    if len(twitter.nfts_to_tweet) == 0:
        twitter.nfts_to_tweet = nfts
        twitter.delete_my_timeline()

    print(f"Trying to tweet at: {datetime.today()}")

    try:
        twitter.tweet()
        print("Tweet Sucess")

    except:
        print("Tweet failed")
        pass
      
    sleep(random.randint(hour, 2*hour))

    for i in range(4):
        print(f"Trying to reply at: {datetime.today()}")

        try:
            twitter.reply_something()
            print("Reply Sucess")

        except:
            print("Reply failed")
            pass

        sleep(random.randint(300, 420))
        print(f"Trying to follow at: {datetime.today()}")

        try:
            twitter.follow_people()
            print("Follow Sucess")

        except:
            print("Follow failed")
            pass

        sleep(random.randint(2.5*hour, 3.5*hour))

    sleep(random.randint(10*hour, 12*hour))