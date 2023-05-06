"""
This program run the bot and loads the cogs
"""

import datetime as dt
import os
from platform import python_version

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")
GUILD = discord.Object(GUILD_ID)
OWNER_ID = os.getenv("OWNER_ID")


class Client(commands.Bot):
    """
    This class is the bot
    """
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('.'), intents=discord.Intents.all())

    async def setup_hook(self) -> None:
        """
        Loads the cogs
        """
        cogs = []
        for cog in cogs:
            await self.load_extension(cog)

    async def on_ready(self):
        """
        Prints the time, the event, and the bot's name and that it is online
        """
        # prints the time, the event, and the bot's name and that it is online
        print(f'\033[1;30m{dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\033[1;34m INFO     ' +
              f'\033[0;35mdiscord.client.event | on_ready\033[0;31m {self.user} is online\033[0;0m', flush=True)
        # prints the time, the event, and the bot's ID
        print(f'\033[1;30m{dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\033[1;34m INFO     ' +
              f'\033[0;35mdiscord.client.event | on_ready\033[0;31m Bot ID: {self.user.id}\033[0;0m', flush=True)
        # prints the time, the event, and the discord version
        print(f'\033[1;30m{dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\033[1;34m INFO     ' +
              f'\033[0;35mdiscord.client.event | on_ready\033[0;31m Discord Version: {discord.__version__}\033[0;0m',
              flush=True)
        # prints the time, the event, and the python version
        print(f'\033[1;30m{dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\033[1;34m INFO     ' +
              f'\033[0;35mdiscord.client.event | on_ready\033[0;31m Python Version: {python_version()}\033[0;0m',
              flush=True)

        synced = await self.tree.sync(guild=GUILD)

        print(f'\033[1;30m{dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\033[1;34m INFO     ' +
              f'\033[0;35mdiscord.client.event | on_ready\033[0;31m Synced {synced} commands\033[0;0m', flush=True)


bot = Client()
bot.run(DISCORD_TOKEN)