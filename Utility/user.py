import nextcord
from nextcord.ext import commands
import main
from main import *

class UserInfo(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['user'])
  async def Userinfo(self, ctx, member: nextcord.Member = None):
    date_format = "%a, %d %b %Y %I:%M %p"
    if member == None:
      member = ctx.author
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in member.guild_permissions if p[1]])
    embed = nextcord.Embed(title=f"{member}'s info", color=clr)
    embed.add_field(name="Name", value=f"{member.name}", inline=True)
    embed.add_field(name="ID", value=f"{member.id}", inline=True)
    embed.add_field(name="User Joined", value=member.joined_at.strftime(date_format), inline=True)
    embed.add_field(name="Account Age", value=member.created_at.strftime(date_format), inline=True)
    if len(member.roles) > 1:
        role_string = ' '.join([r.mention for r in member.roles][1:])
        embed.add_field(name="Member Roles", value=role_string, inline=True)
    embed.add_field(name="Guild Permission", value=perm_string, inline=True)
    embed.set_footer(text='Made by Pranoy#0410')
    await ctx.send(embed=embed)
def setup(client):
  client.add_cog(UserInfo(client))

