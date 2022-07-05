
# ---------------- Fixing firectory importing ----------------
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir  = os.path.dirname(current_dir)
parent_parent_dir = os.path.dirname(parent_dir)

sys.path.append(parent_parent_dir)
# ------------------------------------------------------------

import random
import time

from zelus import Influencer


def main() -> None:
    influencer = Influencer()
    num_tweets = 100
    influencer.like_tweets(num_tweets)


if __name__ == "__main__":
    time.sleep(random.randint(30, 180))
    main()