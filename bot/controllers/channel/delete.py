from models import DiscordClient
from discord import Object, Interaction, utils


def handle_delete_channel(client: DiscordClient, guild: int):
    """The handle_delete_channel function deletes a text channel.

    Args:
        client (DiscordClient): the Discord client
        guild (int): the server id
    Returns:
        a discord command
    """

    @client.tree.command(
        name="rm_text_channel",
        description="Delete an existing text channel",
        guild=Object(id=guild),
    )
    async def delete_channel(interaction: Interaction, *, channel_name: str):
        channel = utils.get(interaction.guild.text_channels, name=channel_name)

        if channel is None:
            await interaction.response.defer(ephemeral=False)
            await interaction.followup.send(
                f":warning: Channel **{channel_name}** not found!"
            )
        else:
            await client.get_channel(channel.id).delete()
            await interaction.response.defer(ephemeral=False)
            await interaction.followup.send(
                f":information_source: Channel **{channel_name}** deleted successfully!"
            )

    return delete_channel
