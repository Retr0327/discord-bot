from typing import Optional
from models import DiscordClient
from discord import Object, Member, Interaction


def handle_ban(client: DiscordClient, guild: int):
    """The handle_ban function bans a user.

    Args:
        client (DiscordClient): the Discord client
        guild (int): the server id
    Returns:
        a discord command
    """

    @client.tree.command(
        name="ban",
        description="Ban user",
        guild=Object(id=guild),
    )
    async def ban(
        interaction: Interaction, member: Member, reason: Optional[str] = None
    ):
        await member.ban(reason=reason)
        await interaction.response.send_message(f":shushing_face: Be quiet **{member}**")

    return ban
