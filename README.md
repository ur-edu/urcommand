# U.R Command - X 

An Discord bot powered by GLM-4 Flash (Zhipu AI From Big Model) that automatically manages your schedule, saves calendar tasks into a local database, and sends real-time alerts when the time is up! 

This is my first Project!!!!
This project was built with a lot of hours, dedication, and custom time counters.

## Features
- **AI-Powered Command (`/ur-x`)**: Talk to the bot in plain language, and GLM-4 Flash will understand what you want to do.
- **Calendar Tools**: Automatically parses names, tasks, and future dates to save them to a local storage.
- **Real-Time Reminders**: Sets up automated background countdown triggers to mention you exactly when your task is due.
- **Lasting Database**: Powered by SQLite3 to seamlessly store all your task data.

---

## 🛠️ Setup Instructions for Users

If you want to download and run this bot yourself, follow these steps:

### 1. Prerequisites
Make sure you have **Python 3.8+** installed on your system.

### 2. Installation
Clone or download this repository to your computer, then install the required dependencies:
```bash
pip install discord.py python-dotenv openai
```

### 3. Environment Configuration (Secrets)
The original secrets are hidden for security reasons. You must provide your own API credentials to run the bot:

1. In the main directory of the bot, create a new file named `.env`.
2. Open the `.env` file and add your own Discord Token and Zhipu AI Key:
> **Note:** If you can't obtain Zhipu API Key, find an alternative[See this really helpful list](https://github.com/OuterSpacee/free-ai-apis)

```env
DISCORD_TOKEN=your_discord_bot_token_here
GLM_API_KEY=your_zhipu_ai_api_key_here
```

> **Note:** Never share your `.env` file or upload it to GitHub. Keep your tokens private

### 4. Setting up the Bot Application
1. Go to the [Discord Developer Portal](https://discord.com/developers/home).
2. Create a new Application and add a **Bot**.
3. Under the **Bot** tab, ensure you have **Privileged Gateway Intents** toggled ON (specifically Application Commands/Default Intents).
4. Reset and copy the token into your `.env` file.

---

## Running

Once your `.env` file is ready, simply launch the script:
```bash
python bot.py
```
*(Replace `bot.py` with the actual filename of your script).*

When you see `Welcome To UR Command - X` in your terminal, the bot is online! It will automatically create a local `ur_x_data.db` file to store your tasks.

Go to your Discord server and type `/ur-x` followed by your task details to test it out!
Watch an Demo Here: https://streamable.com/epok17
