import asyncio
import discord
from config import GUILD
from models import DiscordClient
from .users import UserBan, UserKickOff, UserEcho
from .channel import ChatHistoryClearer, TextChannelCreator, TextChannelRemover

plugins = [
    UserBan,
    UserKickOff,
    UserEcho,
    ChatHistoryClearer,
    TextChannelCreator,
    TextChannelRemover,
]


async def setup(bot: DiscordClient) -> None:
    """The setup function adds custom commands to the bot's command tree.

    Args:
        bot (DiscordClient): the Discord bot
    """
    await asyncio.gather(
        *[
            bot.add_cog(plugin(bot), guild=discord.Object(id=GUILD))
            for plugin in plugins
        ]
    )
