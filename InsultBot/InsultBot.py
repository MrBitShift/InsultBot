import discord
import re
import random

TOKEN_FILE = "./Token.txt"
INSULT_FILE = "./Insults.txt"

insults = None
try:
	insults = open(INSULT_FILE).read().strip().split("\n")
except FileNotFoundError:
	raise FileNotFoundError("Could not open {}".format(INSULT_FILE))

class InsultBotClient(discord.Client):
	mention_regex = re.compile(r"^\\*<@[!]?[0-9]+>$")

	def get_token():
		try:
			return open(TOKEN_FILE).read().strip()
		except:
			raise FileNotFoundError("Could not find \"{}\"".format(TOKEN_FILE))

	def get_insult(user_mention):
		return random.choice(insults).format(user_mention)

	async def on_ready(self):
		print("Logged on as: ", self.user)

	async def on_message(self, message):
		if (message.author == self.user):
			return

		if message.content.startswith(".insultbot"):
			print("Received message: \"" + message.content + "\"")

			arguments = message.content.split(" ")[1:]
			print("Arguments: " + str(arguments))

			if (len(arguments) == 1 and InsultBotClient.mention_regex.match(arguments[0])):
				await message.channel.send(InsultBotClient.get_insult(arguments[0]))

client = InsultBotClient()
client.run(InsultBotClient.get_token())