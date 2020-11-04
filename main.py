import discord
from os import path, listdir    # Used to check config location + listdir for auto cog loading
import datetime # Used for logging
from discord.ext import commands, tasks
from configparser import ConfigParser   # Used for updating and creating config
import random
import asyncio
import logging
import coloredlogs
import json

client = discord.Client()
with open('token.txt', 'r') as file:
    data = file.read().replace('\n', '')
token = data
FOOTER =  "Aetheria Online Bot | Coded By <@456951144166457345>"
# Colours for embeds
THUMBNAIL = "https://cdn.discordapp.com/attachments/722091896931090575/759794463307726848/9c2a9f40100d08147c6b6fb8166a4799.png"
INFO = 0x5d13cd
WARN = 0x8959fb
ERROR = 0x2a0e7b

logger = logging.getLogger(__name__)
fmt = ("%(asctime)s - %(message)s")
coloredlogs.install(fmt=fmt, logger=logger)


client = commands.Bot(command_prefix="-")
client.remove_command('help')
config = ConfigParser()
# Constants
LOG_LOCATION = 'logs/main.log'
@client.event
async def on_ready():
    print ("--------------------------------------------------------------")
    print ("Discord API version:")
    print (discord.version_info)
    print('Logged in as {0.user}'.format(client))
    print ("Token: " + token)
    print ("--------------------------------------------------------------")

@client.event
async def on_connect():
    logger.info(f"Connected to discord as: {client.user.name} ({client.user.id})!")
    with open(LOG_LOCATION, "a+") as main_log:
        main_log.write(f"[{datetime.datetime.now()}]: connected to discord as: "
                       f"{client.user.name} ({client.user.id})!\n")
        main_log.close()


@client.event
async def on_disconnect():
    logger.warning("Disconnected!")
    with open(LOG_LOCATION, "a+") as main_log:
        main_log.write(f"[{datetime.datetime.now()}]: disconnected!\n")
        main_log.close()

# Ping Command
@client.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: Pong! {round(client.latency * 1000)}ms')

async def update_presence():
    await client.wait_until_ready()

    statuses = ["-help", "kek"]

    while not client.is_closed():
        status = random.choice(statuses)

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        await asyncio.sleep(20)
client.loop.create_task(update_presence())
if __name__ == "__main__":
    client.run(token)
