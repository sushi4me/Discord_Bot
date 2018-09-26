"""
giphy.py:
A random gif-generator!
"""

# Import statements
import inspect

from discord import File
from discord.ext import commands
from random import choice


class Giphy:
    def __init__(self, server_bot):
        self.server_bot = server_bot
        self.voice_state = {}
        #self.session = server_bot.session
        #self.giphy_api_key = server_bot.giphy_api_key
        self.get_random_gif = 'https://api.giphy.com/v1/gifs/random'
        self.get_searched_gif = 'https://api.giphy.com/v1/gifs/search'
        self.get_trending_gif = 'https://api.giphy.com/v1/gifs/trending'

    async def get(self, url: str, params: dict):
        async with self.session.get(url, params=params) as response:
            if response.status is 200:
                return await response.json()
            else:
                return False

    @commands.command(name="test_gif")
    async def _test_gif(self, ctx):
        # Initialize an empty list
        files_list = list()

        # Send content
        attachment = "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif"

        # Add Giphy badge
        giphy_badge = File("./media/powered_by_giphy_vert_100.png")
        files_list.append(giphy_badge)

        # Send the files list
        await ctx.send(content=attachment, files=files_list)
    """
    @commands.command()
    async def gif(self, ctx):
        params = {
            'api_key': self.giphy_api_key
        }

        random_results = await self.get(self.get_random_gif, params)
        await ctx.send(random_results['data']['image_original_url'])

    @commands.command()
    async def search(self, ctx, *, query):
        params = {
            'api_key': self.giphy_api_key,
            'q': query,
            'limit': '100',
            'offset': '0',
            'rating': 'R',
            'lang': 'en'
        }

        search_results = await self.get(self.get_searched_gif, params)
        values = [v for results in search_results['data']
                  for k, v in results.items() if k == 'url']
        url = choice(values)
        await ctx.send(url)

    @commands.command()
    async def trending(self, ctx):
        params = {
            'api_key': self.giphy_api_key,
            'limit': '100',
            'rating': 'R',
        }

        trending_results = await self.get(self.get_trending_gif, params)
        values = [v for results in trending_results['data']
                  for k, v in results.items() if k == 'url']
        url = choice(values)
        await ctx.send(url)
    """

# Necessary for cogs
def setup(server_bot):
    server_bot.add_cog(Giphy(server_bot))