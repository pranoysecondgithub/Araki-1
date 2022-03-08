import nextcord, emoji, config
from nextcord.ext import commands
from emoji import *
from config import *
from main import *

class Unban(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(ban_members=True)
  @commands.bot_has_permissions(ban_members=True)
  @commands.cooldown(2, 1, type=commands.BucketType.user)
  async def Unban(self, ctx, member: nextcord.User = None):
    if member == None:
      await ctx.reply(f"{error} | Please mention a member!")
    guild = ctx.guild
    embed = nextcord.Embed(title=f'{success} | Unbanned Successfully', description=f"{member} Unbanned by {ctx.author.mention}", colour=clr)
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)
    await ctx.guild.unban(user=member)
def setup(client):
  client.add_cog(Unban(client))