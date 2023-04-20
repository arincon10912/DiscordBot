#!/usr/bin/env python3

import discord
from discord.ext import commands
import os
from googletrans import Translator, constants
from pprint import pprint

from dotenv import load_dotenv

load_dotenv()
translator = Translator() # Google Translate API

intents = discord.Intents.default()  # create an Intents object
intents.members = True  # enable the Members intent, so you can access member events
intents.message_content = True
client = discord.Client(intents=intents)  # create a Client object with the Intents object

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# defaults to english translation
@client.event
async def on_message(message):
    global translation
    if message.content.startswith('$'):
        dest_language = message.content[1:3]
        translation = translator.translate(message.content[3:], dest=dest_language) 
        await message.channel.send(f'{translation.origin} ({translation.src}) --> {translation.text} ({dest_language})')

    if message.content == '!pronounce':
        await message.channel.send(translation.text, tts = True)

print(os.getenv('TOKEN'))
client.run(os.getenv('TOKEN'))