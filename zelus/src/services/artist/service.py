
import os
import random
from typing import List

from zelus.src.repositories.access.repository import AccessRepository
from zelus.src.repositories.bearer.repository import BearerRepository


class Artist:


    user_id    : str = os.environ["USER_ID"]
    hash_tags  : str
    influencers: List[str]


    def __init__(self, mfts_to_reply: dict, nfts_to_tweet: dict) -> None:
        pass


    def delete_my_timeline(self) -> None:
        pass


    def reply_something(self) -> None:
        pass


    def follow_people(self) -> None:
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
            bearer_repo = BearerRepository()
            people = bearer_repo.search_for_people()

            if people != None:
                if len(people) > to_follow - count:
                    index = to_follow - count

                else:
                    index = len(people)

                for i in range(int(index)):
                    sleep(random.randint(60, 180))
                    access_repo.follow(user_id = people[i])
                    count += 1


    def tweet(self) -> None:
        chosen_nft = random.choice(list(self.nfts_to_tweet.keys()))
        nft_info   = self.nfts_to_tweet.pop(chosen_nft)
        
        #s save the temp nft_data

        collection = nft_info["collection"]
        link       = nft_info["link"]

        random.shuffle(self.hash_tags)
        hashtags = f"{self.hash_tags[0]} {self.hash_tags[1]} {self.hash_tags[2]} {self.hash_tags[3]} {self.hash_tags[4]} #Metaverse"
        
        text1 = random.choice(["Behold", "How about", "Check", "How would you like"])
        text2 = random.choice(["this", "my"])
        text3 = random.choice(["amazing", "awesome"])
        text4 = random.choice(["by me", "by myself", "by yours truly"])
        text5 = random.choice(["From the", "Part of the", "Out of the"])
        text6 = random.choice(["Luxury", ""])
        text7 = random.choice(["available at", "only at", "at"])
        
        text = f'{text1} {text2} {text3} "{chosen_nft}" #NFT {text4} #JacquesDeVoid | {text5} {collection} {text6} Collection {text7} @opensea\n\n {hashtags} \n {link}'

        repo = AccessRepository()
        
        response = repo.tweet(text = text)
        repo.like_tweet(tweet_id = response.data["id"])