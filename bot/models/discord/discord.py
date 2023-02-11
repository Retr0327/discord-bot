from typing import List
from asyncio import Task
from services import get_schedulers
from config import BOT_PREFIX, GUILD
from utils.logger import setup_logger
from utils.schedule import schedule_message
from discord.ext.commands import Bot, when_mentioned_or
from discord import Intents, Activity, ActivityType, Object


logger = setup_logger(__name__)


class DiscordClient(Bot):
    """
    The DiscordClient object represents a Discord bot.
    """

    def __init__(self) -> None:
        intents = Intents.default()
        intents.message_content = True
        intents.members = True
        activity = Activity(name=f"{BOT_PREFIX}help", type=ActivityType.listening)
        self.tasks: List[Task] = []
        super().__init__(
            command_prefix=when_mentioned_or(BOT_PREFIX),
            intents=intents,
            activity=activity,
        )

    async def on_ready(self) -> None:
        logger.info("⚡️[bot] Ready to accept connections")

        # load tasks from db
        schedulers = get_schedulers()
        if schedulers:
            for scheduler in schedulers:
                _, cid, message, event_time = scheduler
                task = self.loop.create_task(
                    schedule_message(self.get_channel(cid), message, event_time),
                    name=cid,
                )
                self.tasks.append(task)

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=Object(id=GUILD))
        logger.info("⚡️[bot] Slash commands synced!")
