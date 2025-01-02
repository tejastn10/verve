# Verve 🤖

**Daily Motivation at Your Fingertips**. Verve Bot is an AI-powered Twitter bot that spreads positivity and inspiration every day. Built with Python, Verve crafts personalized motivational messages for various audiences and posts them to Twitter, ensuring everyone gets their daily dose of encouragement.

## Features

- 🎯 **Personalized Motivation**
  Inspires audiences like working professionals, students, elderly people, and everyone through gratitude.

- 🤖 **AI-Powered Content**
  Integrates with AI models to generate unique and engaging motivational messages.

- ⏰ **Automated Scheduling**
  Posts daily messages to Twitter without manual intervention.

- 📦 **Modular Design**
  Built with reusable, extensible components for AI and Twitter integrations.

---

## How It Works

1. **AI Integration**
   Generates motivational messages using AI-driven language models.

2. **Twitter API**
   Posts these messages directly to a dedicated Twitter account.

3. **Audience-Specific Prompts**
   Uses custom-crafted prompts to cater to specific groups like students, professionals, and more.

4. **Scheduled Automation**
   Verve Bot runs on a scheduled job, ensuring your timeline stays consistently uplifting.

---

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/verve-bot.git
   cd verve-bot
   ```

2. Install dependencies:

   ````bash
   poetry install
   poetry shell
   pre-commit install
   pre-commit run --all-files
   ```

3. Add your API keys:

   Create a .env file in the root directory:

   ```environment
      TWITTER_API_KEY=your_twitter_key
      TWITTER_API_SECRET=your_twitter_secret
      TWITTER_ACCESS_TOKEN=your_access_token
      TWITTER_ACCESS_SECRET=your_access_secret
   ```

4. Run the tests:

   ```bash
      poetry run pytest
   ```

5. Run the bot:

   ````bash
   python src/app.py
   ```

## Project Structure

```md
verve/
├── src/
│   ├── app.py           # Main application entry point
│   ├── config/          # Configuration files
│   ├── constants/       # Constant values
│   ├── services/        # Service modules
│   ├── tasks/           # Task modules
│   └── utils/           # Utility functions
├── tests/               # Unit tests
├── poetry.lock          # Dependency management
├── pyproject.toml       # Project configuration
├── LICENSE.md           # Project License
└── README.md            # Project documentation
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Inspired by the **Verve** - an energy and enthusiasm that drives us forward.
- Built with ❤️, Python, and a sprinkle of daily motivation.
