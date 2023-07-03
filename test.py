# This file is not to be pushed outside this branch; what follows is documentation explaining each component of test.py


# The following imports the 'discord.py' API
import discord


# The following is not from the example documentation. Instead, this is me making the token usage more convenient.
token = 'nul'   # Replace nul with corresponding token


# Intents =
# ... what this does ...
intents = discord.Intents.default()
intents.message_content = True


# Client = Fujiwara
# ... what this does ...
client = discord.Client(intents=intents)



### @client.event (unknown)
# This outputs in the terminal when this file has been successfully activated
# Client, the object, is initialized earlier via 'discord.py/discord/client.py'
# User, the object property, is, for lack of better description, the name (string value) of the client.
# Client (App)  ;  User (Bot)
# Fujiwara  ;  Fujiwara#5065 (or whatever the discriminator is)
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# This is where the commands are triggered via C&R. It's essentially a bunch of if-statements depending on what is said. This specific @client.event instance awaits for messages to be typed, reads what they say, and then initiates the code based on the outcome.
# 'Call & Response' (C&R) Command
# Default Prefix: $
# Input: '$hello'
# Output: "Hello!"
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


# This is where the token goes so that the bot can run. If the token is not present, the bot will not run.
client.run(token)