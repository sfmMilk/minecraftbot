import discord
import os
import importlib

from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

command_files = [
    #"communicate",
    "startserver",
    "stopserver",
    "status"
]

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "!", intents = intents)
guild = discord.Object(439550192526688256)

async def load_commands():
    for name in command_files:
        print(f"Loading...{name}")
        try:
            modulePath = f"commands.{name}"
            module = importlib.import_module(modulePath)
            await module.setup(bot)
            print(f"Loaded...{name}!")
        except Exception as e:
            print(e)

@bot.event
async def on_ready():
    print("Bot is running. Loading and syncing commands..")
    await load_commands()
    bot.tree.clear_commands(guild=guild)
    await bot.tree.sync(guild=guild)
    print("Synced commands.")

bot.run(token)