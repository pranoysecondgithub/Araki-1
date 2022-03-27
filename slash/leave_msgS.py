import nextcord
from nextcord.ext import commands
from config import *
from main import *
from emoji import *
import datetime

class LeaveS(commands.Cog):
  def __init__(self, client):
    self.client = client
        
  @nextcord.slash_command(name='set-leave-channel', description='This command will set the leave channel for you!')
  @commands.has_permissions(administrator=True)
  async def set_leaveS(
    self,
    interaction:nextcord.Interaction,
    channel: nextcord.abc.GuildChannel = nextcord.SlashOption(channel_types=[ChannelType.text],name='channel', description='Please select a channel', required=False)
    ):
    if not channel:
      channel = interaction.channel
    find = await leave.find_one({"guild": interaction.guild.id})
    if find is None:
      insert = {"guild": interaction.guild.id, "channel": channel.id}
      await leave.insert_one(insert)
      await interaction.response.send_message(f"{success} | Leave channel set to {channel}")
    elif channel == find['channel']:
      await interaction.response.send_message(f"{error} | This channel is already registered for leave")
    else:
      await leave.update_one({"guild": interaction.guild.id}, {"$set": {"channel": channel.id}})
      await interaction.response.send_message(f"{success} | Leave channel changed to {channel}")
  @nextcord.slash_command(name='remove-leave-channel', description='This will remove your leave channel')
  @commands.has_permissions(administrator=True)
  async def remove_leaveS(self,
                          interaction:nextcord.Interaction,
                          channel: nextcord.abc.GuildChannel = nextcord.SlashOption(channel_types=[ChannelType.text],name='channel', description='Please select a channel', required=False)
                          ):
    find = await leave.find_one({"guild": interaction.guild.id, "channel": channel.id})
    if not channel:
      channel = interaction.channel
    if find is None:
      await interacton.response.send_message(f"{error} | This is not a Leave channel!")
    else:
      await leave.delete_one({"guild": guild.id, "channel": channel.id})
      await interacton.response.send_message(f"{success} | Leave channel removed!")
              
def setup(client):
  client.add_cog(LeaveS(client))