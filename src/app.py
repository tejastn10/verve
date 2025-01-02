from config.settings import Settings
from tasks.tweet_task import schedule_tweets
from utils.helpers import validate_environment_variables


def main():
    """
    Main function to run the Twitter bot.
    """
    validate_environment_variables(
        [
            Settings.TWITTER_API_KEY,
            Settings.TWITTER_API_SECRET,
            Settings.TWITTER_ACCESS_TOKEN,
            Settings.TWITTER_ACCESS_SECRET,
        ],
    )

    # Scheduler to post tweets
    schedule_tweets()


if __name__ == "__main__":
    main()
