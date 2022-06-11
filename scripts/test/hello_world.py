
# ---------------- Fixing firectory importing ----------------
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir  = os.path.dirname(current_dir)
parent_parent_dir = os.path.dirname(parent_dir)

sys.path.append(parent_parent_dir)
# ------------------------------------------------------------

from zelus.src.repositories.access.repository import AccessRepository


def main() -> None:
    repo = AccessRepository()
    text = "Alo alo teste teste"

    response = repo.tweet(tweet_text = text)


if __name__ =="__main__":
    main()