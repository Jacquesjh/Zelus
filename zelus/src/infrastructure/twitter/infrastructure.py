

from tweepy import Client

from zelus.src.core.interfaces.infrastructure.twitter import ITwitterInfrastructure


class BearerInfrastructure(ITwitterInfrastructure):


    client = None


    @classmethod
    def get_client(cls, bearer_token: str) -> Client:
        if cls.client is None:
            cls.client = Client(bearer_token = bearer_token, wait_on_rate_limit = True)

        return cls.client


class AccessInfrastructure(ITwitterInfrastructure):


    client = None


    @classmethod
    def get_client(cls, consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str) -> Client:
        if cls.client is None:
            cls.client = Client(consumer_key        = consumer_key,
                                consumer_secret     = consumer_secret,
                                access_token        = access_token,
                                access_token_secret = access_token_secret,
                                wait_on_rate_limit  = True)

        return cls.client