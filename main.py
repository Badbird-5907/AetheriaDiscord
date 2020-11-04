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
INFO = 0x13cd5d
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
#TODO here

@load.error
async def load_error(self, ctx, error):
    error_embed = discord.Embed(title="Error!",
                                colour=ERROR)
    error_embed.set_author(name=f"{self.client.user.name}", icon_url=self.client.user.avatar_url)
    error_embed.set_footer(text=FOOTER)
    if isinstance(error, commands.CommandOnCooldown):
        error_embed.add_field(name=f"Information",
                              value=f"{ctx.author.mention}, you are on cooldown for this command!\nPlease try again later.")
    if isinstance(error, commands.NotOwner):
        error_embed.add_field(name=f"Information",
                              value=f"{ctx.author.mention}, you are need to be the bot owner to use this command.")
    if isinstance(error, commands.MissingRequiredArgument):
        error_embed.add_field(name=f"Information", value=f"{ctx.author.mention}, you are missing a required argument.")
    if isinstance(error, commands.MissingAnyRole):
        error_embed.add_field(name=f"Information",
                              value=f"{ctx.author.mention}, you are missing the required role(s) for this command.")
    if isinstance(error, commands.MissingRole):
        error_embed.add_field(name=f"Information",
                              value=f"{ctx.author.mention}, you are missing the required role(s) for this command.")
    if isinstance(error, commands.MissingPermissions):
        error_embed.add_field(name=f"Information",
                              value=f"{ctx.author.mention}, you are missing the required permission(s) for this command.")
    if isinstance(error, commands.BadArgument):
        error_embed.add_field(name=f"Information", value=f"{ctx.author.mention}, {error}")
    if isinstance(error, commands.ExtensionNotFound):
        error_embed.add_field(name=f"Information", value=f"{ctx.author.mention}, the extension you provided does not exist!")

    await ctx.send(embed=error_embed)

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



@unload.error
async def unload_error(self, ctx, error):
    error_embed = discord.Embed(title="Error!",
                                colour=ERROR)
    error_embed.set_author(name=f"{self.client.user.name}", icon_url=self.client.user.avatar_url)
    error_embed.set_footer(text=FOOTER)
    if isinstance(error, commands.CommandOnCooldown):
        error_embed.add_field(name=f"Information",
                              value=f"{ctx.author.mention}, you are on cooldown for this command!\nPlease try again later.")
    if isinstance(error, commands.NotOwner):
        error_embed.add_field(name=f"Information",
                              value=f"{ctx.author.mention}, you are need to be the bot owner to use this command.")
    if isinstance(error, commands.MissingRequiredArgument):
        error_embed.add_field(name=f"Information", value=f"{ctx.author.mention}, you are missing a required argument.")
    if isinstance(error, commands.MissingAnyRole):
        error_embed.add_field(name=f"Information",
                              value=f"{ctx.author.mention}, you are missing the required role(s) for this command.")
    if isinstance(error, commands.MissingRole):
        error_embed.add_field(name=f"Information",
                              value=f"{ctx.author.mention}, you are missing the required role(s) for this command.")
    if isinstance(error, commands.MissingPermissions):
        error_embed.add_field(name=f"Information",
                              value=f"{ctx.author.mention}, you are missing the required permission(s) for this command.")
    if isinstance(error, commands.BadArgument):
        error_embed.add_field(name=f"Information", value=f"{ctx.author.mention}, {error}")
    if isinstance(error, commands.ExtensionNotFound):
        error_embed.add_field(name=f"Information", value=f"{ctx.author.mention}, the extension you provided does not exist!")

    await ctx.send(embed=error_embed)

for filename in listdir("./cogs"):
    if filename != "information.py":
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

    statuses = ["-help", "The Aetheria Online Discord"]

    while not client.is_closed():
        status = random.choice(statuses)

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        await asyncio.sleep(20)
client.loop.create_task(update_presence())
if __name__ == "__main__":
    client.run(token)
