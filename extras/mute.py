import nextcord
from nextcord.ext import commands
import main, config, emoji
from main import *
from emoji import *
from config import *

class Lock(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def mute(self, ctx, member: nextcord.Member, *, reason='No reason'):
        guild = ctx.guild
        muteRole = nextcord.utils.get(guild.roles, name="Muted")
        if not muteRole:
          try:
            mutedRole = await guild.create_role(name="Muted")
          except:
            await ctx.reply('Something went wrong')
        if reason == None:
          reason = 'No reason'

        for channel in guild.channels:
          await channel.set_permissions(muteRole, speak=False, send_messages=False)
        try:
          await member.add_roles(muteRole, reason=reason)
          embed1 = nextcord.Embed(title=f"{success} | Muted", description=f"Muted {member} for {reason}", colour=clr)
          embed1.set_footer(text=footer)
          await ctx.send(embed=embed1)
        except:
          await ctx.reply('Something went wrong')
        try:
          await member.send(f"You were muted in {guild.name} for {reason}")
        except:
          pass
    
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def unmute(self, ctx, member: nextcord.Member):
    mutedRole = nextcord.utils.get(ctx.guild.roles, name="Muted")
    try:
      await member.remove_roles(mutedRole)
    except:
      await ctx.reply('Something went wrong')
    try:
      await member.send(f" You have unmuted from: - {ctx.guild.name}")
    except:
      pass
    embed = nextcord.Embed(title=f"{success} | Unmute", description=f" Unmuted-{member.mention}",colour=clr)
    await ctx.send(embed=embed)
def setup(client):
  client.add_cog(Lock(client))