# BotOuan

BotOuan is a Discord bot that interacts with users using OpenAI's GPT models.

## Features

- Responds to messages in a specific Discord channel.
- Uses OpenAI's GPT models to generate responses.
- Customizable system prompt and unknown responses.

## Setup

1. Clone the repository.
2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Create a `.env` file in the root directory and add your Discord token and OpenAI API key:
    ```
    DISCORD_TOKEN=your_discord_token
    OPENAI_API_KEY=your_openai_api_key
    ```
4. Customize the `data/boonmathun_core.json` file with your desired system prompt and unknown responses.

## Running the Bot

To run the bot, execute the following command:
```sh
python bot.py
```