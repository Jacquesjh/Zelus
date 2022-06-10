
import os
from typing import Union

from zelus.src.infrastructure.twitter.infrastructure import AccessInfrastructure
from zelus.src.core.interfaces.repositories.twitter import IAccessRepository


class AccessRepository(IAccessRepository, AccessInfrastructure):


    consumer_key   : str = os.environ["CONSUMER_KEY"]
    consumer_secret: str = os.environ["CONSUMER_SECRET"]
    access_token   : str = os.environ["ACCESS_TOKEN"]
    access_secret  : str = os.environ["ACCESS_SECRET"]


    def get_num_followers(self) -> int:
        # api = TwitterAPI(self.creds["consumer_key"],
        #                  self.creds["consumer_secret"],
        #                  self.creds["access_token"],
        #                  self.creds["access_secret"],
        #                  api_version = "2")
                         
        # followers = api.request(f"users/:{self.my_user_id}/followers")
        # count     = len([f for f in followers])

        # return count
        pass


    def like_tweet(self) -> None:
        pass


    def follow(self) -> None:
        pass


    def delete_tweet(self) -> None:
        pass


    def tweet(self, tweet_text: str) -> Union:
        client = self.get_client(consumer_key = self.consumer_key,
                                 consumer_secret = self.consumer_secret,
                                 access_token = self.access_token,
                                 access_token_secret = self.access_token_secret)

        response = client.create_tweet(text = tweet_text)

        return reponse


    def reply(self) -> None:
        pass