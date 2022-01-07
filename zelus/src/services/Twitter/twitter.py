

from typing import List
import random
from datetime import datetime, timedelta
from time import sleep

from tweepy import Client, Paginator
from TwitterAPI import TwitterAPI


class Twitter:

    creds    : dict
    hash_tags: list

    nfts_to_tweet: dict
    nfts_to_reply: dict


    def __init__(self, creds: dict, nfts_to_tweet: dict, nfts_to_reply: dict) -> None:

        self.creds = creds

        self.nfts_to_tweet = nfts_to_tweet
        self.nfts_to_reply = nfts_to_reply
        
        self.influencers = ["OpenSea", "ZssBecker", "rarible", "beeple", "BoredApeYC", "elliotrades", "MetaMask", "TheSandboxGame", "TheBinanceNFT", "DCLBlogger",
                            "thebrettway", "decentraland", "niftygateway", "MrsunNFT", "BinanceChain"]
        self.hash_tags   = ["#NFTArt", "#NFTCommunity", "#NFTCollection", "#NFTArtist", "#NFTs"]
        self.my_user_id  = "1474097571408883730"


    def _get_bearer_client(self) -> Client:

        client = Client(bearer_token = self.creds["bearer_token"], wait_on_rate_limit = True)

        return client


    def _get_access_client(self) -> Client:

        client = Client(consumer_key        = self.creds["consumer_key"],
                        consumer_secret     = self.creds["consumer_secret"],
                        access_token        = self.creds["access_token"],
                        access_token_secret = self.creds["access_secret"],
                        wait_on_rate_limit  = True)

        return client


    def _search_followables(self) -> List[str]:

        client = self._get_bearer_client()

        influencer = client.get_user(username = random.choice(self.influencers))
        choices    = ["follow from tweets", "follow from followers"]

        if random.choice(choices) == choices[0]:
            print("searching from tweets")
            tweets = self._get_user_timeline_tweets(user_id = influencer.data["id"])
            tweets = [t for t in tweets.data]
            random.shuffle(tweets)

            likers = []
            for i in range(5):
                chosen_tweet = tweets.pop(0)

                temp = client.get_liking_users(id = chosen_tweet.id)
                new  = [l.id for l in temp.data]
                likers += new
            # chosen_tweet = random.choice(tweets)
            # likers = client.get_liking_users(id = chosen_tweet.id)
            # likers = [l.id for l in likers.data]
            
            return likers

        else:
            temp = client.get_users_followers(id = influencer.data["id"], max_results = 1000)
            followers = [f.id for f in temp.data]
            
            return followers


    def _get_user_timeline_tweets(self, user_id: str) -> list:

        client = self._get_bearer_client()
        tweets = client.get_users_tweets(id = user_id, exclude = ["retweets"])

        return tweets


    def _like_tweet(self, tweet_id: str) -> None:

        client   = self._get_access_client()
        response = client.like(tweet_id = tweet_id)


    def _follow(self, user_id: str) -> None:

        client   = self._get_access_client()
        response = client.follow_user(target_user_id = user_id)

    
    def _get_my_timeline(self) -> list:

        client = self._get_bearer_client()
        
        ts = client.get_users_tweets(id = self.my_user_id, tweet_fields = ["context_annotations"])

        tweets   = []
        retweets = []

        for tweet in ts.data:
            if tweet.data["text"].startswith("@"):
                retweets.append(tweet)
            
            else:
                tweets.append(tweet)

        return tweets, retweets


    def _search_tweets_to_reply(self) -> List[str]:

        client = self._get_bearer_client()
        query  = ["drop your nft -is:retweet"]

        ts = client.search_recent_tweets(query = query, tweet_fields = ["context_annotations"], max_results = 100)

        tweets = []

        for tweet in ts.data:
            if tweet["text"].startswith("@") == False:
                tweets.append(tweet)
        
        return tweets


    def _reply(self, tweet_id: str) -> None:

        chosen_nft = random.choice(list(self.nfts_to_reply.keys()))
        nft_info   = self.nfts_to_reply[chosen_nft]

        collection = nft_info["collection"]
        link       = nft_info["link"]

        random.shuffle(self.hash_tags)
        hashtags   = f"{self.hash_tags[0]} {self.hash_tags[1]} {self.hash_tags[2]} {self.hash_tags[3]} {self.hash_tags[4]}"

        text1 = "Get this #NFT to display in the #Metaverse:\n\n"
        text2 = "Check this #NFT out:\n\n"
        text3 = "How about this #NFT for your #Metaverse collection?\n\n"

        texts = [text1, text2, text3]

        text = f'{random.choice(texts)}"{chosen_nft}" by #JacquesDeVoid | From the {collection} Luxury Collection \n\n {hashtags} \n {link}'

        client   = self._get_access_client()
        response = client.create_tweet(text = text, in_reply_to_tweet_id = tweet_id)
        
        self._like_tweet(tweet_id = reponse.data["id"])


    def _get_my_retweets(self) -> List[str]:
        
        tweets = self._get_my_timeline()[1]

        return tweets


    def _get_my_tweets(self) -> List[str]:
        
        tweets = self._get_my_timeline()[0]

        return tweets


    def _delete_tweet(self, tweet_id: str) -> None:

        client   = self._get_access_client()
        response = client.delete_tweet(id = tweet_id)


    def _get_my_num_followers(self) -> int:

        api = TwitterAPI(self.creds["consumer_key"],
                         self.creds["consumer_secret"],
                         self.creds["access_token"],
                         self.creds["access_secret"],
                         api_version = "2")
                         
        followers = api.request(f"users/:{self.my_user_id}/followers")
        count     = len([f for f in followers])

        return count


    def reply_something(self) -> None:

        tweets = self._search_tweets_to_reply()

        for tweet in tweets:
            self._like_tweet(tweet_id = tweet.data["id"])

        tweet = random.choice(tweets)
        self._reply(tweet_id = tweet.data["id"])


    def delete_my_timeline(self) -> None:

        tweets = self._get_my_tweets()

        for tweet in tweets:
            self._delete_tweet(tweet_id = tweet.data["id"])


    def follow_people(self) -> None:

        num_followers = self._get_my_num_followers()

        if num_followers < 1000:
            num_followers = 1000
        
        coef      = 0.05
        to_follow = coef*num_followers
        count     = 0

        now = datetime.today()

        while count < to_follow:
            people = self._search_followables()
            if people != None:
                if len(people) > to_follow - count:
                    index = to_follow - count

                else:
                    index = len(people)

                for i in range(int(index)):
                    sleep(2)
                    self._follow(user_id = people[i])
                    count += 1
                    print(f"{i} followed")


    def tweet(self) -> None:

        chosen_nft = random.choice(list(self.nfts_to_tweet.keys()))
        nft_info   = self.nfts_to_tweet.pop(chosen_nft)

        collection = nft_info["collection"]
        link       = nft_info["link"]

        random.shuffle(self.hash_tags)
        hashtags = f"{self.hash_tags[0]} {self.hash_tags[1]} {self.hash_tags[2]} {self.hash_tags[3]} {self.hash_tags[4]} #Metaverse"

        text = f'"{chosen_nft}" #NFT by #JacquesDeVoid | Part of the {collection} Luxury Collection \n\n {hashtags} \n {link}'

        client = self._get_access_client()
        response = client.create_tweet(text = text)
        self._like_tweet(tweet_id = response.data["id"])

if __name__ == "__main__":

    with open("C:/Users/Joao/Repositories/Zelus/data/credentials.json") as file:
        creds = json.load(file)

    with open("C:/Users/Joao/Repositories/Zelus/data/nfts.json") as file:
        nfts = json.load(file)


    twitter = Twitter(creds = creds, nfts_to_reply = nfts, nfts_to_tweet = nfts)


    while True:

        if len(twitter.nfts_to_tweet) == 0:
            twitter.nfts_to_tweet == nfts

        twitter.tweet()
        
        hour = 60*60
        sleep(random.randint(hour, 2*hour))

        for i in range(6):
            twitter.reply_something()
            sleep(300)
            twitter.follow_people()
            sleep(2*hour)
        
        sleep(random.randint(10*hour, 12*hour))