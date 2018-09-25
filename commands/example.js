const Discord = require('discord.js')

module.exports.run = async(bot, message, args) => {
	// Code for command
	await message.delete()
	return message.reply("Hi! I am the example command.").then(m => m.delete(10000))
}

module.exports.help = {
	name: "example"
}