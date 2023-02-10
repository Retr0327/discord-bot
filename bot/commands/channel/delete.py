from models.discord import DiscordClient
from discord.ext.commands import Cog
from discord import app_commands, Interaction, TextChannel


class TextChannelRemover(Cog):
    def __init__(self, bot: DiscordClient) -> None:
        self.bot = bot

    @app_commands.command(
        name="rm_text_channel", description="Delete an existing text channel"
    )
    async def delete(self, interaction: Interaction, *, channel: TextChannel):
        await channel.delete()
        await interaction.response.defer(ephemeral=False)
        await interaction.followup.send(
            f":information_source: Channel **{channel.name}** deleted successfully!"
        )
