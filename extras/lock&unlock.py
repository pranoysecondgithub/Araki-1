import nextcord, config, main, emoji
from nextcord.ext import commands
from main import *
from config import *
from emoji import *

class Lock_Unlock(commands.Cog):
  def __init__(self,client):
    self.client = client
    
  @commands.command(aliases=['lock'])
  @commands.has_permissions(manage_channels=True)
  async def Lockdown(self, ctx, channel:nextcord.TextChannel = None):
    if channel == None:
      channel = ctx.channel
    await channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send(f"<#{channel.id}> Is now in lockdown!")
    
  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def Unlock(self, ctx, channel:nextcord.TextChannel = None):
    if channel == None:
      channel = ctx.channel
    await channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(f"<#{channel.id}> is now unlocked")
  
def setup(client):
  client.add_cog(Lock_Unlock(client))