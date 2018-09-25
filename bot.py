import discord
from discord.ext import commands

import os

BOT_PREFIX = os.environ['prefix']
TOKEN = os.environ['token']

DIVIDER = "--------------------------------------------------------------------------------"

bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
	print('Logged in as: {0}#{1}\n{2}'.format(bot.user.name, bot.user.id, DIVIDER))
	# Set the bot's status and activity (different with the rewritten Discord lib)
	await bot.change_presence(status=discord.Status.online, 
		activity=discord.Game(name="Literally Botting"))

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	if message.content.lower() == "where is bryant?":
		await message.channel.send("Late.")

	await bot.process_commands(message)

@bot.command()
async def greet(ctx):
	await ctx.send(":wave: Hello there!")

@bot.command()
async def cat(ctx):
	await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

bot.run(TOKEN)