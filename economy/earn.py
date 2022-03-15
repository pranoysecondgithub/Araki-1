import nextcord, main, config, emoji
from nextcord.ext import commands
from main import *
from config import *
from emoji import *

class Earn(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.command()
  async def Earn(self, ctx):
    prefix_check = await predb.find_one({"guild": ctx.guild.id})
    prefix = prefix_check['prefix']
    embed = nextcord.Embed(title="Ways to earn arency", colour=clr)
    embed.add_field(name=f"Work", value="Example ```{prefix}work```")
    embed.add_field(name=f"Slots", value="Example ```{prefix}slots amount```")
    embed.add_field(name=f"Coinflip", value="Example ```{prefix}cf amount```")
    embed.add_field(name=f"Vote", value="Example ```{prefix}vote```")
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)
def setup(client):
  client.add_cog(Earn(client))