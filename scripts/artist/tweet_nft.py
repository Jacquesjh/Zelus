
# ---------------- Fixing firectory importing ----------------
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir  = os.path.dirname(current_dir)
parent_parent_dir = os.path.dirname(parent_dir)

sys.path.append(parent_parent_dir)
# ------------------------------------------------------------

import json
import time

from zelus import Artist


def load_single_nft() -> list:
    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(f"{current_dir}/cache_nfts.json") as file:
        nfts = json.load(file)

    if nfts == dict():
        with open(f"{current_dir}/nfts.json") as file:
            nfts = json.load(file)

    nft_name = random.choice(list(nfts.keys()))
    nft_info = nfts.get(nft_name)

    del nfts[nft_name]

    with open(f"{current_dir}/cache_nfts.json", "w") as file:
        json.dump(nfts, file)

    return [nft_name, nft_info]


def get_hashtags() -> list:
    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(f"{current_dir}/hashtags.json") as file:
        hashtags_json = json.load(file)

    hashtags_list = hashtags_json["hashtags"]

    return hashtags_list


def main() -> None:
    nft = load_single_nft()

    nft_name = nft[0]
    nft_info = nft[1]

    hashtags     = get_hashtags()
    num_hashtags = 6

    artist = Artist()

    artist.tweet(nft_name = nft_name, nft_info = nft_info, hashtags = hashtags, num_hashtags = num_hashtags)


if __name__ == "__main__":
    time.sleep(random.randint(30, 180))
    main()