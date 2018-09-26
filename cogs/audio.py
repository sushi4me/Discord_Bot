"""
audio.py:
Used as a means to play audio in a voice channel.
"""

# Import statements
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

        if ctx.message.author.voice not None:
            #print("Aha! {0} is in {1}".format(ctx.message.author.name, ctx.message.author.voice.channel.name))
            ctx.message.author.voice.channel.connect(timeout=10.0, reconnect=True)
        else:
            print("{0} is not in a voice channel".format(ctx.message.author.name))

    @commands.command(name="disconnect")
    async def _disconnect(self, ctx):


# Necessary for cogs
def setup(server_bot):
    server_bot.add_cog(Audio(server_bot))