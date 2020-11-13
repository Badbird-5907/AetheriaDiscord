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

class INFORMATION(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events#
    @commands.Cog.listener()
    async def on_ready(self):
        logger.info('Loaded information cog!')
    @commands.command()
    async def help(self,ctx):
        embed=discord.Embed(title="Help Menu", description="test", color=INFO)
        embed.add_field(name=f"-info", value="More Info", inline=False)
        embed.add_field(name=f"-ping", value="ping", inline=False)
        embed.set_thumbnail(url=THUMBNAIL)
        embed.set_footer(text=FOOTER)
        await ctx.channel.send(embed=embed)
    @commands.command()
    async def info(self, ctx):
        embed=discord.Embed(title="Info", description="Additonal details related to this bot.", color=INFO)
        embed.add_field(name="Author", value="<@456951144166457345>", inline=False)
        embed.add_field(name="Server Invite", value="<https://discord.gg/yfNYNkM>", inline=False)
        embed.set_thumbnail(url=THUMBNAIL)
        embed.set_footer(text=FOOTER)
        await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(INFORMATION(client))
