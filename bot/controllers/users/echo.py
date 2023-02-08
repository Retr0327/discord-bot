from models import DiscordClient
from discord import Object, Interaction


def handle_echo(client: DiscordClient, guild: int):
    """The handle_echo function repeats a user's input.

    Args:
        client (DiscordClient): the Discord client
        guild (int): the server id
    Returns:
        a discord command
    """

    @client.tree.command(
        name="echo",
        description="Echo a user's input.",
        guild=Object(id=guild),
    )
    async def echo(interaction: Interaction, *, message: str):
        if interaction.user == client.user:
            return
        username = interaction.user
        await interaction.response.defer(ephemeral=False)
        await interaction.followup.send(f'❗**{username}** says "{message}"')

    return echo
