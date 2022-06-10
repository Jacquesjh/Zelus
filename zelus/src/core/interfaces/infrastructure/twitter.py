

from abc import ABC, abstractclassmethod

from tweepy import Client


class ITwitterInfrastructure(ABC):


    @abstractclassmethod
    def get_client(cls) -> Client:
        pass