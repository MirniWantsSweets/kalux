import discord
from discord.ext import commands
from config import *
import asyncio
from time import gmtime, strftime
with open('D:/Stuff/Python/Discord/questions.txt') as file:
    questions = [line.strip('\n') for line in file]
client = commands.Bot(command_prefix=Command_Prefix)

#async def game_message(status, question):
#    if status is True:


async def game_message(channel, user, question):
    if channel == user:
        await client.send_message(user, question)
    else:
        await client.send_message(channel, "<@" + user.id + "> " + question)



async def game(channel, author):
    print("@GAME: New game starts.")
    game_status = True
    await client.send_message(channel, "Want me to send the questions via private messages?")
    message1 = await client.wait_for_message(author=author, channel=channel)
    question1 = True
    while question1 is True:
        if message1.content.upper().startswith("YES"):
            private_status = True
            question1 = False
        if message1.content.upper().startswith("NO"):
            private_status = False
            question1 = False
        if question1 is True:
            await client.send_message("I didn't understand that one.")
    await client.send_message(channel, "Tag who's playing")
    message2 = await client.wait_for_message(author=author, channel=channel)
    players_list = message2.mentions
    msg = "So, "
    for x in players_list:
        msg = msg + "<@" + x.id + "> "
    msg = msg + "are the players that are playing."
    await client.send_message(channel, msg)
    while game_status is True:
        #get question function here
        if private_status is True:
            for x in players_list:
                await game_message(x, x, "potato")
        else:
            for x in players_list:
                await game_message(channel, x, "potato")
        game_status = False
        print("@GAME: A game has finished.")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.upper().startswith("KALUX GOT MY TONGUE") and str(message.author.id) == Owner_ID:
        await client.send_message(message.channel, "Gonna take a nap.")
        await client.close()
    if message.content.upper().startswith("KALUX GOT MY TONGUE") and str(message.author.id) != Owner_ID:
        await client.send_message(message.channel, "You don't have the power to make me stop.")
    if message.content.upper().startswith("HEY KALUX"):
        await client.send_message(message.channel, "Hey, Wanna play a game?")
        question1 = True
        while question1 is True:
            answer = await client.wait_for_message(author=message.author, channel=message.channel)
            if answer.content.upper().startswith("YES"):
                await client.send_message(message.channel, "So be it.")
                question1 = False
                await game(message.channel, message.author)
            if answer.content.upper().startswith("NO"):
                await client.send_message(message.channel, "See you later then.")
                question1 = False
            if question1 is True:
                await client.send_message(message.channel, "I didn't understand that one.")
    await client.process_commands(message=message)


@client.command()
async def cookie():
    await client.say(":cookie:")


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
    await client.change_presence(game=discord.Game(name=Status))


'''@client.event
async def on_start():
    if Command_Prefix is None or Token is None or Owner_ID is None or Presence is None:
        if Command_Prefix is None:
            client.command_prefix = '!'
            print("@INFO: No Prefix is defined, setting prefix to '!'.")
        if Token is None:
            print("@ERROR: No token inserted.")
            await asyncio.sleep(1)
            client.close()
        if Owner_ID is None:
            print("@ERROR: No Owner_ID is defined.")
            await asyncio.sleep(1)
            client.close()
    else:'''

client.run(Token)
