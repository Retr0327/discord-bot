from config import get_env
from models import DiscordClient
from discord.ext.commands import Cog
from discord import utils, app_commands, Interaction, Object


class TextChannelRemover(Cog):
    def __init__(self, bot: DiscordClient) -> None:
        self.bot = bot

    @app_commands.command(
        name="rm_text_channel", description="Delete an existing text channel"
    )
    async def delete(self, interaction: Interaction, *, channel_name: str):
        channel = utils.get(interaction.guild.text_channels, name=channel_name)

        if channel is None:
            await interaction.response.defer(ephemeral=False)
            await interaction.followup.send(
                f":warning: Channel **{channel_name}** not found!"
            )
        else:
            await self.bot.get_channel(channel.id).delete()
            await interaction.response.defer(ephemeral=False)
            await interaction.followup.send(
                f":information_source: Channel **{channel_name}** deleted successfully!"
            )


async def setup(bot: DiscordClient) -> None:
    await bot.add_cog(TextChannelRemover(bot), guild=Object(id=get_env("guild")))
