import discord
from discord.ext import commands

class MyBot(discord.Client):
    intents = discord.Intents.all()
    client = commands.Bot(command_prefix="$", intents= intents)

    async def on_ready(self):

        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):

        print('Message from {0.author}: {0.content}'.format(message))

        if message.content == '?radiostg':
            await message.channel.send(
                f"{message.author.name} o link da rádio é: https://www.radiosantiago.com.br/player/"
                )

client = MyBot(intents=discord.Intents.all())
client.run('MTA4MzA1NzU0NjcyNzc5MjY5MQ.GKOsvF.5b9dPLv6I1xP0MjCjCJmDBt62Pz_NEAxSDeWcM')