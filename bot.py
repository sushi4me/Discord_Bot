import const
import youtube_dl

from debug import dprint
from discord import FFmpegPCMAudio, Game, PCMVolumeTransformer, Status, VoiceChannel
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
        dprint('Success!')

    @commands.Bot.event
    async def on_ready():
        dprint('Logged in as: {0}, {1}\n{2}'.format(bot.user.name, bot.user.id, const.DIVIDER))
        # Set the bot's status and activity (different with the rewritten Discord lib)
        await bot.change_presence(status=Status.online, 
            activity=Game(name="Literally Botting"))

    @commands.Bot.event
    async def on_message(message):
        # Messages sent by the bot are ignored
        if message.author == bot.user:
            return
        # Bot will response given these patterns in a message
        if message.content.lower() == "where is bryant?":
            await message.channel.send("Late.")
        # If a message does not match the above, attempt to parse as command
        await bot.process_commands(message)

    @commands.command()
    async def echo(ctx):
        await ctx.send(":wave: Hello there!")

    @commands.command()
    async def cat(ctx):
        await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

    @commands.command()
    async def sayit(self, ctx, *, channel: VoiceChannel):
        url = "https://www.youtube.com/watch?v=ZiE3aVQGf8o"

        if ctx.voice_client is not None:
            vc = await ctx.voice_client.move_to(channel)
        
        player = await YTDLSource.from_url(url, loop=self.bot.loop)
        ctx.voice_client.play(player, after=lambda e: print('Player error %s' % e) if e else None)
        await vtc.voice_client.disconnect()
