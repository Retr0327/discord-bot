from typing import Optional
from models.discord import DiscordClient
from discord.ext.commands import Cog
from discord import app_commands, Interaction, Member

template = {
    "member": "Dear {}, you have been banned from **{}**\nReason: {}",
    "channel": "**{}** has been banned!\nReason: {}",
}


class UserBan(Cog):
    """
    The UserBan object bans a user.
    """

    def __init__(self, bot: DiscordClient) -> None:
        self.bot = bot

    @app_commands.command(name="ban", description="Ban user")
    async def ban(
        self, interaction: Interaction, member: Member, reason: Optional[str] = None
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

