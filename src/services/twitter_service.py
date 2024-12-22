import tweepy
from config.settings import Settings


class TwitterService:
    """Handles interactions with Twitter API."""

    def __init__(self) -> None:
        """Initialize the Twitter Client using environment variables."""
        self.client = tweepy.Client(
            consumer_key=Settings.TWITTER_API_KEY,
            consumer_secret=Settings.TWITTER_API_SECRET,
            access_token=Settings.TWITTER_ACCESS_TOKEN,
            access_token_secret=Settings.TWITTER_ACCESS_SECRET,
        )

    def post_tweet(self, message: str) -> dict:
        """Posts a tweet with the given message.
        :param message: The message to post.
        :return: The tweet response
        """
        try:
            response = self.client.create_tweet(text=message)
            return response.data
        except Exception as e:
            raise RuntimeError(f"Failed to post tweet: {e}")
