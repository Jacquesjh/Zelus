
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
import time

from zelus import Influencer


def get_news_list() -> list:
    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(f"{current_dir}/news.json") as file:
        influencers_json = json.load(file)

    influencers_list = influencers_json["news"]

    return influencers_list


def main() -> None:
    news = get_influencers_list()

    influencer = Influencer()

    influencer.retweet(chosen_news_username = random.choice(news))


if __name__ == "__main__":
    time.sleep(random.randint(30, 180))
    main()