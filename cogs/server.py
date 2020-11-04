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

class server(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events#
    @commands.Cog.listener()
    async def on_ready(self):
        logger.info('Loaded information cog!')
    @commands.command()
    async def serverinfo(self, ctx):
        #Badbird5907, Dwagon, Badbird ALT, tuck, pylons, noah
        if ctx.author.id == 456951144166457345 or 287696585142304769 or 467016253417193472 or 251556377284050946 or 136587043164782593 or 330017448382169088:
            embed = discord.Embed(title="Welcome to the Aetheria Online Discord!!!",
                                  description="Here is some information you might need!", color=INFO)
            embed.set_thumbnail(url=THUMBNAIL)
            await ctx.channel.send(embed=embed)

            embed = discord.Embed(title="Server IPs", description="The IPs you need to connect to the server!",
                                  color=INFO)
            embed.add_field(name=f"Java Server IP:", value="aetheria.world", inline=False)
            embed.add_field(name=f"Bedrock Server IP:", value="aetheriabedrock.ddns.net", inline=False)
            await ctx.channel.send(embed=embed)

            embed = discord.Embed(title="Server Versions",
                                  description="Here is some information you might need to know:", color=INFO)
            embed.add_field(name=f"Java Server: ", value="1.16.3", inline=False)
            embed.add_field(name=f"Bedrock Server:", value="**NOT ONLINE**", inline=False)
            await ctx.channel.send(embed=embed)

            embed = discord.Embed(title="Server List",
                                  description="A list of the servers available for the java server:", color=INFO)
            embed.add_field(name=f"Hub:", value="The server that allows connection to all other servers.", inline=False)
            embed.add_field(name=f"Survival/Aetheria: ",
                            value="The \"modded\" survival world made to be like Aetheria. Not actually modded, don't worry.",
                            inline=False)
            embed.add_field(name=f"Vanilla: ", value="A vanilla Minecraft world, that's it. Also there's no rules.",
                            inline=False)
            embed.add_field(name=f"Beta: ", value="A server where you can test out our newest features!", inline=False)
            embed.add_field(name=f"UHC: ",
                            value="Stands for Ultra Hardcore. If you don't know what it is, it's basically hunger games but in a blank world with a closing border.",
                            inline=False)
            embed.add_field(name=f"How to join the server:",
                            value="Check out <#719614335361744967> for instructions to join!", inline=False)
            await ctx.channel.send(embed=embed)

            embed = discord.Embed(title="Server Invite", description="Make sure to invite your friends!", color=INFO)
            embed.add_field(name=f"Invite:", value="<https://discord.gg/yfNYNkM>", inline=False)
            await ctx.channel.send(embed=embed)

            embed = discord.Embed(title="Servers that are currently down",
                                  description="These servers are currently offline.", color=WARN)
            embed.add_field(name=f"UHC", value="UHC is currently down until further notice.", inline=False)
            embed.add_field(name=f"Bedrock", value="Bedrock is currently down until further notice.", inline=False)
            await ctx.channel.send(embed=embed)

            embed = discord.Embed(title="Beta Server Commands",
                                  description="These commands are for abilites in the beta server.", color=INFO)
            embed.add_field(name=f"Stats", value="`/stat`", inline=False)
            embed.add_field(name=f"Abilites", value="`/ability [<add/clear/remove>] [<ability>]`", inline=False)
            await ctx.channel.send(embed=embed)

            embed = discord.Embed(title="Staff & Youtube Rank Applications",
                                  description="Apply for staff or <@&529067749909987339> rank", color=INFO)
            embed.add_field(name=f"Rank Applications", value="do ea!apply <position> in <#532417633782595584>",
                            inline=False)
            embed.add_field(name=f"<@&529067749909987339> Rank Applications",
                            value="DM <@456951144166457345> or <@287696585142304769> or anyone with the <@&770078888277049344> role",
                            inline=False)
            await ctx.channel.send(embed=embed)

            embed = discord.Embed(title="Support tickets",
                                  description="If you need help from staff, please feel free to open a ticket!",
                                  color=INFO)
            embed.add_field(name=f"Get Help", value="Head Over to <#737020656360882197> and open a support ticket!",
                            inline=False)
            embed.add_field(name=f"Player reports",
                            value="If you would like to report a player stealing or hacking, head over to <#737020656360882197> and open a Report A Player ticket!",
                            inline=False)
            embed.add_field(name=f"Bug Reports",
                            value="If you experience a bug or something that isn't e=intended with any of our plugins, go to <#737020656360882197> and open a Bug Report ticket.",
                            inline=False)
            embed.add_field(name=f"Punishment Appeals",
                            value="If you think that a staff member punished you unfairly, go to <#737020656360882197> and open an appeal ticket.",
                            inline=False)
            embed.add_field(name=f"Please Also Read:",
                            value="Please read [this](https://discord.com/channels/528980928094142484/737020656360882197/737024010499653693) before creating a ticket.",
                            inline=False)
            await ctx.channel.send(embed=embed)

            embed = discord.Embed(title="Current Available Staff Positions",
                                  description="Available Staff Positions you can apply to", color=INFO)
            embed.add_field(name=f"Rank Applications", value="do ea!apply <position> in <#532417633782595584>",
                            inline=False)
            embed.add_field(name=f"Builder", value="do ea!apply Builder in <#532417633782595584>", inline=False)
            embed.add_field(name=f"Developer", value="do ea!apply Developer in <#532417633782595584>", inline=False)
            embed.add_field(name=f"Loremaster", value="do ea!apply Loremaster in <#532417633782595584>", inline=False)
            embed.add_field(name=f"Discord Staff", value="do ea!apply Discord in <#532417633782595584>", inline=False)

            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="Error", description="You Must be Whitelisted to execute this.", color=ERROR)
            await ctx.channel.send(embed=embed)
    @commands.command()
    async def totop(self, ctx):
        embed = discord.Embed(title="Go To Top", description="Click [here](https://discord.com/channels/528980928094142484/545994362413252608/773616074268475403)",color=INFO)
        await ctx.channel.send(embed=embed)
        #TODO to prevent spam.

def setup(client):
    client.add_cog(server(client))