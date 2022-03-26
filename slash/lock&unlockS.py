import nextcord, config, main, emoji
from nextcord.ext import commands
from main import *
from config import *
from emoji import *

class Lock_UnlockS(commands.Cog):
  def __init__(self,client):
    self.client = client
    
  @nextcord.slash_command(name='lock', description='This will lock the channel')
  @commands.has_permissions(manage_channels=True)
  async def LockdownS(
    self,
    interaction:nextcord.Interaction,
    channel: nextcord.abc.GuildChannel = nextcord.SlashOption(channel_types=[ChannelType.text],name='channel', description='Please select a channel', required=False)
  ):
    if not channel:
      channel = interaction.channel
    await channel.set_permissions(interaction.guild.default_role, send_messages=False)
    await interaction.response.send_message(f"<#{channel.id}> Is now in lockdown!")
    
  @nextcord.slash_command(name='unlock', description='This will unlock the channel')
  @commands.has_permissions(manage_channels=True)
  async def UnlockS(
    self,
    interaction:nextcord.Interaction,
    channel: nextcord.abc.GuildChannel = nextcord.SlashOption(channel_types=[ChannelType.text],name='channel', description='Please select a channel', required=False)
  ):
    if not channel:
      channel = interaction.channel
    await channel.set_permissions(interaction.guild.default_role, send_messages=True)
    await interaction.response.send_message(f"<#{channel.id}> is now unlocked")
  
def setup(client):
  client.add_cog(Lock_UnlockS(client))