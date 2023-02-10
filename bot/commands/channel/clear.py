from models.discord import DiscordClient
from discord.ext.commands import Cog
from discord import app_commands, Interaction, TextChannel


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
    async def clear(self, interaction: Interaction, *, channel_name: TextChannel):
        await interaction.response.defer(ephemeral=False)
        await channel_name.purge()
        await interaction.followup.send(
            f":broom: Channel **{channel_name}** chat history has been cleared!"
        )
