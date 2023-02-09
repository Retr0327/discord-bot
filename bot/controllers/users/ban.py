from typing import Optional
from models import DiscordClient
from discord import Object, Member, Interaction

template = {
    "member": "Dear {}, you have been banned from {}\nReason: {}",
    "channel": "**{}** has been banned!\nReason: {}",
}


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
        member_msg = template["member"].format(
            member.name,
            interaction.guild.name,
            "Not Specified" if reason is None else reason,
        )
        channel_msg = template["channel"].format(member.name, "Not Specified")

        await member.send(member_msg)
        await interaction.response.send_message(channel_msg)
        await member.ban()

    return ban
