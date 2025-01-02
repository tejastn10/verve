import random

from transformers import pipeline, set_seed


class AiService:
    """Handles interactions with Hugging Face Transformers for text generation."""

    def __init__(self) -> None:
        """
        Initialize the Hugging Face pipeline for text generation using GPT-2.
        """
        self.generator = pipeline("text-generation", model="gpt2")
        set_seed(42)  # Set seed for reproducibility

    def generate_message(self, prompt: str) -> str:
        """
        Generates a motivational message using Hugging Face Transformers.
        :param prompt: The prompt to generate a message for.
        :return: The generated motivational message.
        """
        # Randomly vary the tone or style of the message for uniqueness
        tone = random.choice(["in a cheerful tone,", "in an inspiring way,", "in a positive mood,"])
        prompt = f"Write a motivational message for {prompt} {tone}"

        try:
            # Generate the message with additional parameters
            response = self.generator(
                prompt,
                max_length=150,  # Increased max length to allow for more content
                temperature=1.0,  # Increased randomness
                top_k=120,  # Sampling top_k words for diversity
                top_p=0.9,  # Nucleus sampling for diverse output
                do_sample=True,  # Enable sampling
                num_return_sequences=5,  # Generate multiple responses
                repetition_penalty=1.5,  # Penalize repeated phrases
                truncation=True,  # Ensure the output is not cut off
            )

            # Clean the responses to avoid duplicates and randomness issues
            messages = [r["generated_text"].strip() for r in response]

            # Ensure the message is not too similar to others
            unique_messages = list(set(messages))  # Remove exact duplicates
            if len(unique_messages) > 1:
                message = random.choice(unique_messages)  # Choose a random message from unique ones
            else:
                message = unique_messages[0]  # If there's only one unique message, use it

            # Ensure the message does not include the prompt
            if message.startswith(prompt):
                message = message[len(prompt) :].strip()

            return message
        except Exception as e:
            print(f"Error generating message: {e}")
            return "Stay motivated! 🚀"
