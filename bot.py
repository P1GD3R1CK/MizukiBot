import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # needed to read messages
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Trigger word(s) and sticker
TRIGGER_WORDS = ["mizuki"]   # add as many as you like
STICKER_ID = 1428133923958951997  # replace with your sticker ID


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


@bot.event
async def on_message(message):
    # ignore messages from the bot itself
    if message.author.bot:
        return

    # check if any trigger word appears in the message
    content_lower = message.content.lower()
    if any(word in content_lower for word in TRIGGER_WORDS):
        try:
            await message.channel.send(stickers=[discord.Object(id=STICKER_ID)])
            print(f"🎉 Sent sticker for trigger word in: '{message.content}'")
        except Exception as e:
            print(f"❌ Error sending sticker: {e}")

    # let commands still work
    await bot.process_commands(message)

from flask import Flask
from threading import Thread

app = Flask('')

# Define a simple route
@app.route('/')
def home():
    return "Bot is alive!"

# Function to run the Flask app
def run():
    # On Render/Replit, the port is typically read from environment variables
    import os
    port = int(os.environ.get("PORT", 8081))
    app.run(host='0.0.0.0', port=port)

# Start the Flask server in a separate thread
def keep_alive():
    Thread(target=run).start()

keep_alive()
bot.run(TOKEN)