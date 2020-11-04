import logging

import coloredlogs
import discord
from discord.ext import commands

logger = logging.getLogger(__name__)
fmt = ("%(asctime)s - %(message)s")
coloredlogs.install(fmt=fmt, logger=logger)

client = discord.Client()
with open('./token.txt', 'r') as file:
    data = file.read().replace('\n', '')
token = data
FOOTER =  "Aetheria Online Bot | Coded By Badbird5907#7139"

THUMBNAIL = "https://cdn.discordapp.com/attachments/722091896931090575/759794463307726848/9c2a9f40100d08147c6b6fb8166a4799.png"
INFO = 0x13cd5d
WARN = 0xFFB100
ERROR = 0xFF2D00
COG_LOG_LOCATION = "./logs/cog_information.log"
class shutdown(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events#
    @commands.Cog.listener()
    async def on_ready(self):
        logger.info('Loaded information cog!')

    @commands.command()
    async def shutdown(self, ctx):
        if ctx.author.id == 456951144166457345:
            embed = discord.Embed(title="Shutting down...", description="Goodbye!",color=ERROR)
            await ctx.channel.send(embed=embed)
            await client.close()
            await exit(1)
        else:
            embed = discord.Embed(title="Error", description="You are not whitelisted for this command!", color=ERROR)
            await ctx.channel.send(embed=embed)
def setup(client):
    client.add_cog(shutdown(client))