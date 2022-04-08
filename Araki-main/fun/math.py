import nextcord
from nextcord.ext import commands
import main
from main import *
class Math(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @commands.command()
  async def add(self, ctx, *nums):
    opp = " + ".join(nums)
    try:
      emb = nextcord.Embed(title=f"{ctx.author.name}", description=f"{opp} = {eval(opp)}", color=clr)
      emb.set_footer(text='Made by Pranoy#0140')
      await ctx.send(embed=emb)
    except:
      await ctx.reply("Something went wrong")
def setup(client):
  client.add_cog(Math(client))