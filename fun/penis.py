import nextcord
from nextcord.ext import commands
import random
import main
from main import *

class Penis(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @commands.command(aliases=['pep'])
  async def Penis(self, ctx, user: nextcord.Member = None):
    if user == None:
      user = ctx.author
      emb1 = nextcord.Embed(title='Nunnu measuring tape', description=f"Your penus size is {random.randrange(11)}inch.", color=clr)
      await ctx.reply(embed=emb1)
    else:
      emb2 = nextcord.Embed(title='Nunnu measuring tape', description=f"{user.mention}'s penis size is {random.randrange(11)}inch.", color=clr)
      await ctx.reply(embed=emb2)

def setup(client):
  client.add_cog(Penis(client))

