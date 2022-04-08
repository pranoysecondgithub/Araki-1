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
    embed.add_field(name=f"Vote", value="Example ```{prefix}vote```")
    embed.add_field(name=f"Coinflip", value="Example ```{prefix}cf amount```")
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)

  @nextcord.slash_command(name='earn', description='It will show how you earn arency')
  async def EarnS(self, intr:nextcord.Interaction):
    prefix_check = await predb.find_one({"guild": intr.guild.id})
    prefix = prefix_check['prefix']
    embed = nextcord.Embed(title="Ways to earn arency", colour=clr)
    embed.add_field(name=f"Work", value="Example ```/work```")
    embed.add_field(name=f"Slots", value="Example ```/slots amount```")
    embed.add_field(name=f"Vote", value="Example ```/vote```")
    embed.add_field(name=f"Coinflip", value="Example ```/cf amount```")
    embed.set_footer(text=footer)
    await intr.response.send_message(embed=embed)
def setup(client):
  client.add_cog(Earn(client))