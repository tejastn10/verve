import tweepy


class TwitterService:
    """Handles interactions with Twitter API."""

    def __init__(
        self,
        api_key: str,
        api_secret: str,
        access_token: str,
        access_secret: str,
    ) -> None:
        """Initialize the Twitter Client."""
        self.client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_secret,
        )

    def post_tweet(self, message: str) -> None:
        """Posts a tweet with the given message."""
        try:
            response = self.client.create_tweet(text=message)
            return response.data
        except Exception as e:
            raise RuntimeError(f"Failed to post tweet: {e}")
