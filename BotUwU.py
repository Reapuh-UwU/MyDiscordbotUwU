from urllib import response
import discord
import random
from pandas import describe_option
import requests
from discord.ext import commands
from ping3 import ping
import asyncio


TOKEN = ''
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!',case_insensitive=True,intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.remove_command('help')

#embed/help zone
@client.command()
async def help(message):
    embed = discord.Embed(
        title='commands?',
        description='This is the help section. Here are all the commands for me!', #continue me
        colour=discord.Colour(0xd88c54)
        )
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/944013283327893545/d15911188dda36091a1fc1813ef4263f.webp?size=2048')
    embed.add_field(
        name='!help',
        value='List all of the commands',
        inline=False
    )
    embed.add_field(
        name='!hello',
        value='Hello to the user',
        inline=False
    )
    embed.add_field(
        name='!rng',
        value='Gives a random number with the given range that the user gives. Example !rng 0 10',
        inline=False
    )
    embed.add_field(
        name='!ping',
        value='HA GET PONGED. I think you know this command is...',
        inline=False
    )
    embed.add_field(
        name='!mcstat',
        value='Gives the hostname, status, ip and a max and current player count',
        inline=False
    )
    embed.add_field(
        name='!xkcd',
        value='Sends a xkcd comic within a given number. Example: !xkcd 5',
        inline=False
    )
    embed.add_field(
        name='!rngxkcd',
        value='Sends a random xkcd comic',
        inline=False
    )

    await message.send(embed=embed)

#message commands/FUN COMMANDS!#
@client.command()
async def hello(message):

    username = message.author
    await message.send(f'Hello {username}!')

@client.command()
async def rng(message,number1,number2):
    number1 = (int(number1))
    number2 = (int(number2))
    result = random.randrange(number1,number2)
    response = (f'This is your random number: **``{result}``**!')
    await message.send(response)

@client.command()
async def ping(message):
    await message.send(f'HA! GET PONGED!!. heres your latency {round(client.latency * 1000)}ms') 

#MCstats#
@client.command()
async def mcstatus(message,IP):
    response = requests.get('https://api.mcsrvstat.us/2/'+IP)
    status = response.json()
    if status['online'] == True:
       x = 'Online'
    else:
        x = 'Offline'

    #turning things to string UwU
    player_online=str(status['players']['online'])
    player_max=str(status['players']['max'])
    player_ratio=player_online + '/' + player_max

    embed = discord.Embed(
        title='Minecraft server',
        colour=discord.Colour(0xd88c54)
    )
    embed.add_field(
        name='Minecraft Server IP',
        value=IP,
        inline=False
    )
    embed.add_field(
        name='Status',
        value=x,
        inline=False
    )
    embed.add_field(
        name='Player count',
        value=player_ratio,
        inline=False
    )
    await message.send(embed=embed)

#XKCD SECTIONS#
@client.command()
async def xkcd(message,number):
    response = requests.get('https://xkcd.com/'+number+'/info.0.json')
    status = response.json()
    await message.send(status['img'])

@client.command()
async def rngxkcd(message):
    rng = random.randrange(1,2582)
    response = requests.get('https://xkcd.com/'+str(rng)+'/info.0.json')
    status = response.json()
    await message.send(status['img'])

client.run(TOKEN)