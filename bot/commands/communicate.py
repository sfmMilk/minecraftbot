from discord import app_commands, Interaction
from discord.ext.commands import Bot
# Essentially, this bot will ALWAYS listen to a specific channel and minecraft chat. When players send a chat message, it sends to discord, when people on discord send a message, it sends to the server.