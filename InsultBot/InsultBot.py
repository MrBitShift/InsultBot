import discord

TOKEN_FILE = "./token.txt"

def get_token():
	try:
		return open(TOKEN_FILE).read()
	except:
		raise FileNotFoundError("Could not find \"{}\"".format(TOKEN_FILE))

class MyClient(discord.Client):
	async def on_ready(self):
		print("Logged on as: ", self.user)

	async def on_message(self, message):
		if (message.author == self.user):
			return

		if message.content.startswith(".insultbot"):
			await message.channel.send("I'm here!")

client = MyClient()
client.run(get_token())