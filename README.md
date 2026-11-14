# U.R Command - X 

This is an Discord bot that uses GLM-4 Flash which automatically manages your schedule, saves tasks into a database, and sends real-time alerts when the time is up! 

This is my first Project!!!!
This project was built with a lot of hours, dedication, and custom time counters.

## Features
- **Command (`/ur-x`)**: Ask it anything with command "ur-x", and it will answer it(e.g. What is the recent news on the Iphone Duo).
- **Calendar**: Automatically saves names, tasks, and dates to save them to a local storage.
- **Reminders**: Sets up countdown timer to notify you exactly when your task is done.
- **Database**: A local, light-weighted SQLite3 database to store all task data.

---

## Setup Instructions

If you want to download and run this yourself, follow these steps:

### 1. Install
Download this repository to your computer, then install the required dependencies:
```bash
pip install discord.py python-dotenv openai
```

### 3. Environment Secrets
Provide your own API credentials to run the bot:

1. In the main directory of the bot, create a new file named `.env`.
2. Open the `.env` file and add your own Discord Token and Zhipu AI Key:
> **Note:** If you can't have a Zhipu API Key, find an alternative[See this really helpful list](https://github.com/OuterSpacee/free-ai-apis)

```env
DISCORD_TOKEN=your_discord_bot_token_here
GLM_API_KEY=your_zhipu_ai_api_key_here
```

### 4. Setting up the Bot Application
1. Go to the [Discord Developer Portal](https://discord.com/developers/home).
2. Make a new Application and click on **Bot**.
3. Under the **Bot** tab, open**Privileged Gateway Intents** and toggle it on.
4. Reset and copy the token into your `.env` file.

---

## Running

Once your `.env` file is ready, run the script:
```bash
python main.py
```

When you see `Welcome To UR Command - X` in your terminal, the bot is running! It will automatically make a local `ur_x_data.db` file to store your tasks.

Go to your Discord server and type `/ur-x` followed by your task details to test it out!
Watch an Demo Here: https://streamable.com/epok17
