import discord
import lib.const
import safygiphy

from debug import dprint
from discord.ext import commands
from discord.voice_client import VoiceClient

class ServerBot:
    def __init__(self, bot):
        self.bot = bot
        dprint('Success!')

    @commands.command(name="test")
    async def _echo_test(self, ctx):
        await ctx.send(":wave: Hello there!")

    @commands.command(name="cat_gif")
    async def _cat(self, ctx):
        await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

    @commands.command(name="gif_me")
    async def _random_gif(self, ctx, tag):
        random_gif = safygiphy.Giphy().random(tag=tag)
        await ctx.send(file=discord.File(random_gif))