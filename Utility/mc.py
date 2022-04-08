import nextcord
from nextcord.ext import commands
import main
from main import *

class MemberCount(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['mc'])
  async def MemberCount(self, ctx):
    embed = nextcord.Embed(
      title=f"Member count of {ctx.guild.name}",
      description=f"{ctx.guild.member_count}",
      colour=clr
    )
    embed.set_thumbnail(url=ctx.author.avatar.url)
    await ctx.reply(embed=embed)

def setup(client):
  client.add_cog(MemberCount(client))