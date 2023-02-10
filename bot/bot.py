import asyncio
from models.sql import init_db
from models.discord import DiscordClient
from config import TOKEN, DB_PATH, make_db_dir


async def run_discord_bot() -> None:
    if not DB_PATH.is_file():
        make_db_dir()
        init_db()

    client = DiscordClient()
    async with client:
        await client.load_extension("commands.setup")
        await client.start(token=TOKEN)


if __name__ == "__main__":
    asyncio.run(run_discord_bot())
