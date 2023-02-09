import asyncio
from config import get_env
from models import DiscordClient

TOKEN = get_env("token")

command_plugins = [
    "commands.users.ban",
    "commands.users.echo",
    "commands.channel.clear",
    "commands.channel.create",
    "commands.channel.delete",
]


async def run_discord_bot():
    client = DiscordClient()
    async with client:
        await asyncio.gather(
            *[client.load_extension(plugin) for plugin in command_plugins]
        )
        await client.start(token=TOKEN)


if __name__ == "__main__":
    asyncio.run(run_discord_bot())
