import discord
from discord.ext import commands
from discord.flags import Intents
from discord import FFmpegPCMAudio
from discord.ext.commands import Bot

intents = discord.Intents.all()
client = commands.Bot(command_prefix="$", intents= intents)

@client.command(aliases=['radiostg', 'rstg'])
async def play(ctx, url: str = 'https://streamssl.hospedandosites.com.br/h52izize.php/;'):
    channel = ctx.message.author.voice.channel
    global player
    try:
        player = await channel.connect()
    except:
        pass
    player.play(FFmpegPCMAudio('https://streamssl.hospedandosites.com.br/h52izize.php/;'))
    await ctx.send(
        """
        ### Programação Rádio Santiago Segunda a Sexta ###
5h às 6h30min - Amanhecer Nos Pampas - Luiz Fernando Rocha
6h30min às 6h45min - Oração do Trabalhador - Igreja do Evangelho Quadrangular/Riachuelo
06h45min às 07h - Uma Luz Em Seu Caminho - Paróquia Nossa Senhora da Conceição
07h às 08h - Terra Nativa - Luiz Fernando Rocha
08h às 08h10min - Correspondente Gaúcha - Rede Gaúcha Sat
08h10min às 09h55min - Olho Vivo - Jones Diniz
10h às 11h25min - Santiago Atualidade - Paulo Pinheiro
11h25 às 11h45min - De Bem com a Vida - Ieda Beltrão
11h45min às 12h - Atualidade Esportes - Sérgio Ramos
12h15min - Jornal falado - Jones Diniz e Paulo Pinheiro
12h50min às 13h - Correspondente Gaúcha - Rede Gaúcha Sat
13h às 13h20min - Palavras Amigas - Igreja Missionária Cristo Está Voltando
13h20min às 14h - Santiago Movimenta - Paulo Pinheiro
14h às 15h - Tá em casa - Ieda Beltrão
15h às 16h -  Baita Chão - Marco Antônio Nunes
16h às 17h -  Pátria e Querência - Marco Antônio Nunes e Luiz Fernando Rocha
17h às 18h -  Buenas Tarde meu Santiago (1º parte) - Marco Antônio Nunes
17h55min às 18h - Oração da Ave Maria - Paróquia Nossa Senhora da Conceição
18h às 18h45min - Buenas Tarde meu Santiago (2º parte) - Marco Antônio Nunes
18h50min às 19h - Correspondente Gaúcha - Rede Gaúcha Sat
19h às 20h - A Voz do Brasil - EBC Serviços
20h às 20h10min - Correspondente Gaúcha - Rede Gaúcha Sat
20h10min às 22h - Clube do Ouvinte - Jorge Augusto Gonçalves
22h às 5h - Rede Gaúcha Sat 
        """
    )

@client.command(pass_context = True)
async def rstgoff(ctx):
    if (ctx.voice_client):

        await ctx.guild.voice_client.disconnect()
        await ctx.send("Obrigado por ouvir a rádio da Terra dos Poetas")

    else:
        await ctx.send("ta maluco pae")

@client.event
async def on_ready():
    print("O Bot foi ligado. Dale gremio!")

client.run('MTA4MzA1NzU0NjcyNzc5MjY5MQ.GKOsvF.5b9dPLv6I1xP0MjCjCJmDBt62Pz_NEAxSDeWcM')