from discord import app_commands, Intents, Client


class DiscordClient(Client):
    """
    The Bot object represents a client connection that connects to Discord.
    """

    def __init__(self) -> None:
        intents = Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.synced = False
