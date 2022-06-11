
# ---------------- Fixing firectory importing ----------------
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir  = os.path.dirname(current_dir)
parent_parent_dir = os.path.dirname(parent_dir)

sys.path.append(parent_parent_dir)
# ------------------------------------------------------------

import json
import random

from zelus.src.repositories.access.repository import AccessRepository

import json
import random


def load_nft() -> dict:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    
    with open(f"{current_dir}/cache_nfts.json") as file:
        nfts = json.load(file)
    
    print(f"cache nfts - {len(nfts)}")

    if nfts == dict():
        with open(f"{current_dir}/nfts.json") as file:
            nfts = json.load(file)

    nft_name = random.choice(list(nfts.keys()))
    nft_info = nfts.get(nft_name)

    del nfts[nft_name]

    with open(f"{current_dir}/cache_nfts.json", "w") as file:
        json.dump(nfts, file)

    return nft_name, nft_info


def main() -> None:
    nft = load_nft()

    nft_name = nft[0]
    nft_info = nft[1]
    
    collection = nft_info["collection"]
    link       = nft_info["link"]

    
    text1 = random.choice(["Behold", "How about", "Check", "How would you like"])
    text2 = random.choice(["this", "my"])
    text3 = random.choice(["amazing", "awesome"])
    text4 = random.choice(["by me", "by myself", "by yours truly"])
    text5 = random.choice(["From the", "Part of the", "Out of the"])
    text6 = random.choice(["Luxury", ""])
    text7 = random.choice(["available at", "only at", "at"])
    
    text = f'{text1} {text2} {text3} "{chosen_nft}" #NFT {text4} #JacquesDeVoid | {text5} {collection} {text6} Collection {text7} @opensea\n\n {link}'
    repo = AccessRepository()
    response = repo.tweet(tweet_text = text)
    repo.like_tweet(tweet_id = response.data["id"])


if __name__ == "__main__":
    main()