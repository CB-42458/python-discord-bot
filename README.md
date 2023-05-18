## python-discord-bot
This is a python discord bot which is a base for cogs. There is an example cog in the cogs folder. To get this bot running you require to create a `.env` file in the `./bot` directory with the following variables:
```
DISCORD_TOKEN=your_discord_token_for_your_bot
GUILD_ID=the_id_of_the_server_you_want_the_bot_to_run_on
OWNER_ID=your_discord_id
BOT_CHANNEL_ID=your_bot_channel_id
MEME_CHANNEL_ID=your_meme_channel_id
BLACKLISTED_USERS=[your_blacklisted_users_ids]
```
The `BOT_CHANNEL ID`, `MEME_CHANNEL_ID` and `BLACKLISTED_USERS` enviroment varibles are used by the `./bot/generalCommandsCog.py` file.
This project has a docker-compose.yml file which can be used to run the bot in a docker container. This bot was designed to add cogs to it for added functionality.

### Running the bot
To run the bot you need to have docker installed. Once you have it installed you can run the following command in the root directory of the project:
```
docker compose -f "docker-compose.yml" up -d --build 
```

### Adding cogs
To add cogs to the bot you need to create a new python (or folder with python files) file in the `./bot/cogs` directory. You can use the `./bot/generalCommandsCog.py` file as an example. Once you have created your cog you need to add it to the `./bot/bot.py` file. You can do this by modifying the decleration of the `cogs` variable in the `setup_hook` function of the class `Client`. For example:
if your cog file is called `./bot/cogs/myCog.py` then you would add it to the `cogs` variable like so:
```py
async def setup_hook(self) -> None:
    """
    Loads the cogs
    """
    cogs = ["cogs.generalCommandsCog", "cogs.myCog"] # <- add your cog here
    for cog in cogs:
        await self.load_extension(cog)
```