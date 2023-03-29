import discord
from discord.ext import commands
from discord.flags import Intents
from discord import FFmpegPCMAudio

intents = discord.Intents.all()
client = commands.Bot(command_prefix="$", intents= intents)

@client.command(pass_context = True)
async def radiostg(ctx):
    if (ctx.author.voice):
        await ctx.send("Rádio Santiago Online na call ou pelo link https://www.radiosantiago.com.br/player/")
        
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('')
        player = voice.play(source)

    else:
        await ctx.send("Entre num voice pls.")

@client.command(pass_context = True)
async def radiostgoff(ctx):
    if (ctx.voice_client):

        await ctx.guild.voice_client.disconnect()
        await ctx.send("Obrigado por ouvir a rádio da Terra dos Poetas")

    else:
        await ctx.send("ta maluco pae")

@client.event
async def on_ready():
    print("O Bot foi ligado. Dale gremio!")

client.run('MTA4MzA1NzU0NjcyNzc5MjY5MQ.GKOsvF.5b9dPLv6I1xP0MjCjCJmDBt62Pz_NEAxSDeWcM')