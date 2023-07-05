import discord as dpy
from datetime import *

token = 'nul'   # Replace nul with corresponding token
prefix = '&'

intents = dpy.Intents.default()
intents.message_content = True

bot = dpy.Client(intents=intents)   # 'bot' substitutes for 'client'

try:
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

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
    
        if message.content.startswith(f'{prefix}call'):
            print('  Cmd Called:   \'+call\'\nCmd Response:   \'response\'')

            await message.channel.send('response')
except KeyboardInterrupt:
    ping = str(datetime.now())
    print(ping[0:19], f'{bot.user} has disconnected')

    # channel = bot.get_channel(1092234344535445534)
    # channel.send('**おやすみなさい**\nFujiwara-Chan, signing off!')

# @bot.event
# async def on_disconnect():
#     ping = str(datetime.now())
#     print(ping[0:19], f'{bot.user} has disconnected')

#     channel = bot.get_channel(1092234344535445534)
#     await channel.send('**おやすみなさい**\nFujiwara-Chan, signing off!')

bot.run(token)