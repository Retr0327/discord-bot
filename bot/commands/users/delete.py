from typing import Optional
from models.discord import DiscordClient
from discord.ext.commands import Cog
from discord import app_commands, Interaction, Member


class UserKickOff(Cog):
    def __init__(self, bot: DiscordClient) -> None:
        self.bot = bot

    @app_commands.command(name="kick", description="Kick user out")
    async def kick(
        self, interaction: Interaction, member: Member, reason: Optional[str] = None
    ):
        await member.send(
            f"Dear {member}, you have been kicked out from {interaction.guild.name}"
        )
        await interaction.response.send_message(f":people_hugging: Adios **{member}**")
        await member.kick(reason=reason)
