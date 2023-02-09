from log import setup_logger
from config import BOT_PREFIX, get_env
from discord.ext.commands import Bot, when_mentioned_or
from discord import Intents, Activity, ActivityType, Object

logger = setup_logger(__name__)


class DiscordClient(Bot):
    def __init__(self) -> None:
        intents = Intents.default()
        intents.message_content = True
        intents.members = True
        activity = Activity(name=f"{BOT_PREFIX}help", type=ActivityType.listening)
        super().__init__(
            command_prefix=when_mentioned_or(BOT_PREFIX),
            intents=intents,
            activity=activity,
        )

    async def on_ready(self) -> None:
        logger.info("⚡️[bot] Ready to accept connections")

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=Object(id=get_env("guild")))
        logger.info("⚡️[bot] Slash commands synced!")
