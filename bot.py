import discord
from discord.ext import commands
from discord.ext.commands import Bot
from config import *
import asyncio
from time import gmtime, strftime

client = Bot(command_prefix=Command_Prefix)


@client.event
async def on_start():
    if Command_Prefix is None:
        client.command_prefix = '!'
    if Token is None:
        print("ERROR: No token inserted")
        await asyncio.sleep(1)
        client.close()
    else:
        return


async def game(channel, author):
    await client.send_message(channel, "Want me to send the questions via private messages?")
    message1 = await client.wait_for_message(author=author, channel=channel)
    if message1 is "Yes" or "yes":
        private_state = True
    else:
        private_state = False
    await client.send_message(channel, "Tag who's playing")
    players_list = await client.wait_for_message(author=author, channel=channel)
    print(players_list.content)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.contains.mention:

    if message.content.startswith("Hey Kalux") or message.content.startswith("hey kalux") or message.content.startswith("hey Kalux") or message.content.startswith("Hey kalux"):
        await client.send_message(message.channel, "Hey, Wanna play a game?")
        question1 = True
        while question1 is True:
            answer = await client.wait_for_message(author=message.author, channel=message.channel)
            if answer.content.startswith("Yes") or answer.content.startswith("yes"):
                await client.send_message(message.channel, "So be it.")
                question1 = False
                # await game(message.channel, message.author)
            if answer.content.startswith("No") or answer.content.startswith("no"):
                await client.send_message(message.channel, "See you later then.")
                question1 = False
            if question1 is True:
                await client.send_message(message.channel, "Hey, Wanna play a game?")

    else:
        client.process_commands(message)


@client.event
async def on_ready():
    print("@INFO: Logging Successful.")
    await asyncio.sleep(1)
    time = strftime("%H:%M:%S of %d-%m-%Y", gmtime())
    print("@INFO: Logged at: " + time)
    await asyncio.sleep(1)
    print("@INFO: Username: " + client.user.name + ".")
    await asyncio.sleep(1)
    print("@INFO: ID: " + client.user.id + ".")
    await client.change_presence(game=discord.Game(name=Presence))


client.run(Token)
