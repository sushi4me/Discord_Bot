import discord
import inspect

from discord import File
from discord.ext import commands
from random import choice


class Audio:
    def __init__(self, server_bot):
        self.server_bot = server_bot
        self.voice_client = None

    @property
    def voice_channel(self):
        if self.voice is None:
            return None
        else:
            return self.voice.channel

    @commands.command(name="join")
    async def _join_channel(self, ctx):
        print("ctx: {0}".format(ctx.__class__.__mro__))
        print("[1] {0}".format(ctx.message))
        print("[2] {0}".format(ctx.message.author.voice))
        print("[3] {0}".format(ctx.message.channel))
        print("[4] {0}".format(ctx.message.content))

        if isinstance(ctx.message.author, discord.Member):
            print("[5] {0}".format(ctx.message.author.voice))
            self.server_bot.connect(ctx.message.author.voice.channel)

# Necessary for cogs
def setup(server_bot):
    server_bot.add_cog(Audio(server_bot))