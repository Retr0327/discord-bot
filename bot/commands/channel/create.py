from models import DiscordClient
from discord.ext.commands import Cog
from discord import utils, app_commands, Interaction


class TextChannelCreator(Cog):
    """
    The TextChannelCreator object creates a text channel.
    """

    def __init__(self, bot: DiscordClient) -> None:
        self.bot = bot

    @app_commands.command(name="text_channel", description="Create a new text channel")
    async def create(self, interaction: Interaction, *, channel_name: str) -> None:
        channel = utils.get(interaction.guild.text_channels, name=channel_name)

        if channel is not None:
            await interaction.response.send_message(
                f":no_entry: **{channel_name}** already exists!",
            )
        else:
            await interaction.guild.create_text_channel(name=channel_name.strip())
            await interaction.response.defer(ephemeral=False)
            await interaction.followup.send(
                f":star: New channel **{channel_name}** is created!"
            )
