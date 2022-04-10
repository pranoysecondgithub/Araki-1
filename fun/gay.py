import nextcord
from nextcord.ext import commands
import random
import main
from main import *


class Gay(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @commands.command()
  @commands.is_nsfw()
  async def Gay(self, ctx, user: nextcord.Member = None):
    if user == None:
      user = ctx.author
      emb1 = nextcord.Embed(title='Gay rate', description=f"You are {random.randrange(101)}% gay.", color=clr)
      await ctx.reply(embed=emb1)
    else:
      emb2 = nextcord.Embed(title='Gay rate', description=f"{user.mention} is {random.randrange(101)}% gay.", color=clr)
      await ctx.reply(embed=emb2)

  @Gay.error
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.errors.NSFWChannelRequired):
        msg = 'Sorry this command only works in nsfw channels.'
        em100 = nextcord.Embed(title="**Error Block**", color=clr)
        em100.add_field(name="__Nsfw command:__", value=msg)
        return await ctx.send(embed=em100)


def setup(client):
  client.add_cog(Gay(client))