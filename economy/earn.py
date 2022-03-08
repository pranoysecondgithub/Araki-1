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
    embed.add_field(name=f"{prefix}Work", value="Work in every 60 mins to get random money arency. to your credits.")
    embed.add_field(name=f"{prefix}Slots", value="Bet to Have quadruple return if won and Loose the arency if lost.")
    embed.add_field(name=f"{prefix}Coinflip", value="Work in every 60 mins to get random arency acc. to your credits.")
    # embed.add_field(name=f"{prefix}Vote", value="Vote our  bot on top.gg in every 6hr and get 1000 coins after each vote.")
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)
def setup(client):
  client.add_cog(Earn(client))