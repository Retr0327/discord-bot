import asyncio
from discord import TextChannel


async def schedule_message(channel: TextChannel, message: str, event_time: int) -> None:
    """The schedule_message function schedule message to a specific channel at a
    specific time.

    Args:
        channel (TextChannel): the Discord text channel
        message (str): the message to be sent
        event_time (int): the number of seconds to wait before sending the message again
    """
    while True:
        await asyncio.sleep(event_time * 60)
        await channel.send(message)
