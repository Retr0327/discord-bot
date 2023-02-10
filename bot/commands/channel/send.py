from models.discord import DiscordClient
from discord.ext.commands import Cog
from discord import utils, app_commands, Interaction


class ChannelMessageSender(Cog):
    """
    The ChannelMessageSender object sends message to a specific channel.
    """

    def __init__(self, bot: DiscordClient) -> None:
        self.bot = bot

    @app_commands.command(
        name="send_to", description="Send message to a specific channel."
    )
    async def send(self, interaction: Interaction, *, channel_name: str, message: str):
        channel = utils.get(interaction.guild.text_channels, name=channel_name)

        if channel is None:
            await interaction.response.defer(ephemeral=False)
            await interaction.followup.send(
                f":man_gesturing_no: Channel **{channel_name}** not found!"
            )

        await channel.send(message)
        await interaction.response.send_message(":grin: Message sent successfully")
