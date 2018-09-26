import configparser
import lib.const as const
import os
import sys

from lib.bot import ServerBot
from debug import dprint
from discord import Game, Status
from discord.ext import commands
from optparse import OptionParser

def setupBot(bot):    
    @bot.event
    async def on_ready():
        dprint("Logged in as: {0}, {1}\n{2}".format(bot.user.name, bot.user.id, const.DIVIDER))
        # Set the bot's status and activity (different with the rewritten Discord lib)
        await bot.change_presence(status=Status.online, 
            activity=Game(name="Literally Botting"))

    @bot.event
    async def on_message(message):
        # Messages sent by the bot are ignored
        if message.author == bot.user:
            return
        # Bot will response given these patterns in a message
        if message.content.lower() == "where is bryant?":
            await message.channel.send("Late.")
        # If a message does not match the above, attempt to parse as command
        await bot.process_commands(message)

    return bot

if __name__ == "__main__":
    # Parse system args
    parser = OptionParser(version=const.version_no, usage=const.usage_msg)
    parser.add_option("-l", "--local", 
        action='store_true',
        dest="local",
        default=False,
        help="Running locally")

    options, args = parser.parse_args(sys.argv[1:])

    if options.local is True:
        # Read config vars from local config file
        config = configparser.ConfigParser(comment_prefixes=('#'))
        config.read(const.config)
        os.environ[const.PREFIX_STR] = config[const.DEFAULT_STR][const.PREFIX_STR]
        os.environ[const.TOKEN_STR] = config[const.DEFAULT_STR][const.TOKEN_STR]
        os.environ[const.DEBUG_STR] = config[const.DEFAULT_STR][const.DEBUG_STR]
    else:
        # Setup environment
        pass

    # Create ServerBot object
    description = "A small bot."
    bot = commands.Bot(command_prefix=os.environ[const.PREFIX_STR], 
        formatter=None,
        description=description,
        pm_help=False)
    bot = setupBot(bot)

    # Login, start bot
    bot.add_cog(ServerBot(bot))
    bot.run(os.environ[const.TOKEN_STR])