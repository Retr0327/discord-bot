import asyncio
from config import TOKEN
from models import DiscordClient


async def run_discord_bot():
    client = DiscordClient()
    async with client:
        await client.load_extension("commands.setup")
        await client.start(token=TOKEN)


if __name__ == "__main__":
    asyncio.run(run_discord_bot())
