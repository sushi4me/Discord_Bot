"""
startBot.py:
Used in setting up and starting the ServerBot.
"""

# Import statements
import aiohttp
import asyncpg
import discord
import os
import sys
import time
import traceback

from datetime import datetime
from discord.ext import commands
from optparse import OptionParser
from configManager import ConfigManager


# List of extensions
extensions = (
    'cogs.audio',
    'cogs.basic',
    'cogs.discord',
    'cogs.games',
    'cogs.giphy',
    'cogs.tracker',
    'cogs.weather'
)


class ServerBot(commands.Bot):
    def __init__(self, config_dict):
        super(ServerBot, self).__init__(command_prefix=commands.when_mentioned_or('!'),
                                        pm_help=None, 
                                        help_attrs=dict(hidden=True))
        """
        self.bot_name = config['bot']['name']
        self.token = config['bot']['token']
        self.client_id = config['bot'].getint('client_id')
        self.owner_id = config['bot'].getint('owner_id')
        self.lol_api_key = config['lol']['key']
        self.owm_api_key = config['owm']['key']
        self.giphy_api_key = config['giphy']['key']
        self.trn_api_key = config['trn']['key']
        """
        self.start_time = time.time()
        self.session = aiohttp.ClientSession(loop=self.loop)
        self.prefix = config_dict['prefix']
        self.discord_token = config_dict['discord_token']
        #self.giphy_api_key = config_dict['giphy_token']
        self.debug = config_dict['debug']

        for extension in extensions:
            try:
                self.load_extension(extension)
            except Exception as e:
                exc = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension '{extension}'\n{exc}")

    async def on_ready(self):
        await server_bot.change_presence(status=discord.Status.online, 
                                         activity=discord.Game(name="Literally Botting"))
        #print(f"{self.bot_name} - {self.client_id}")
        print(f"{datetime.now().strftime('%B %d, %Y - %I:%M%p%z')}")

    async def on_message(self, message):
        if message.author.bot:
            return
        elif message.content.lower() == "where is bryant?":
            await message.channel.send("Late.")
        else:
            await self.process_commands(message)

    async def on_command_error(self, ctx, error):
        """on_command_error(self, ctx, error)
        An event that is called when an error is 
        raised while invoking a command.
        """

        if isinstance(error, commands.CommandOnCooldown):
            minutes, seconds = divmod(error.retry_after, 60)
            await ctx.send(f"This command is on cooldown. Please wait {seconds:.0f} seconds.")          
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(f"Could not find this command: {error}")
        else:
            traceback.print_tb(error.original.__traceback__)
            print(f"{error.original.__class__.__name__}: {error.original}", file=sys.stderr)

    def run(self):
        super().run(self.discord_token, reconnect=True)


if __name__ == "__main__":
    # Option parser
    parser = OptionParser()
    parser.add_option("-l", "--local",
        dest="local",
        default=False,
        action="store_true",
        help="Will get config vars from a file instead.")
    (options, args) = parser.parse_args()

    # Read configuration file from local
    if options.local:
        config = ConfigManager(config_file="config.ini")
    else:
        config = ConfigManager()

    # Create and run ServerBot
    server_bot = ServerBot(config.config_dict)
    server_bot.run()