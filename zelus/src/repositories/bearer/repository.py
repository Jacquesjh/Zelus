
from zelus.src.core.interfaces.infrastructure.twitter import ITwitterInfrastructure

from zelus.src.core.interfaces.repositories.twitter import IBearerRepository


class BearerRepository(IBearerRepository, ITwitterInfrastructure):


    bearer_token: str = os.environ["BEARER_TOKEN"]


    def get_user_tweets(self):
        pass


    def get_user_retweets(self):
        pass


    def search_for_people(self):
        pass


    def get_user_like_tweet(self, tweet_id: str):
        pass


    def get_users_followers(self):
        pass


    def get_recent_tweets(self, query, num_tweets):
        pass