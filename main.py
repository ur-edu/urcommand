import os
import json
import asyncio
import sqlite3
import datetime
import discord
from discord import app_commands
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
DISCORD_TOKEN=os.getenv("DISCORD_TOKEN")
ZHIPU_API_KEY=os.getenv("GLM_API_KEY")

ai=OpenAI(
    api_key=ZHIPU_API_KEY, 
    base_url="https://open.bigmodel.cn/api/paas/v4"
)

#SQL datbase used to store messages and information 
#V1 just on computer
DB_PATH="ur_x_data.db"
def db():
    connect=sqlite3.connect(DB_PATH)
    manage=connect.cursor()
    manage.execute(
        """
        CREATE TABLE IF NOT EXISTS calander_tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            assignee TEXT,
            due_date TEXT,
            status TEXT DEFAULT 'pending'
        )
    """)
    connect.commit()
    connect.close()
    
db()
def save_calendar(title,assignee,due_time):
    #Tool 1: Save Tasks to local storage
    connect=sqlite3.connect(DB_PATH)
    manage=connect.cursor()
    manage.execute(
        "INSERT INTO calander_tasks (title,assignee,due_date) VALUES (?, ?, ?)",
        (title, assignee, due_time)
    )
    connect.commit()
    connect.close()
    return json.dumps({"status": "success", "message": f"Yay! Task 【{title}】 saved."})

async def send_reminders(ctx_interaction,delay_seconds,reminder_text):
    #Tool 2: Send messages at a specific time in teh future
    await asyncio.sleep(delay_seconds)
    user_mention=ctx_interaction.user.mention
    await ctx_interaction.followup.send(f"{user_mention} Time On Your Scedule Is UP!!! \n{reminder_text}")
TOOLS_SCHEMA=[
    {
        "type":"function",
        "function":{
            "name":"save_calendar",
            "description":"When the user want to record a future tasks/reminder/special dates or when someone did something at sometime then this opens",
            "parameters":{
                "type":"object",
                "properties":{
                    "title":{"type": "string","description":"task"},
                    "assignee":{"type":"string","description":"user in charge name"},
                    "due_time":{"type":"string","description":"date in future like 2026-10-31 00:00"}
                },
                "required":["title","assignee","due_time"]
            }
        }
    }
] 
class URXBot(discord.Client):
    def __init__(self):
        intents=discord.Intents.default()
        super().__init__(intents=intents)
        self.tree=app_commands.CommandTree(self)
    async def on_ready(self):
        print("Welcome To UR Command - X")
        print(f"Account Logined right now: {self.user}")
        await self.tree.sync()
bot=URXBot()
@bot.tree.command(name="ur-x")
async def ur_x_command(interaction:discord. Interaction, text:str):
    #await interaction.response.defer(thinking=True)
    await interaction.response.send_message("GLM-4 Flash Thinking....")

    current_now=datetime.datetime.now()
    messages=[
        {"role": "system", "content": f"You are UR Command - X, it now {current_now.strftime('%Y-%m-%d %H:%M:%S')}。You can record local calander and deploy future event notifications ability"},
        {"role": "user", "content": text}
    ]
    response = ai.chat.completions.create(
        model="glm-4-flash",
        messages=messages,
        tools=TOOLS_SCHEMA,
        tool_choice="auto"
    )
    response_message=response.choices[0].message

        
    tool_calls=response_message.tool_calls
    if tool_calls:
        messages.append(response_message)
        for tool_call in tool_calls:
            function_name=tool_call.function.name
            args=json.loads(tool_call.function.arguments)
            tool_output="Tool executed with fallback." 
            if function_name=="save_calendar":
                tool_output=save_calendar(args["title"], args["assignee"], args["due_time"])
                try:
                    target_time=datetime.datetime.strptime(args["due_time"], "%Y-%m-%d %H:%M")
                    if target_time.date()==datetime.date(1900, 1, 1):
                        target_time = target_time.replace(year=current_now.year, month=current_now.month, day=current_now.day)
                    
                    delay=(target_time-current_now).total_seconds()

                    if delay > 0:
                        reminder_msg=f"Time to finish Task【{args['title']}】! (Assigned to: {args['assignee']})"
                        asyncio.create_task(send_reminders(interaction, delay, reminder_msg))
                except Exception as time_error:
                    print(f"Time Error: {time_error}")

            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": tool_output,
            })
        final_response=ai.chat.completions.create(
            model="glm-4-flash", 
            messages=messages
        )
        reply_content=final_response.choices[0].message.content
    else:
        reply_content=response_message.content
    embed=discord.Embed(title="UR Command - X", description=reply_content, color=discord.Color.blue())
    embed.set_footer(text="Modles Used: GLM 4 Flash")
    await interaction.followup.send(embed=embed)


if __name__=="__main__":
    bot.run(DISCORD_TOKEN)

#DONE!!! This Project Spend Hours Upon Hours!! I started it before the hack club project and finished the last part with the time counter on!