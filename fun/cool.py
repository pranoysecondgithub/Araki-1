import nextcord
from nextcord.ext import commands
import random
import main
from main import *

class Cool(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @commands.command()
  async def Cool(self, ctx, user: nextcord.Member = None):
    if user == None:
      user = ctx.author
      emb1 = nextcord.Embed(title='Cool rate', description=f"You are {random.randrange(101)}% cool.", color=clr)
      await ctx.reply(embed=emb1)
    else:
      emb2 = nextcord.Embed(title='Cool rate', description=f"{user.mention} is {random.randrange(101)}% cool.", color=clr)
      await ctx.reply(embed=emb2)

def setup(client):
  client.add_cog(Cool(client))