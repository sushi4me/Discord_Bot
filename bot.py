import discord
from discord.ext import commands

import os

access_token = os.environ["token"]

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message(mesage):
	if message.author == client.user:
		return

	if message.content.startswith('!hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)

@bot.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('----------')

bot.run(access_token)