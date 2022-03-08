import nextcord, config, main, emoji
from nextcord.ext import commands
from emoji import *
from config import *

class Warn(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def Warn(self, ctx, member:nextcord.Member, reason = "No reason"):
    if member == None:
      await ctx.reply(f"{error} | Please mention someone")
    elif member == ctx.author.mention:
      await ctx.reply("You can't warn")
    else:
      emb = nextcord.Embed(title=f'{success} | Warning', description=f"{ctx.author.mention} warn {member.mention} for {reason}")
      emb.set_footer(text=footer)
      await ctx.send(embed=emb)
      try:
        await member.send(f"You have been warned from **{ctx.guild}** for {reason}")
      except:
        pass

def setup(client):
  client.add_cog(Warn(client))