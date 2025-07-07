import subprocess

from pathlib import Path
from util import serverutil
from discord import app_commands, Interaction
from discord.ext.commands import Bot

current_dir = Path(__file__).resolve()
bot_dir = current_dir.parent.parent
stopServerBash_dir = bot_dir / "stopserver.sh"

async def setup(bot: Bot):
    def is_admin(interaction: Interaction) -> bool:
        return any(role.name == "Admin" for role in interaction.user.roles)
    
    @app_commands.check(is_admin)
    @bot.tree.command(
        name = "stopserver",
        description = "Stops the server."
    )
    async def stopserver(interaction: Interaction):
        status = serverutil.getStatus()
        if not status:
            await interaction.response.send_message("Server isn't online.")
            return
        subprocess.run([stopServerBash_dir])
        await interaction.response.send_message("Server stopping.. Check status before starting.")