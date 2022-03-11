import nextcord
from nextcord.ext import commands
import main, emoji, config
from main import *
from emoji import *
from config import *

class Ban(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(ban_members=True)
  @commands.bot_has_permissions(ban_members=True)
  async def Ban(self, ctx, member: nextcord.Member = None, *, reason = 'No reason'):
    user = ctx.author
    if member == None:
      await ctx.reply("Please provide a member")
    else:
      try:
        await member.ban(reason=reason)
        emb = nextcord.Embed(title=f'{success} | Successfully Banned', description=f"{ctx.author.mention} banned {member.mention} for {reason}", colour=clr)
        emb.set_footer(text=footer)
        await ctx.send(embed=emb)
      except:
        pass
      
def setup(client):
  client.add_cog(Ban(client))