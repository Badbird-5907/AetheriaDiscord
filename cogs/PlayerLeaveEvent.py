import logging
import os

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


class PlayerLeaveEvent(commands.Cog):
    def __init__(self, client):
        self.client = client
    # Events#
    @commands.Cog.listener()
    async def on_ready(self):
        logger.info('Loaded player leave event cog!')

    @client.event
    async def on_member_leave(member):
        embed = discord.Embed(title="You left Aetheria Online... :cry:",
                              description="We're sorry to see you go", color=ERROR)
        embed.add_field(name=f"If you left by accident ", value="Join back at https://discord.gg/yfNYNkM", inline=False)
        embed.set_thumbnail(url=THUMBNAIL)
        await member.send(embed=embed)

def setup(client):
    client.add_cog(PlayerLeaveEvent(client))