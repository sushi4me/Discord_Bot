import const
import youtube_dl

from debug import dprint
from discord import FFmpegPCMAudio, PCMVolumeTransformer, VoiceChannel
from discord.ext import commands
from discord.voice_client import VoiceClient

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

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

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state

        return state

    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = self.get_voice_state(channel.server)
        state.voice = voice

    @commands.command()
    async def sayit(self, ctx):
        url = "https://www.youtube.com/watch?v=ZiE3aVQGf8o"
        channel = ctx.message.author.voice.channel
        dprint("Attempting to join {0}".format(channel))

        if channel is not None:
            state = self.get_voice_state(channel.server)
            if state.voice is None:
                state.voice = await self.bot.join_voice_channel(channel)
            else:
                await state.voice.move_to(channel)
        
        player = await YTDLSource.from_url(url, loop=self.bot.loop)
        ctx.voice_client.play(player, after=lambda e: print('Player error %s' % e) if e else None)

        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        if voice_client:
            await vtc.voice_client.disconnect()
            dprint("Left the voice channel")
        else:
            dprint("Not in a voice channel")