from config import get_env
from models import DiscordClient
from discord.ext.commands import Cog
from discord import app_commands, Interaction, Object


class UserEcho(Cog):
    """
    The UserEcho object repeats a user's input.
    """
    def __init__(self, bot: DiscordClient) -> None:
        self.bot = bot

    @app_commands.command(
        name="echo",
        description="Echo what a user said.",
    )
    async def echo(self, interaction: Interaction, *, message: str):
        if interaction.user == self.bot.user:
            return

        username = interaction.user
        await interaction.response.send_message(
            f':wave: **{username}** says "{message}"',
        )


async def setup(bot: DiscordClient) -> None:
    await bot.add_cog(UserEcho(bot), guild=Object(id=get_env("guild")))