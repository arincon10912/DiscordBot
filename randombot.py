#!/usr/bin/env python3

import discord
import random
from discord.ext import commands
import os

from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()  # create an Intents object
intents.members = True  # enable the Members intent, so you can access member events
intents.message_content = True
client = discord.Client(intents=intents)  # create a Client object with the Intents object


commands = {
    '!hello': 'Say hello to the bot',
    '!flipCoin': 'Flip a coin and get heads or tails',
    '!genNum': 'Generate a random number between 1 and 100',
    '!randomUser': 'Get a random user from the server',
    '!help': 'Get a list of available bot commands'
}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        command_list = '\n'.join([f'{command}: {description}' for command, description in commands.items()])
        help_message = f'Here are the available commands:\n{command_list}'
        await message.channel.send(help_message)

@client.event
async def on_message(message):
    print(message.content)
    #Flip Coin
    if message.content == '!coin':
        result = random.choice(['heads', 'tails'])
        await message.channel.send(result)
    #Generate Number 1-100
    elif message.content == '!genNum':
        result = random.randint(1, 100)
        await message.channel.send(result)
    elif message.content == '!randomUser':
        guild = message.guild
        members = guild.members
        random_member = random.choice(members)
        await message.channel.send(random_member.mention)

print(os.getenv('TOKEN2'))
client.run(os.getenv('TOKEN2'))