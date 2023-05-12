"""
This Cog contains some general commands that are used in the bot
"""
import json
import os

import discord
import requests
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

# gets the program path and the path to the .env file
PROGRAM_PATH = os.path.dirname(os.path.abspath(__file__))
DOTENV_PATH = os.path.join(PROGRAM_PATH, ".env")
# loads the .env file
load_dotenv(DOTENV_PATH)
# creates global variables for the server, the owner, and the meme channel
GUILD_ID = os.getenv("GUILD_ID")
GUILD = discord.Object(GUILD_ID)
OWNER_ID = int(os.getenv("OWNER_ID"))
MEME_CHANNEL_ID = int(os.getenv("MEME_CHANNEL_ID"))
# creates a global variable for the blacklisted users
blacklisted_users_str: str = os.getenv("BLACKLISTED_USERS")
BLACKLISTED_USERS = json.loads(blacklisted_users_str)


def not_blacklisted_user(interaction: discord.Interaction) -> bool:
    """ checks if the user is allowed to use the bot """
    return interaction.user.id not in BLACKLISTED_USERS


class GeneralCommandsCog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.bot = client

    @app_commands.command(name="ping", description="Pong!")
    @app_commands.check(not_blacklisted_user)
    async def ping(self, interaction: discord.Interaction) -> None:
        """ Pong! """
        await interaction.response.send_message("Pong!", ephemeral=True)

    @app_commands.command(name="cleardms", description="bot removes all the messages that it has sent in your DMs")
    @app_commands.check(not_blacklisted_user)
    async def clear_dms(self, interaction: discord.Interaction) -> None:
        """ bot removes all the messages that it has sent in your DMs """
        if interaction.user.id == OWNER_ID:
            await interaction.response.send_message("Deleting all my messages in your DMs", ephemeral=True)
            # check if the user has a dm channel
            if interaction.user.dm_channel is None:
                await interaction.user.create_dm()
            # delete all the messages that the bot has sent in the dm channel
            async for message in interaction.user.dm_channel.history(limit=None):
                if message.author == self.bot.user:
                    await message.delete()
        else:
            # if the user is not the owner of the bot
            await interaction.response.send_message("You are not the owner of the bot", ephemeral=True)

    @app_commands.command(name="meme", description="Sends a random meme")
    @app_commands.check(not_blacklisted_user)
    async def meme(self, interaction: discord.Interaction) -> None:
        """ Sends a random meme """
        await interaction.response.defer()
        # check if the message was in the channel ids
        if interaction.channel.id in (MEME_CHANNEL_ID):
            # get a random meme from the api
            response = requests.get("https://meme-api.com/gimme")
            if response.status_code == 200:
                data = response.json()
                meme = discord.Embed(title=str(data["title"]))
                meme.set_image(url=str(data["url"]))
            else:
                meme = discord.Embed(title="Error", description="Something went wrong", color=discord.Color.red())
            
            # send the meme
            meme_message: discord.WebhookMessage = await interaction.followup.send(embed=meme)

            # delete the meme after 10 seconds
            await meme_message.delete(delay=60)
        # if the message was not in the channel ids
        else:
            await interaction.followup.send("This command can only be used in the #memez channel", ephemeral=True)

    @app_commands.command(name="pfp", description="Sends the profile picture of the user")
    @app_commands.check(not_blacklisted_user)
    async def pfp(self, interaction: discord.Interaction, user: discord.Member = None) -> None:
        """ Sends the profile picture of the user """
        if user is None:
            user = interaction.user
        # creates an embed with the profile picture of the user and sends it
        embed = discord.Embed(title=f"{user.name}'s profile picture")
        embed.set_image(url=user.avatar.url)
        await interaction.response.send_message(embed=embed)


async def setup(client: commands.Bot) -> None:
    """ Setup the cog """
    await client.add_cog(GeneralCommandsCog(client), guild=GUILD)
