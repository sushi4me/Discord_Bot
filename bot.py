from debug import dprint
from discord import Game, Status
from discord.ext import commands

DIVIDER = "----"

class ServerBot():
    def __init__(self):
        dprint('Success!')

    @bot.event
    async def on_ready():
        dprint('Logged in as: {0}#{1}\n{2}'.format(bot.user.name, bot.user.id, DIVIDER))
        # Set the bot's status and activity (different with the rewritten Discord lib)
        await bot.change_presence(status=Status.online, 
            activity=Game(name="Literally Botting"))

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        if message.content.lower() == "where is bryant?":
            await message.channel.send("Late.")

    await bot.process_commands(message)

    @bot.command()
    async def echo(ctx):
        await ctx.send(":wave: Hello there!")

    @bot.command()
    async def cat(ctx):
        await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
