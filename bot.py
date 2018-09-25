import asyncio
import const
import discord

from debug import dprint
from discord.ext import commands
from discord.voice_client import VoiceClient

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus.dll')

class VoiceState:
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.play_next_song = asyncio.Event()
        self.songs = asyncio.Queue()
        self.skip_votes = set() # a set of user_ids that voted
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())

    def is_playing(self):
        if self.voice is None or self.current is None:
            return False

        player = self.current.player
        return not player.is_done()

    @property
    def player(self):
        return self.current.player

    def skip(self):
        self.skip_votes.clear()
        if self.is_playing():
            self.player.stop()

    def toggle_next(self):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.set)

    async def audio_player_task(self):
        while True:
            self.play_next_song.clear()
            self.current = await self.songs.get()
            await self.bot.send_message(self.current.channel, 'Now playing ' + str(self.current))
            self.current.player.start()
            await self.play_next_song.wait()

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

    @commands.command()
    async def echo(self, ctx):
        await ctx.send(":wave: Hello there!")

    @commands.command()
    async def cat(self, ctx):
        await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

    @commands.command(pass_context=True, no_pm=True)
    async def join(self, ctx):
        url = "https://www.youtube.com/watch?v=ZiE3aVQGf8o"

        channel = ctx.message.author.voice_channel
        if channel is None:
            await self.bot.say("You are not in a voice channel.")
            return False

        state = self.get_voice_state(ctx.message.server)

        if state_voice is None:
            state.voice = await self.bot.join_voice_channel(channel)
        else:
            await state.voice.move_to(channel)

        return True