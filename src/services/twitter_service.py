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
        except tweepy.errors.Forbidden as e:
            # Handle duplicate content error (403 Forbidden)
            print(f"Error posting tweet: Forbidden - Duplicate content: {e}")
            # Optionally, try to send a different fallback message here if you need
            fallback_message = "Stay motivated! 🚀"
            try:
                # Fallback to a generic motivational tweet
                response = self.client.create_tweet(text=fallback_message)
                return response.data
            except Exception as e:
                # Log the error and return a failure response
                print(f"Error posting fallback tweet: {e}")
                return {"error": "Unable to post tweet after retry"}
        except Exception as e:
            # Catch any other general exceptions and log them
            print(f"Error posting tweet: {e}")
            return {"error": f"Failed to post tweet: {e}"}
