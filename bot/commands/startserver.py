import subprocess

from discord import app_commands, Interaction
from discord.ext.commands import Bot


async def setup(bot: Bot):
    def is_admin(interaction: Interaction) -> bool:
        return any(role.name == "Admin" for role in interaction.user.roles)
    
    @app_commands.check(is_admin)
    @bot.tree.command(
        name = "startserver",
        description = "Starts the server."
    )
    async def startserver(interaction: Interaction):
        subprocess.run(["./startserver.sh"])