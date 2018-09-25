from debug import dprint
from discord import Game, Status
from discord.ext import commands

DIVIDER = "----"

class ServerBot():
    def __init__(self, command_prefix, description):
        self.bot = commands.Bot(command_prefix=command_prefix, description=description)
        dprint('Success!')

    @self.bot.event
    async def on_ready(self):
        dprint('Logged in as: {0}, {1}\n{2}'.format(self.bot.user.name, self.bot.user.id, DIVIDER))
        # Set the bot's status and activity (different with the rewritten Discord lib)
        await bot.change_presence(status=Status.online, 
            activity=Game(name="Literally Botting"))

    @self.bot.event
    async def on_message(self, message):
        # Messages sent by the bot are ignored
        if message.author == self.bot.user:
            return
        # Bot will response given these patterns in a message
        if message.content.lower() == "where is bryant?":
            await message.channel.send("Late.")
        # If a message does not match the above, attempt to parse as command
        await self.bot.process_commands(message)

    @self.bot.command()
    async def echo(ctx):
        await ctx.send(":wave: Hello there!")

    @self.bot.command()
    async def cat(ctx):
        await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
