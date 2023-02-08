from models import DiscordClient
from discord import Object, Interaction


def handle_create_channel(client: DiscordClient, guild: int):
    """The handle_create_channel function creates a text channel.

    Args:
        client (DiscordClient): the Discord client
        guild (int): the server id
    Returns:
        a discord command
    """

    @client.tree.command(
        name="text_channel",
        description="Create a new text channel",
        guild=Object(id=guild),
    )
    async def create_channel(interaction: Interaction, *, channel_name: str):
        await interaction.guild.create_text_channel(name=channel_name.strip())
        await interaction.response.defer(ephemeral=False)
        await interaction.followup.send(
            f":star: New channel **{channel_name}** is created!"
        )

    return create_channel
