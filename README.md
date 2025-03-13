# BotOuan

BotOuan is a Discord bot that interacts with users using OpenAI's GPT models.
 
## Features

- Responds to messages in a specific Discord channel.
- Uses OpenAI's GPT models to generate responses.
- Customizable system prompt and unknown responses.
- Joins and leaves voice channels.
- Speaks responses using Edge-TTS.

## Setup

1. Clone the repository.
2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Create a `.env` file in the root directory and add your Discord token, OpenAI API key, and allowed channel ID:
    ```
    DISCORD_TOKEN=your_discord_token
    OPENAI_API_KEY=your_openai_api_key
    ALLOWED_CHANNEL_ID=your_allowed_channel_id
    ```
4. Customize the `data/core.json` file with your desired system prompt and unknown responses.

## Running the Bot

To run the bot, execute the following command:
```sh
python bot.py
```

## Files

- `bot.py`: Main bot script.
- `modules/chat.py`: Handles chat interactions.
- `modules/config.py`: Loads configuration from `.env`.
- `modules/voice.py`: Manages voice channel interactions and text-to-speech.
- `data/commands.json`: JSON file containing command mappings.
- `data/core.json`: JSON file containing the system prompt and unknown responses.
- `requirements.txt`: List of dependencies.
- `.env`: Environment variables file.

## License

This project is licensed under the MIT License..
