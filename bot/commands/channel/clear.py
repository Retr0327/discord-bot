from models.discord import DiscordClient
from discord.ext.commands import Cog
from discord import app_commands, Interaction


class ChatHistoryClearer(Cog):
    """
    The ChatHistoryClearer object clean the chat history.
    """

    def __init__(self, bot: DiscordClient):
        self.bot = bot

    @app_commands.command(
        name="clear",
        description="Delete all messages in a text channel.",
    )
    async def clear(self, interaction: Interaction):
        await interaction.response.defer(ephemeral=False)
        await interaction.channel.purge()
