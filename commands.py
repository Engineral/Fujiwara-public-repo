import discord as dpy
import random
from datetime import *

token = 'nul'   # Replace nul with corresponding token
prefix = '+'

intents = dpy.Intents.default()
intents.message_content = True

bot = dpy.Client(intents=intents)   # 'bot' substitutes for 'client'


@bot.event
async def on_ready():
    ping = str(datetime.now())
    print(ping[0:19], f'We have logged in as {bot.user}')

    channel = bot.get_channel(1092234344535445534)
    await channel.send('**おはよございます**\nFujiwara-Chan, signing on!')

"""
@bot.event
async def on_connect():
    channel = bot.get_channel(1092234344535445534)
    await channel.send('**おはよございます**\nFujiwara-Chan, signing on!')
    print(datetime.now(), f'{bot.user} is now appearing online')
"""

# Commands (not to be confused with @bot.commands)
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    """
    Prefix: +
    Commands:
        help - lists all commands
        call - response
        coinflip - flips a coin
    """
    
    if message.content.startswith(f'{prefix}help'):
        await message.channel.send(embed=dpy.Embed(title='Commands', description='List of Fujiwara Commands\n\nhelp - lists all commands\ncall - response\ncoinflip - flips a coin', color=0x00ff00))

    if message.content.startswith(f'{prefix}call'):
        print('  Cmd Called:   \'+call\'\nCmd Response:   \'response\'')

        await message.channel.send('response')
    
    if message.content.startswith(f'{prefix}coinflip'):
        rng = random.randint(0,1)

        coin = 'nul'
        if rng == 0:
            coin = 'Heads'
        elif rng == 1:
            coin = 'Tails'
        else:
            coin = 'nul'

        await message.channel.send(coin)

@bot.event
async def on_disconnect():
    ping = str(datetime.now())
    print(ping[0:19], f'{bot.user} has disconnected')

    channel = bot.get_channel(1092234344535445534)
    await channel.send('**おやすみなさい**\nFujiwara-Chan, signing off!')

bot.run(token)