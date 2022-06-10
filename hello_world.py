
from zelus.src.repositories.access.repository import AccessRepository


def main() -> None:
    repo = AccessRepository()
    text = "Alo alo teste teste"

    response = repo.tweet(tweet_text = text)


if __name__ =="__main__":
    main()