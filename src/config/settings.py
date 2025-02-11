import os

from dotenv import load_dotenv

# * Load environment variables from the .env file
# ? Moves two levels up from `src/config`
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

# ? Path to the `.env` file in the root (`verve`) directory
dotenv_path = os.path.join(BASE_DIR, ".env")

# * Load environment variables from the .env file
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path, override=True)


class Settings:
    # Twitter API credentials
    TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
    TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
    TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
