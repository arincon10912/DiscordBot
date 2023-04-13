import discord
import os

intents = discord.Intents.default()  # create an Intents object
intents.members = True  # enable the Members intent, so you can access member events

client = discord.Client(intents=intents)  # create a Client object with the Intents object

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTA5NjEyMjIzNDMzNjE5NDY4Mg.G8AOlb.YB5NLzShce_fhevK_dG8u4Fume8YxaTuhb73v0')