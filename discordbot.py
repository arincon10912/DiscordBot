import discord
from discord.ext import commands
import os

from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()  # create an Intents object
intents.members = True  # enable the Members intent, so you can access member events
intents.message_content = True
client = discord.Client(intents=intents)  # create a Client object with the Intents object

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# async def on_message(message):
#     if message.content == '$hello':
#         await message.channel.send('hello')


@client.event
async def on_message(message):
#     if message.author == client.user: // not the bot ??
#         return
    print(message.content)
    if message.content.startswith('$'):
        await message.channel.send('Hello!')


print(os.getenv('TOKEN'))
client.run(os.getenv('TOKEN'))
