# Telegram Bot and Web Server

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Devansh0012/AageBot.git
    cd AageBot
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Initialize the database:

    ```bash
    python -m app.db
    ```

4. Run the Flask server:

    ```bash
    python run.py
    ```

5. Run the Telegram bot:

    ```bash
    python -m app.bot
    ```

## Usage

1. Start the bot and use `/create` to generate your unique link.
2. Visit `http://localhost:5000/link/{id}` to see your Telegram user ID.

## Bot Username

`Aaagee_bot`

## Using Through Heroku

1. Open the following link: ```https://aagebot-e7c002fc374d.herokuapp.com/```
2. Open the telegram bot using the link on the website
3. Start the bot and use `/create` to see the unique link id.
4. The bot is not hosted yet thus you need to run the bot locally on your system using `python -m app.bot` and then open the telegram bot to generate the link.
