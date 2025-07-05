from util import serverutil
from discord import app_commands, Interaction
from discord.ext.commands import Bot


async def setup(bot: Bot):
    def is_admin(interaction: Interaction) -> bool:
        return any(role.name == "Admin" for role in interaction.user.roles)
    
    @app_commands.check(is_admin)
    @bot.tree.command(
        name = "status",
        description = "Check the status and details of the server."
    )
    async def stopserver(interaction: Interaction):
        status = serverutil.getStatus()
        status_b = status != None

        if not status_b:
            await interaction.response.send_message("Server isn't online.")
            return
        onlinePlayers = status.players.online
        latency = float(int(status.latency * 100)) / 100
        await interaction.response.send_message(f"Players Online: {status.players.online}\nLatency: {latency}")
        