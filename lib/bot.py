import asyncio
import const
import discord

from debug import dprint
from discord.ext import commands
from discord.voice_client import VoiceClient

class ServerBot:
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}
        dprint('Success!')

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state

        return state

    @commands.command(name="test")
    async def _echo_test(self, ctx):
        await ctx.send(":wave: Hello there!")

    @commands.command(name="cat_gif")
    async def _cat(self, ctx):
        await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")