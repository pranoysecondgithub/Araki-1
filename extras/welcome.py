import nextcord
from nextcord.ext import commands
from config import *
from main import *
from emoji import *
import datetime

class Welcome(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['Set-welcome'])
  async def set_welcome(self, ctx, channel:nextcord.TextChannel = None):
    if channel == None:
      channel = ctx.channel
    find = await welcome.find_one({"guild": ctx.guild.id})
    if find is None:
      insert = {"guild": ctx.guild.id, "channel": channel.id}
      await welcome.insert_one(insert)
      await ctx.send(f"{success} | Welcome channel set to {channel}")
    else:
      update = {"guild": ctx.guild, "channel": channel.id}
      await welcome.update_one(update)
      await ctx.send(f"{success} | Welcome channel changed to {channel}")
  @commands.command(aliases=['Remove-welcome'])
  async def remove_welcome(self, ctx, channel:nextcord.TextChannel = None):
    if channel == None:
      channel = ctx.channel
    find = await welcome.find_one({"guild": ctx.guild.id, "channel": ctx.channel.id})
    if find is None:
      await ctx.reply(f"{error} | This is not a welcome channel!")
    else:
      await welcome.delete_one({"guild": ctx.guild.id, "channel": ctx.channel.id})
      await ctx.send(f"{success} | Welcome channel removed!")
      
  @commands.Cog.listener()
  async def on_member_join(self,member):
    timestamp = datetime.datetime.utcnow()
    embed = nextcord.Embed(title=f"", description=f"Hey {member.mention}, Welcome to our server {member.guild.name}.", colour=clr)
    embed.set_author(name=member.name,icon_url=pranoy.user.avatar.url)
    embed.set_footer(text=f"Joined at {timestamp}")
    embed.set_thumbnail(url=member.avatar.url)
    find = await welcome.find_one({"guild": member.guild.id})
    if find is None:
      pass
    else:
      channel = find['channel']
      await pranoy.get_channel(channel).send(f"Hii {member.mention}", embed=embed)
def setup(client):
  client.add_cog(Welcome(client))