import const
import discord
import youtube_dl

from debug import dprint
from discord.ext import commands
from discord.voice_client import VoiceClient

class ServerBot:
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}
        dprint('Success!')

    @commands.command()
    async def echo(self, ctx):
        await ctx.send(":wave: Hello there!")

    @commands.command()
    async def cat(self, ctx):
        await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

    @commands.command(pass_context=True)
    async def sayit(self, ctx):
        url = "https://www.youtube.com/watch?v=ZiE3aVQGf8o"

        channel = ctx.message.author.voice.voice_channel
        await self.bot.join_voice_channel(channel)

        server = ctx.message.server
        vc = self.bot.voice_client_in(server)
        player = await vc.create_ytdl_player(url)
        players[server.id] = player
        player.start()