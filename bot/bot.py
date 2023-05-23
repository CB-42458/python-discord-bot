"""
This program run the bot and loads the cogs
"""

import os  # used for getting the path to the .env file
from platform import python_version  # used for getting the python version for the logs

import discord
import logger
from discord.ext import commands
from dotenv import load_dotenv  # used for loading the .env file

# loads the .env file and creates global variables for the server and the owner
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")
GUILD = discord.Object(GUILD_ID)
OWNER_ID = os.getenv("OWNER_ID")


def find_cogs(path: str | None = None, cogs_path: str | None = None) -> list[str]:
    """
    Finds the cogs in the cogs folder, it will add the path to the cogs to the list cogs if it ends with "Cog.py"
    """
    # creates an empty list
    cog_list: list[str] = []
    # if the path is None then it is set to the ./cogs folder
    path = path or os.path.join(os.path.dirname(os.path.abspath(__file__)), "cogs")
    # the variable cog_path is used for the method load_extension in the setup_hook method of the Client class and the
    # method likes to have the paths to the cogs in a specific format e.g. "cogs.generalCommandsCog" hence the variable
    # cogs_path is used to store the path to the cogs in that format
    cogs_path = cogs_path or "cogs."
    # for each file in the path
    for file in os.listdir(path):
        # if the file is a folder
        if os.path.isdir(os.path.join(path, file)):
            # find the cogs in the folder
            cog_list += find_cogs(os.path.join(path, file), cogs_path + file + ".")
        # if the file ends with "Cog.py"
        elif file.endswith("Cog.py"):
            # add the path to the cogs to the list cogs
            cog_list.append(cogs_path + file[:-3])

    return cog_list


class Client(commands.Bot):
    """
    This class is the bot
    """

    def __init__(self) -> None:
        super().__init__(command_prefix=commands.when_mentioned_or('.'), intents=discord.Intents.all())

    async def setup_hook(self) -> None:
        """
        Loads the cogs
        """    
        cogs: list[str] = []
        cogs += find_cogs()
        for cog in cogs:
            await self.load_extension(cog)

    async def on_ready(self) -> None:
        """
        This method is called when the bot is ready
        """
        # logs the bots details
        logger.log("INFO", "discord.on_ready", f"{self.user} is online")
        logger.log("INFO", "discord.on_ready", f"Bot ID: {self.user.id}")
        logger.log("INFO", "discord.on_ready", f"Discord Version: {discord.__version__}")
        logger.log("INFO", "discord.on_ready", f"Python Version: {python_version()}")

        # syncs the commands to the server and logs how many commands were synced
        synced = await self.tree.sync(guild=GUILD)
        logger.log("INFO", "discord.on_ready", f"Synced {len(synced)} commands")


# runs the bot
bot = Client()
bot.run(DISCORD_TOKEN)
