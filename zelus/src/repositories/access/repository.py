
import os
from typing import Union

from TwitterAPI import TwitterAPI
from zelus.src.infrastructure.twitter.infrastructure import AccessInfrastructure
from zelus.src.core.interfaces.repositories.twitter import IAccessRepository


class AccessRepository(IAccessRepository, AccessInfrastructure):


    # consumer_key       : str = os.environ["CONSUMER_KEY"]
    # consumer_secret    : str = os.environ["CONSUMER_SECRET"]
    # access_token       : str = os.environ["ACCESS_TOKEN"]
    # access_token_secret: str = os.environ["ACCESS_SECRET"]

    consumer_key       : str = "JXFOP8KkkrYnaVzw02beckdGz"
    consumer_secret    : str = "3d3zbl2kIXrD64YdlwlUosq3TLps9fnyyWOIlwlBwLDMWqsQtg"
    access_token       : str = "1474097571408883730-APQnJxCASOZehB0zYJb8zey4XhC9Z6"
    access_token_secret: str = "7qzcHlgPw5e4oF8122FH2XBshTGox8nToD5Uft9MQrXNY"


    def unfollow_user_id(self, user_id: str) -> None:
        client = self.get_client(consumer_key = self.consumer_key,
                                 consumer_secret = self.consumer_secret,
                                 access_token = self.access_token,
                                 access_token_secret = self.access_token_secret)

        client.unfollow_user(target_user_id = user_id)


    def get_num_followers(self, user_id: str) -> int:
        api = TwitterAPI(self.consumer_key,
                         self.consumer_secret,
                         self.access_token,
                         self.access_token_secret,
                         api_version = "2")
                         
        followers     = api.request(f"users/:{user_id}/followers")
        num_followers = len([f for f in followers])

        return num_followers


    def like_tweet(self, tweet_id: str) -> None:
        client = self.get_client(consumer_key = self.consumer_key,
                                 consumer_secret = self.consumer_secret,
                                 access_token = self.access_token,
                                 access_token_secret = self.access_token_secret)

        client.like(tweet_id = tweet_id)


    def follow(self, user_id: str) -> None:
        client = self.get_client(consumer_key = self.consumer_key,
                                 consumer_secret = self.consumer_secret,
                                 access_token = self.access_token,
                                 access_token_secret = self.access_token_secret)

        client.follow_user(target_user_id = user_id)


    def delete_tweet(self, tweet_id: str) -> None:
        client = self.get_client(consumer_key = self.consumer_key,
                                 consumer_secret = self.consumer_secret,
                                 access_token = self.access_token,
                                 access_token_secret = self.access_token_secret)

        client.delete_tweet(id = tweet_id)


    def tweet(self, tweet_text: str) -> Union:
        client = self.get_client(consumer_key = self.consumer_key,
                                 consumer_secret = self.consumer_secret,
                                 access_token = self.access_token,
                                 access_token_secret = self.access_token_secret)

        response = client.create_tweet(text = tweet_text)

        return response


    def reply(self, tweet_text: str, tweet_id_to_reply: str) -> Union:
        client = self.get_client(consumer_key = self.consumer_key,
                                 consumer_secret = self.consumer_secret,
                                 access_token = self.access_token,
                                 access_token_secret = self.access_token_secret)

        response = client.create_tweet(text = tweet_text, in_reply_to_tweet_id = tweet_id_to_reply)

        return response