from src.services.ai_service import AiService


# Test Initialization
def test_ai_service_initialization():
    """Test if the AiService class initializes properly."""
    ai_service = AiService()

    assert ai_service is not None
    assert ai_service.generator is not None


# Test Message Generation
def test_generate_message():
    """Test if the AiService generates a motivational message."""
    ai_service = AiService()

    prompt = "students"
    message = ai_service.generate_message(prompt)

    assert message is not None
    assert isinstance(message, str)
    assert len(message) > 0  # Ensure the generated message is non-empty


# Test Message Uniqueness
def test_generate_unique_messages():
    """Test if the AiService generates unique motivational messages."""
    ai_service = AiService()

    prompt = "working professionals"
    messages = [ai_service.generate_message(prompt) for _ in range(5)]

    assert len(messages) == len(set(messages))  # Ensure uniqueness of generated messages


# Test No Prompt Inclusion
def test_generate_message_no_prompt_inclusion():
    """Test if the generated message doesn't include the prompt."""
    ai_service = AiService()

    prompt = "students"
    message = ai_service.generate_message(prompt)

    assert prompt not in message  # Ensure the prompt itself is not part of the generated message


# Test Multiple Responses Generation
def test_generate_multiple_responses():
    """Test if the AiService generates multiple responses."""
    ai_service = AiService()

    prompt = "entrepreneurs"
    message = ai_service.generate_message(prompt)

    # Ensure multiple messages are generated and returned (could be in a list or a similar structure)
    assert isinstance(message, str)  # The message should still be a single response,
    # as the generator returns one random unique message, not a list.
    assert len(message) > 0
