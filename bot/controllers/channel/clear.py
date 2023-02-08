from models import DiscordClient
from discord import Object, Interaction


def handle_clear_all_messages(client: DiscordClient, guild: int):
    """The handle_clear_all_messages function clears all messages in a text channel.

    Args:
        client (DiscordClient): the Discord client
        guild (int): the server id
    Returns:
        a discord command
    """

    @client.tree.command(
        name="clear",
        description="Delete all messages in a text channel.",
        guild=Object(id=guild),
    )
    async def clear(interaction: Interaction):
        await interaction.response.defer(ephemeral=False)
        await interaction.channel.purge()

    return clear
