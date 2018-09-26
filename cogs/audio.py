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
        print(ctx.__class__.__mro__)


# Necessary for cogs
def setup(server_bot):
    server_bot.add_cog(Audio(server_bot))