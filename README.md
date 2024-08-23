# Telegram Bot and Web Server

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd telegram-web-server-bot
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

`<Your_Bot_Username>`
