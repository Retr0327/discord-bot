from typing import Optional
from models import DiscordClient
from discord import Object, Member, Interaction


def handle_delete_user(client: DiscordClient, guild: int):
    """The handle_delete_user function kicks a user out of the channel.

    Args:
        client (DiscordClient): the Discord client
        guild (int): the server id
    Returns:
        a discord command
    """

    @client.tree.command(
        name="kick",
        description="Kick user out",
        guild=Object(id=guild),
    )
    async def delete_user(
        interaction: Interaction, member: Member, reason: Optional[str] = None
    ):
        await member.send(
            f"Dear {member}, you have been kicked out from {interaction.guild.name}"
        )
        await interaction.response.send_message(f":people_hugging: Adios **{member}**")
        await member.kick(reason=reason)

    return delete_user
