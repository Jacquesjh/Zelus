
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

from zelus import Artist


def main() -> None:
    artist = Artist()
    num_people = 500
    artist.unfollow_people(num_people = num_people)


if __name__ == "__main__":
    # time.sleep(random.randint(30, 180))
    time.sleep(random.randint(1, 3))
    main()