import const
from debug import dprint
from discord import Game, Status
from discord.ext import commands
from discord.voice_client import VoiceClient

class ServerBot():
    def __init__(self, config_dict, description):
        bot = commands.Bot(command_prefix=config_dict['prefix'], description=description)
        dprint('Success!')

        @bot.event
        async def on_ready():
            dprint('Logged in as: {0}, {1}\n{2}'.format(bot.user.name, bot.user.id, const.DIVIDER))
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

        @bot.command()
        async def echo(ctx):
            await ctx.send(":wave: Hello there!")

        @bot.command()
        async def cat(ctx):
            await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

        @bot.command(pass_context=True)
        async def sayit(ctx):
            url = "https://www.youtube.com/watch?v=ZiE3aVQGf8o"
            channel = ctx.message.author.voice_channel
            vc = await bot.join_voice_channel(channel)
            player = await vc.create_ytdl_player(url)
            player.start()

        # Login, start bot
        bot.run(config_dict['token'])