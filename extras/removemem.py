import nextcord
from nextcord.ext import commands
from config import *
from main import *
from emoji import *
import datetime

class Leave(commands.Cog):
  def __init__(self, client):
    self.client = client
        
  @commands.command(aliases=['Set-leave'])
  @commands.has_permissions(administrator=True)
  async def set_leave(self, ctx, channel:nextcord.TextChannel = None):
    if channel == None:
      channel = ctx.channel
    find = await leave.find_one({"guild": ctx.guild.id})
    if find is None:
      insert = {"guild": ctx.guild.id, "channel": channel.id}
      await leave.insert_one(insert)
      await ctx.send(f"{success} | Leave channel set to {channel}")
    elif channel == find['channel']:
      await ctx.reply(f"{error} | This channel is already registered for leave")
    else:
      await leave.update_one({"guild": ctx.guild.id}, {"$set": {"channel": channel.id}})
      await ctx.send(f"{success} | Leave channel changed to {channel}")
  @commands.command(aliases=['Remove-leave'])
  @commands.has_permissions(administrator=True)
  async def remove_leave(self, ctx, channel:nextcord.TextChannel = None):
    if channel == None:
      channel = ctx.channel
    find = await leave.find_one({"guild": ctx.guild.id, "channel": ctx.channel.id})
    if find is None:
      await ctx.reply(f"{error} | This is not a Leave channel!")
    else:
      await leave.delete_one({"guild": ctx.guild.id, "channel": ctx.channel.id})
      await ctx.send(f"{success} | Leave channel removed!")
              
  @commands.Cog.listener()
  async def on_member_remove(self,member):
    timestamp = datetime.datetime.utcnow()
    embed = nextcord.Embed(title=f"", description=f"{member.name} just leave the server.", colour=clr)
    embed.set_footer(text=f"Leave at {timestamp}")
    embed.set_thumbnail(url=member.avatar.url)
    find = await leave.find_one({"guild": member.guild.id})
    if find is None:
      pass
    else:
      channel = find['channel']
      await pranoy.get_channel(channel).send(embed=embed)
def setup(client):
  client.add_cog(Leave(client))