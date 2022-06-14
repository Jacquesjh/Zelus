
import os
from typing import List

from zelus.src.infrastructure.twitter.infrastructure import BearerInfrastructure
from zelus.src.core.interfaces.repositories.twitter import IBearerRepository


class BearerRepository(IBearerRepository, BearerInfrastructure):


    bearer_token: str = os.environ["BEARER_TOKEN"]


    def get_user_data(self, username: str) -> str:
        client = self.get_client(bearer_token = self.bearer_token)

        user_data = client.get_user(username = username)

        return user_data


    def get_user_tweets_data(self, user_id: str) -> list:
        client = self.get_client(bearer_token = self.bearer_token)

        response = client.get_users_tweets(id = user_id, tweet_fields = ["context_annotations"])

        tweets_data = []

        for tweet in response.data:
            if not tweet.data["text"].startswith("@"):
                tweets_data.append(tweet)

        return tweets_data


    def get_user_retweets_data(self, user_id: str) -> list:
        client = self.get_client(bearer_token = self.bearer_token)

        response = client.get_users_tweets(id = user_id, tweet_fields = ["context_annotations"])

        retweets_data = []

        for tweet in response.data:
            if tweet.data["text"].startswith("@"):
                retweets_data.append(tweet)

        return retweets_data


    def search_for_people_id_from_influencers(self, num_people: int, influencers_ids: List[str]) -> List[str]:
        users_id = list()

        while len(users_id) < num_people:
            for influencer_id in influencers_ids:
                followers_id = self.get_users_followers(user_id = influencer_id, num_results = num_people)

                users_id += followers_id

        if len(users_id) > num_people:
            users_id = users_id[: num_people]

        return users_id

    def search_for_people_id_from_tweets(self, num_people: int, tweets_ids: List[str]) -> List[str]:
        users_id = list()

        while len(users_id) < num_people:
            for tweet_id in tweets_ids:
                liking_users_id = self.get_liking_users_id_from_tweet(tweet_id = tweet_id)

                users_id += liking_users_id

        if len(users_id) > num_people:
            users_id = users_id[: num_people]

        return users_id


    def get_liking_users_id_from_tweet(self, tweet_id: str) -> List[str]:
        client = self.get_client(bearer_token = self.bearer_token)

        response = client.get_liking_users(id = tweet_id)
        users_id = [user.id for user in response.data]

        return users_id


    def get_users_followers_id(self, user_id: str, num_results: int) -> List[str]:
        client = self.get_client(bearer_token = self.bearer_token)
        
        response     = client.get_users_followers(id = user_id, max_results = num_results)
        followers_id = [follower.id for follower in response.data]

        return followers_id


    def get_recent_tweets_data(self, query: str, num_tweets: int) -> list:
        client = self.get_client(bearer_token = self.bearer_token)

        query = [query]

        tweets_data = client.search_recent_tweets(query = query, tweet_fields = ["context_annotations"], max_results = num_tweets)

        tweets = []

        for tweet in ts.data:
            if tweet["text"].startswith("@") == False:
                tweets.append(tweet)

        return tweets