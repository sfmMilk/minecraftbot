import subprocess

from util import serverutil
from discord import app_commands, Interaction
from discord.ext.commands import Bot


async def setup(bot: Bot):
    def is_admin(interaction: Interaction) -> bool:
        return any(role.name == "Admin" for role in interaction.user.roles)
    
    def is_starting() -> bool:
        return False
    
    @app_commands.check(is_admin)
    @bot.tree.command(
        name = "startserver",
        description = "Starts the server."
    )
    async def startserver(interaction: Interaction):
        status = serverutil.getStatus() != None
        if not status: return
        subprocess.run(["./startserver.sh"])
        await interaction.response.send_message("Server starting.. Check status with the status command. (Be patient!)")