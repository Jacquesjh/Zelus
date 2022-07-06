
import os
import random
import time
from typing import List

from zelus.src.repositories.access.repository import AccessRepository
from zelus.src.repositories.bearer.repository import BearerRepository


class Influencer:


    user_id: str = os.environ["USER_ID"]


    def unfollow_people(self, num_people: int) -> None:
        pass


    def delete_my_timeline(self) -> None:
        pass


    def reply_to_something(self, hashtags: List[str], num_hashtags: int) -> None:
        pass


    def _get_people_from_influencer_followers(self, num_people: int, influencer_username: str) -> List[str]:
        bearer_repo = BearerRepository()

        influencer_data = bearer_repo.get_user_data(username = influencer_username)
        influencer_id   = influencer_data.data["id"]

        followers_id = bearer_repo.get_users_followers_id(user_id = influencer_id, num_results = num_people)

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


    def _get_people(self, num_people: int, influencers_list: List[str]) -> List[str]:
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

        if to_follow > 50:
            to_follow = 50

        while count < to_follow:
            people_ids = self._get_people(num_people = to_follow, influencers_list = influencers)

            for person_id in people_ids:
                time.sleep(random.randint(10, 60))

                try:
                    access_repo.follow(user_id = person_id)

                except:
                    pass

                count += 1


    def tweet(self, hashtags: List[str], num_hashtags: int) -> None:
        pass


    def like_tweets(self, num_tweets: int) -> None:
        bearer_repo = BearerRepository()

        query = "crypto -is:retweet"
        tweets_data = bearer_repo.get_recent_tweets_data(query = query, num_tweets = num_tweets)

        access_repo = AccessRepository()

        for tweet_data in tweets_data:
            time.sleep(random.randint(1, 25))

            try:
                access_repo.like_tweet(tweet_id = tweet_data.data["id"])

            except:
                pass