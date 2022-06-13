
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


def get_influencers_list() -> list:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    
    with open(f"{current_dir}/influencers.json") as file:
        influencers_json = json.load(file)

    influencers_list = influencers_json["influencers"]

    return influencers_list


def main() -> None:
    influencers = get_influencers_list()

    artist = Artist()
    
    artist.follow_people(influencers = influencers)


if __name__ == "__main__":
    time.sleep(random.randint(30, 180))
    main()