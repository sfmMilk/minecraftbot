import subprocess

from util import serverutil
from discord import app_commands, Interaction
from discord.ext.commands import Bot


async def setup(bot: Bot):
    def is_admin(interaction: Interaction) -> bool:
        return any(role.name == "Admin" for role in interaction.user.roles)
    
    @app_commands.check(is_admin)
    @bot.tree.command(
        name = "stopserver",
        description = "Stops the server."
    )
    async def stopserver(interaction: Interaction):
        status = serverutil.getStatus() != None
        if not status:
            await interaction.response.send_message("Server either isn't online.")
            return
        subprocess.run(["./stopserver.sh"])
        await interaction.response.send_message("Server stopping.. Check status before starting.")