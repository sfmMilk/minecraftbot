import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler('discord.log', 'utf-8', 'w')
intents = discord.Intents.default
intents.message_content = True
intents.members = True
