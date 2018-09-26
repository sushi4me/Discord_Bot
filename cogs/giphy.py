import aiohttp
from discord.ext import commands
from random import choice


class Giphy:
    def __init__(self, server_bot):
        self.server_bot = server_bot
        #self.session = server_bot.session
        #self.giphy_api_key = server_bot.giphy_api_key
        self.get_random_gif = 'https://api.giphy.com/v1/gifs/random'
        self.get_searched_gif = 'https://api.giphy.com/v1/gifs/search'
        self.get_trending_gif = 'https://api.giphy.com/v1/gifs/trending'

    async def get(self, url: str, params: dict):
        """get(self, url, params)
        A function that makes a request to a server, and checks the
        status code and returns the response content.
        """

        async with self.session.get(url, params=params) as response:
            if response.status is 200:
                return await response.json()
            else:
                return False

    @commands.command(name="test_gif")
    async def _test_gif(self, ctx):
        """
        Testing command for gif sending.
        """

        await ctx.send_file(self.server_bot.get_channel(ctx.message.author.id), "../media/PoweredByGiphyBadge.gif")

    @commands.command()
    async def gif(self, ctx):
        """*gif
        A command that will return a random .gif.
        """

        params = {
            'api_key': self.giphy_api_key
        }

        random_results = await self.get(self.get_random_gif, params)
        await ctx.send(random_results['data']['image_original_url'])

    @commands.command()
    async def search(self, ctx, *, query):
        """*search <query>
        A command that will return a random .gif that matches the search query.
        """

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
        """*trending
        A command that will return a random .gif from the trending page of Giphy.
        """

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


def setup(server_bot):
    server_bot.add_cog(Giphy(server_bot))