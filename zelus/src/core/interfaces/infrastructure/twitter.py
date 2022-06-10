

from abc import ABC, abstractmethod

from tweepy import Client


class ITwitterInfrastructure(ABC):


    @abstractmethod
    @classmethod
    def get_client(cls) -> Client:
        pass