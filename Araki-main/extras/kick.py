import nextcord
from nextcord.ext import commands
import main, config
from main import *
from config import *
from emoji import *

class Kick(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(kick_members=True)
  @commands.bot_has_permissions(ban_members=True)
  async def Kick(self, ctx, member: nextcord.Member = None, *, reason = 'No reason'):
    user = ctx.author
    if member == None:
      await ctx.reply("Please provide a member")
    else:
        await member.kick(reason=reason)
        emb = nextcord.Embed(title=f'{success} | Successfully Kicked', description=f"{ctx.author.mention} kicked {member.mention} for {reason}", colour=clr)
        emb.set_footer(text=footer)
        await ctx.send(embed=emb)
        
def setup(client):
  client.add_cog(Kick(client))