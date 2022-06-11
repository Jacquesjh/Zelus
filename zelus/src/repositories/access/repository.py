
import os
from typing import Union

from zelus.src.infrastructure.twitter.infrastructure import AccessInfrastructure
from zelus.src.core.interfaces.repositories.twitter import IAccessRepository


class AccessRepository(IAccessRepository, AccessInfrastructure):


    consumer_key       : str = os.environ["CONSUMER_KEY"]
    consumer_secret    : str = os.environ["CONSUMER_SECRET"]
    access_token       : str = os.environ["ACCESS_TOKEN"]
    access_token_secret: str = os.environ["ACCESS_SECRET"]


    def get_num_followers(self, user_id: str) -> int:
        api = TwitterAPI(self.consumer_key,
                         self.consumer_secret,
                         self.access_token,
                         self.access_token_secret,
                         api_version = "2")
                         
        followers = api.request(f"users/:{user_id}/followers")
        count     = len([f for f in followers])

        return count


    def like_tweet(self, tweet_id: str) -> None:
        client = self.get_client(consumer_key = self.consumer_key,
                                 consumer_secret = self.consumer_secret,
                                 access_token = self.access_token,
                                 access_token_secret = self.access_token_secret)

        response = client.like(tweet_id = tweet_id)

        return response


    def follow(self, user__id: str) -> None:
        client = self.get_client(consumer_key = self.consumer_key,
                                 consumer_secret = self.consumer_secret,
                                 access_token = self.access_token,
                                 access_token_secret = self.access_token_secret)

        response = client.follow_user(target_user_id = user__id)

        return response


    def delete_tweet(self) -> None:
        client = self.get_client(consumer_key = self.consumer_key,
                                 consumer_secret = self.consumer_secret,
                                 access_token = self.access_token,
                                 access_token_secret = self.access_token_secret)

        response = client.delete_tweet(id = tweet_id)
        
        return response


    def tweet(self, tweet_text: str) -> Union:
        client = self.get_client(consumer_key = self.consumer_key,
                                 consumer_secret = self.consumer_secret,
                                 access_token = self.access_token,
                                 access_token_secret = self.access_token_secret)

        response = client.create_tweet(text = tweet_text)

        return response


    def reply(self, tweet_text: str, tweet_id_to_reply: str) -> None:
        client = self.get_client(consumer_key = self.consumer_key,
                                 consumer_secret = self.consumer_secret,
                                 access_token = self.access_token,
                                 access_token_secret = self.access_token_secret)

        response = client.create_tweet(text = tweet_text, in_reply_to_tweet_id = tweet_id_to_reply)

        return response