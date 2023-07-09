import commands as cmds
import discord
from discord.ext import commands
from datetime import *
import math
import random as RNG
import time

token = 'nul'   # Replace nul with corresponding token
prefix = '+'

intents = discord.Intents.default()
intents.message_content = True

# client = discord.Client(intents=intents)   # 'bot' substitutes for 'client' --- OUTDATED???
bot = commands.Bot(command_prefix='+', intents=intents)



@bot.event
async def on_ready():
    ping = str(datetime.now())
    print(ping[0:19], f'We have logged in as {bot.user}')

    channel = bot.get_channel(1093371204125065337)
    await channel.send('**おはよございます**\nFujiwara-Chan, signing on!')

"""
@bot.event
async def on_connect():
    channel = bot.get_channel(1092234344535445534)
    await channel.send('**おはよございます**\nFujiwara-Chan, signing on!')
    print(datetime.now(), f'{bot.user} is now appearing online')
"""

"""
# Commands (not to be confused with @bot.commands)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    
    # Prefix: +
    # Commands:
    #     help - lists all commands
    #     call - response
    #     coin - flips a coin
    
    
    if message.content.startswith(f'{prefix}help'):
        await message.channel.send(embed=discord.Embed(title='Commands', description='List of Fujiwara Commands\n\nhelp - lists all commands\ncall - response\ncoin - flips a coin', color=0x00ff00))

    if message.content.startswith(f'{prefix}call'):
        print('  Cmd Called:   \'+call\'\nCmd Response:   \'response\'')

        await message.channel.send('response')
    
    if message.content.startswith(f'{prefix}coin'):
        # outcome = cmds.coin()
        outcome = RNG.choice(['Heads', 'Tails'])
        await message.channel.send(f'`{outcome}`')
    
    if message.content.startswith(f'{prefix}ping'):
        ti = datetime.now()
        await message.channel.send(f'{ti[0:19]}')
"""

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

"""
@bot.command()
async def roll(ctx, dice: str):
    # Rolls a dice in NdN format.
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(RNG.randint(1, limit)) for r in range(rolls))
    await ctx.send(f'`{result}`')
"""

# bot.add_command(test)

"""
@client.event
async def on_disconnect():
    ping = str(datetime.now())
    print(ping[0:19], f'{client.user} has disconnected')

    channel = client.get_channel(1092234344535445534)
    await channel.send('**おやすみなさい**\nFujiwara-Chan, signing off!')
"""

bot.run(token)