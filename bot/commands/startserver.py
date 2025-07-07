import subprocess

from pathlib import Path
from util import serverutil
from discord import app_commands, Interaction
from discord.ext.commands import Bot

current_dir = Path(__file__).resolve()
bot_dir = current_dir.parent.parent
startServerBash_dir = bot_dir / "startserver.sh"

async def setup(bot: Bot):
    def is_admin(interaction: Interaction) -> bool:
        return any(role.name == "Admin" for role in interaction.user.roles)
    
    @app_commands.check(is_admin)
    @bot.tree.command(
        name = "startserver",
        description = "Starts the server."
    )

    async def startserver(interaction: Interaction):
        status = serverutil.getStatus()
        if status:
            await interaction.response.send_message("Server already up. Unable to join? Maybe wait.")
            return
        subprocess.run([startServerBash_dir])
        await interaction.response.send_message("Server starting.. Check status with the status command. (Be patient!)")