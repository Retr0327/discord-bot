from models.discord import DiscordClient
from utils.schedule import schedule_message
from discord.ext.commands import Cog
from discord import app_commands, Interaction, TextChannel
from services import create_scheduler, delete_scheduler, get_scheduler_by_cid


class TextChannelBrodcaster(Cog):
    """
    The TextChannelBrodcaster object brodcast message to a specific channel at
    a specific time.
    """

    def __init__(self, bot: DiscordClient) -> None:
        self.bot = bot

    @app_commands.command(name="unbrodcast", description="Cancel a scheduler.")
    async def unbrodcast(self, interaction: Interaction, *, channel: TextChannel):
        no_schedule = not get_scheduler_by_cid(channel.id)

        if no_schedule:
            await interaction.response.send_message(
                ":man_gesturing_no: No schedule to delete!", ephemeral=False
            )
            return

        delete_scheduler(channel.id)
        for task in self.bot.tasks:
            if int(task.get_name()) == channel.id:
                task.cancel()
                self.bot.tasks.remove(task)

        await interaction.response.send_message(
            ":star_struck: Message unscheduled successfully!", ephemeral=False
        )

    @app_commands.command(
        name="brodcast",
        description="Brodcast a message every n minutes (min 60) in a specific channel.",
    )
    async def brodcast(
        self,
        interaction: Interaction,
        *,
        channel: TextChannel,
        message: str,
        minutes: int
    ):
        try:
            create_scheduler([message, channel.id, minutes])
            task = self.bot.loop.create_task(
                schedule_message(message, channel.id, minutes), name=channel.id
            )
            self.bot.tasks.append(task)
            await interaction.response.send_message(
                ":star_struck: Message scheduled successfully!", ephemeral=False
            )
        except Exception:
            await interaction.response.send_message(
                ":man_bowing: Cannot schedule message! Try again!", ephemeral=False
            )
