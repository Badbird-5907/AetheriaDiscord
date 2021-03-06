import asyncio
import datetime  # Used for logging
import logging
import random
from configparser import ConfigParser  # Used for updating and creating config
from os import listdir  # Used to check config location + listdir for auto cog loading

import coloredlogs
import discord
from discord.ext import commands

client = discord.Client()
with open('token.txt', 'r') as file:
    data = file.read().replace('\n', '')
token = data
FOOTER =  "Aetheria Online Bot | Coded By <@456951144166457345>"
# Colours for embeds
THUMBNAIL = "https://cdn.discordapp.com/attachments/722091896931090575/759794463307726848/9c2a9f40100d08147c6b6fb8166a4799.png"
INFO = 0x13cd5d
WARN = 0xFFB100
ERROR = 0xFF2D00

logger = logging.getLogger(__name__)
fmt = ("%(asctime)s - %(message)s")
coloredlogs.install(fmt=fmt, logger=logger)


client = commands.Bot(command_prefix=commands.when_mentioned_or("-"))
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
    
# COG LOADING
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    logger.warning(f"{ctx.message.author.name} ({ctx.message.author.id}) loaded {extension}!")
    embed = discord.Embed(title=f"Successfully Loaded {extension}!", color=INFO)
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.set_footer(text=FOOTER)
    await ctx.send(embed=embed)

# COG UNLOADING
@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    logger.warning(f"{ctx.message.author.name} ({ctx.message.author.id}) unloaded {extension}!")
    embed = discord.Embed(title=f"Successfully Unloaded {extension}!", color=INFO)
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.set_footer(text=FOOTER)
    await ctx.send(embed=embed)

for filename in listdir("./cogs"):
    try:
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")
            logger.info(f"Loading {filename[:-3]}")
            with open(LOG_LOCATION, "a+") as main_log:
                main_log.write(f"[{datetime.datetime.now()}]: loaded {filename[:-3]}!\n")
                main_log.close()
    except Exception as e:
        logger.critical(e)

async def update_presence():
    await client.wait_until_ready()

    statuses = ["-help", "The Aetheria Online Discord", "aetheria.world"]

    while not client.is_closed():
        status = random.choice(statuses)

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        await asyncio.sleep(20)
client.loop.create_task(update_presence())
if __name__ == "__main__":
    client.run(token)
