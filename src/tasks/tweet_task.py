import time
import schedule

from services.ai_service import AiService
from services.twitter_service import TwitterService

from constants.audience import AudienceType, AUDIENCE_PROMPTS


def tweet_for_audience(audience: AudienceType) -> None:
    """
    Generates a motivational message and posts it to Twitter.
    :param audience: The audience to generate a motivational message for.
    """

    try:
        # Get the prompt for the audience
        prompt = AUDIENCE_PROMPTS.get(audience)
        if not prompt:
            raise ValueError(f"Invalid audience type: {audience}")

        # Initialize the services
        ai_service = AiService()
        twitter_service = TwitterService()

        # Generate a motivational message
        message = ai_service.generate_message(prompt)

        # Post the message to Twitter
        print(f"Posting tweet for {audience}: {message}")
        response = twitter_service.post_tweet(message)
        print(f"Response: {response}")
    except Exception as e:
        raise RuntimeError(f"Failed to generate or post tweet: {e}")


def schedule_tweets():
    """
    Schedule tweets for different audiences at specific times.
    """
    # Schedule tweets for different audiences
    schedule.every().day.at("08:00").do(tweet_for_audience, audience=AudienceType.WORKING)
    schedule.every().day.at("12:00").do(tweet_for_audience, audience=AudienceType.STUDYING)
    schedule.every().day.at("16:00").do(tweet_for_audience, audience=AudienceType.ELDERLY)
    schedule.every().day.at("20:00").do(tweet_for_audience, audience=AudienceType.GRATITUDE)

    # Run the scheduler
    while True:
        schedule.run_pending()
        time.sleep(1)
