
import os
import random
import time
from typing import List

from zelus.src.repositories.access.repository import AccessRepository
from zelus.src.repositories.bearer.repository import BearerRepository


class Artist:


    user_id: str = os.environ["USER_ID"]


    def unfollow_people(self, num_people: int) -> None:
        bearer_repo = BearerRepository()
        followers_id = bearer_repo.get_users_followers_id(user_id = influencer_data)

        random.shuffle(followers_id)

        if num_people > len(followers_id):
            num_people = len(followers_id)

        access_repo  = AccessRepository()
        followers_id = followers_id[: num_people]
        
        for follower_id in followers_id:
            time.sleep(random.randint(1, 10))
            access_repo.unfollow_user_id(user_id = follower_id)


    def delete_my_timeline(self) -> None:
        bearer_repo = BearerRepository()
        my_tweets_data = bearer_repo.get_user_tweets_data(user_id = self.user_id)

        access_repo = AccessRepository()

        for tweet_data in my_tweets_data:
            time.sleep(random.randint(1, 25))
            access_repo.delete_tweet(tweet_id = tweet_data.data["id"])


    def reply_to_something(self, nft_name: str, nft_info: dict, hashtags: List[str], num_hashtags: int) -> None:
        bearer_repo = BearerRepository()

        query = ["drop your nft -is:retweet"]
        tweets_data = bearer_repo.get_recent_tweets_data(query = query, num_tweets = num_tweets)

        chosen_tweet_data = random.choice(tweets_data)
        tweet_id = chosen_tweet_data.data["id"]

        collection = nft_info["collection"]
        link       = nft_info["link"]

        tag = ""
        random.shuffle(hashtags)

        for hashtag in hashtags[: num_hashtags]:
            tag += f" {hashtag}"

        text1 = random.choice(["Get this #NFT", "Check this #NFT", "How about this #NFT"])
        text2 = random.choice([":", " to display in the #Metaverse:", " for you #Metaverse collection:"])
        text3 = random.choice(["by me", "by myself", "by yours truly"])
        text4 = random.choice(["From the", "Part of the", "Out of the"])
        text5 = random.choice(["Luxury", ""])
        text6 = random.choice(["available at", "only at", "at"])

        text = f'{text1}{text2}"{chosen_nft}" {text3} #JacquesDeVoid | {text4} {collection} {text5} Collection {text6} @opensea\n\n {hashtags} \n {link}'

        access_repo = AccessRepository()
        
        response = access_repo.reply(tweet_text = text, tweet_id_to_reply = tweet_id)
        time.sleep(random.randint(10, 60))
        access_repo.like_tweet(tweet_id = response.data["id"])


    def _get_people_from_influencer_followers(self, num_people: int, influencer_username: str) -> List[str]:
        bearer_repo = BearerRepository()

        influencer_data = bearer_repo.get_user_data(username = influencer_username)
        influencer_id   = influencer_data.data["id"]

        followers_id = bearer_repo.get_users_followers_id(user_id = influencer_data, num_results = num_people)

        return followers_id


    def _get_people_from_influencer_tweets(self, num_people: int, influencer_username: str) -> List[str]:
        bearer_repo = BearerRepository()

        influencer_data = bearer_repo.get_user_data(username = influencer_username)
        influencer_id   = influencer_data.data["id"]
    
        tweets_data = bearer_repo.get_user_tweets_data(user_id = influencer_id)
        tweets_id   = [tweet_data.data["id"] for tweet_data in tweets_data]

        likers_id = list()

        for tweet_id in tweets_id:
            users_id = bearer_repo.get_liking_users_id_from_tweet(tweet_id = tweet_id)

            likers_id += users_id

        return likers_id


    def _get_people(sel, num_people: int, influencers_list: List[str]) -> List[str]:
        options = {
            "from_tweets"   : self._get_people_from_influencer_tweets,
            "from_followers": self._get_people_from_influencer_followers,
        }

        chosen_option_function = random.choice(list(options.values()))
        chosen_influencer      = random.choice(influencers_list)

        people_id = chosen_option_function(num_people = num_people, influencer_username = chosen_influencer)

        return people_id


    def follow_people(self, influencers: List[str]) -> None:
        access_repo = AccessRepository()
        num_followers = access_repo.get_num_followers(user_id = self.user_id)

        if num_followers < 1000:
            num_followers = 1000

        coef      = 0.08
        to_follow = coef*num_followers
        count     = 0

        if to_follow > 500:
            to_follow = 500

        while count < to_follow:
            people_ids = self._get_people(num_people = to_follow, influencers_list = influencers)

            for person_id in people_ids:
                time.sleep(random.randint(10, 60))
                access_repo.follow(user_id = person_id)
                count += 1


    def tweet(self, nft_name: str, nft_info: dict, hashtags: List[str], num_hashtags: int) -> None:
        collection = nft_info["collection"]
        link       = nft_info["link"]

        tag = ""
        random.shuffle(hashtags)

        if num_hashtags > len(hashtags):
            num_hashtags = len(hashtags)

        for hashtag in hashtags[: num_hashtags]:
            tag += f" {hashtag}"

        text1 = random.choice(["Behold", "How about", "Check", "How would you like"])
        text2 = random.choice(["this", "my"])
        text3 = random.choice(["amazing", "awesome"])
        text4 = random.choice(["by me", "by myself", "by yours truly"])
        text5 = random.choice(["From the", "Part of the", "Out of the"])
        text6 = random.choice(["Luxury", ""])
        text7 = random.choice(["available at", "only at", "at"])

        text = f'{text1} {text2} {text3} "{nft_name}" #NFT {text4} #JacquesDeVoid | {text5} {collection} {text6} Collection {text7} @opensea\n\n {tag} \n {link}'

        access_repo = AccessRepository()
        
        response = access_repo.tweet(text = text)
        time.sleep(random.randint(10, 60))
        access_repo.like_tweet(tweet_id = response.data["id"])


    def like_tweets(self, num_tweets: int) -> None:
        bearer_repo = BearerRepository()

        query = ["nft -is:tweet"]
        tweets_data = bearer_repo.get_recent_tweets_data(query = query, num_tweets = num_tweets)

        access_repo = AccessRepository()

        for tweet_data in tweets_data:
            time.sleep(random.randint(1, 5))
            access_repo.like_tweet(tweet_id = tweet_data.data["id"])