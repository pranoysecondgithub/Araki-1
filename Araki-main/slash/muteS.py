import nextcord
from nextcord.ext import commands
import main, config, emoji
from main import *
from emoji import *
from config import *
import asyncio


class Confirm(nextcord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = True
  @nextcord.ui.button(label='Create', style=nextcord.ButtonStyle.green)
  async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    await interaction.response.send_message('Checking.....', ephemeral=True)
    await asyncio.sleep(3)
    guild = interaction.guild
    mutedRole = await guild.create_role(name="Muted")
    for channel in guild.channels:
      await channel.set_permissions(mutedRole, speak=False, send_messages=False)
    await interaction.channel.send("Mute role successfully created!\nRun the command again to mute the member.", delete_after=5)
    self.value = True
    self.stop()

class MuteS(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @nextcord.slash_command(name='mute', description='Mute a member')
  @application_checks.has_permissions(administrator=True)
  async def muteS(
    self,
    interaction:nextcord.Interaction,
    member: nextcord.Member = nextcord.SlashOption(name='user', description='mention a user'),
    reason: str = nextcord.SlashOption(name='reason', description='Please provide a reason')
  ):
        guild = interaction.guild
        muteRole = nextcord.utils.get(guild.roles, name="Muted")
        if not muteRole:
          view = Confirm()
          await interaction.response.send_message("You don't have a mute role click **Create** to create a mute role and run the same command again to mute the user.", view=view, ephemeral=True)
        else:
          await member.add_roles(muteRole, reason=reason)
          embed1 = nextcord.Embed(title=f"{success} | Muted", description=f"Muted {member.name} for {reason}", colour=clr)
          embed1.set_footer(text=footer)
          await interaction.response.send_message(embed=embed1)
          try:
            await member.send(f"You were muted in {guild.name} for {reason}")
          except:
            pass
    
  @nextcord.slash_command(name='unmute', description='Unmute a member')
  @application_checks.has_permissions(administrator=True)
  async def unmuteS(
    self,
    interaction:nextcord.Interaction,
    member: nextcord.Member = nextcord.SlashOption(name='user', description='mention a user')
  ):
    mutedRole = nextcord.utils.get(interaction.guild.roles, name="Muted")
    try:
      await member.remove_roles(mutedRole)
    except:
      pass
    try:
      await member.send(f" You have unmuted from: - {ineteraction.guild.name}")
    except:
      pass
    embed = nextcord.Embed(title=f"{success} | Unmute", description=f" Unmuted-{member.mention}",colour=clr)
    await interaction.response.send_message(embed=embed)
def setup(client):
  client.add_cog(MuteS(client))