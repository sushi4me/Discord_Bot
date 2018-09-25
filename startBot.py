import const
import os

from bot import ServerBot
from debug import dprint
from discord import Game, Status
from discord.ext import commands

def setupEnvironment():
    config_vars = {}
    config_vars['prefix'] = "!"
    config_vars['token'] = "none"
    return config_vars

def getEnvironmentConfigVars(temp_dict):
    for key, value in temp_dict.items():
        if key in os.environ:
            temp_dict[key] = os.environ[key]
    return temp_dict

def setupBot(bot):    
    @bot.event
    async def on_ready():
        dprint("Logged in as: {0}, {1}\n{2}".format(bot.user.name, bot.user.id, const.DIVIDER))
        # Set the bot's status and activity (different with the rewritten Discord lib)
        await bot.change_presence(status=Status.online, 
            game=Game(name="Literally Botting"))

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
    # Setup environment
    temp_dict = setupEnvironment()
    config_dict = getEnvironmentConfigVars(temp_dict)

    # Create ServerBot object
    description = "A small bot."
    bot = commands.Bot(command_prefix=config_dict['prefix'], 
        formatter=None,
        description=description,
        pm_help=False)
    bot = setupBot(bot)

    # Login, start bot
    bot.add_cog(ServerBot(bot))
    bot.run(config_dict['token'])