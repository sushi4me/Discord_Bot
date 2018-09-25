import discord
from discord.ext import commands

import os

BOT_PREFIX = os.environ['prefix']
TOKEN = os.environ["token"]

bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('----------')
	await bot.change_presence(game=discord.Game(name="Literally Botting"))

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	if message.content.lower() == "where is bryant?":
		await bot.send_message(message.channel, "Late.")

@bot.command()
async def greet(ctx):
	await ctx.send(":wave: Hello there!")

@bot.command()
async def cat(ctx):
	await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

bot.run(TOKEN)