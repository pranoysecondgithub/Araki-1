import nextcord
from nextcord.ext import commands
import main
from main import *

class Server(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['server'])
  async def Serverinfo(self, ctx):
    guild = ctx.guild
    roles_count = len(ctx.guild.roles)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
    embed = nextcord.Embed(title=f"{guild}'s info", colour=clr)
    embed.add_field(name='Guild Name', value=f"{ctx.guild.name}", inline=True)
    embed.add_field(name='Owner', value=f"{ctx.guild.owner.mention}", inline=True)
    embed.add_field(name='Guild Id', value=f"{ctx.guild.id}", inline=True)
    embed.add_field(name='Owner Id', value=f"{ctx.guild.owner.id}", inline=True)
    embed.add_field(name='Verification Level', value=f"{ctx.guild.verification_level}", inline=True)
    embed.add_field(name='Total Members', value=f"{ctx.guild.member_count}", inline=True)
    embed.add_field(name='Number Of Roles', value=f"{roles_count}", inline=True)
    embed.add_field(name='Bots', value=f"{list_of_bots}", inline=True)
    embed.add_field(name='Highest Role', value=f"{ctx.guild.roles[-2]}", inline=True)
    embed.add_field(name='Guild created at', value=f"{ctx.guild.created_at}", inline=True)
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Server(client))