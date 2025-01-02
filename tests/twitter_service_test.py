import pytest
from unittest.mock import patch

from src.services.twitter_service import TwitterService


# Test class initialization
@pytest.fixture
def twitter_service():
    return TwitterService()


# Test posting a tweet successfully
@patch("src.services.twitter_service.tweepy.Client.create_tweet")
def test_post_tweet_success(mock_create_tweet, twitter_service):
    # Mock the response from Twitter API
    mock_create_tweet.return_value.data = {"id": 12345, "text": "Hello, world!"}

    # Call the method
    result = twitter_service.post_tweet("Hello, world!")

    # Assertions
    assert result == {"id": 12345, "text": "Hello, world!"}
    mock_create_tweet.assert_called_once_with(text="Hello, world!")


# Test posting a tweet when a general exception occurs
@patch("src.services.twitter_service.tweepy.Client.create_tweet")
def test_post_tweet_general_exception(mock_create_tweet, twitter_service):
    # Simulate a general exception (e.g., network failure)
    mock_create_tweet.side_effect = Exception("API request failed")

    # Call the method
    result = twitter_service.post_tweet("Hello, world!")

    # Assertions
    assert result == {"error": "Failed to post tweet: API request failed"}
    mock_create_tweet.assert_called_once_with(text="Hello, world!")
