import discord as dpy
from datetime import *

token = 'nul'   # Replace nul with corresponding token

intents = dpy.Intents.default()
intents.message_content = True

bot = dpy.Client(intents=intents)   # 'bot' substitutes for 'client'

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

bot.run(token)

print(date.today())