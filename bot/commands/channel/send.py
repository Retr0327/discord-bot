from models.discord import DiscordClient
from discord.ext.commands import Cog
from discord import app_commands, Interaction, TextChannel


class ChannelMessageSender(Cog):
    """
    The ChannelMessageSender object sends message to a specific channel.
    """

    def __init__(self, bot: DiscordClient) -> None:
        self.bot = bot

    @app_commands.command(
        name="send_to", description="Send message to a specific channel."
    )
    async def send(
        self, interaction: Interaction, *, channel: TextChannel, message: str
    ):
        await channel.send(message)
        await interaction.response.send_message(":grin: Message sent successfully")
