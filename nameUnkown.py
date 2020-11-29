import discord
import getGif
import re

discordKey = open('info/discordKeys.txt', 'r')
TOKEN = discordKey.readline()


## MyClient inherets from discord.Client
class MyClient(discord.Client):

	## code that runs when the bot is ready
	## similar to __init__ but better in this case
	async def on_ready(self):

		self.commands = {"commands": [], "query":[], "on_mention":[], "off_mention":[]}

		commandSetup = open("info/botInfo.txt", "r")

		n = 0
		keys = list(self.commands.keys())
		for line in commandSetup:
			self.commands[keys[n]].append(line[0:len(line) - 1])
			n += 1
			if n == 4:
				n = 0


		print('Logged on as', self.user)
		
	async def on_message(self, message):
       

		# don't respond to ourselves
		if message.author == self.user:

			return
		
		if message.content.startswith(">help"):

			embed=discord.Embed(title="Welcome to Ebisu", description="this is a clone of a bot made by a former anime memes mod, unfortunately this clone is not perfect so please report any issues to the mods.", color=0x66ff00)
			embed.set_thumbnail(url="https://i.pinimg.com/736x/1c/49/b2/1c49b26da7990363327aa36567f2d912.jpg")
			embed.add_field(name="commands", value="\>sad \n>happy\n>sip\n>angry\n>hug", inline=True)
			await message.channel.send(embed=embed)
			return

		## loop through our set commands
		for i in range(len(self.commands["commands"])):

			## if we hit one we hit one
			if message.content.startswith(self.commands["commands"][i]):

				##same as below, furture, wrap in func
				query = self.commands["query"][i]
				link, _ = getGif.getGif(query)

				result = re.search('<@(.*)>', message.content)

				if link:

					if result:
						user = result.group(1) 
						embedVar = discord.Embed(description=self.commands["on_mention"][i].format(author=message.author.id, user=user), color=0x00ffff)
					else:
						embedVar = discord.Embed(description=self.commands["off_mention"][i].format(author=message.author.id), color=0x00ffff)
					
					embedVar.set_image(url=link)

					await message.channel.send(embed=embedVar)
					return

				else:

					await message.channel.send("No <3")
					return		


		if message.content.lower()[0] == ">": 


			query = message.content.lower().split(" ")[0][1:]

			if len(query) > 2:
				link, conf = getGif.getGif(query)

				# // [text](url)
				# [u/USERNAME](https://www.reddit.com/user/HeyImLuna20)

				if link:
					embedVar = discord.Embed(description="**Heres you gif!**", color=0x00ffff)
					embedVar.set_image(url=link)

					await message.channel.send(embed=embedVar)
				else:

					await message.channel.send("I'm only {}%, confident, so i think i'll pass to save the embarrassment ".format(conf/2))		

client = MyClient()
client.run(TOKEN)
