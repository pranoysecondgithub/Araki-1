import nextcord
from nextcord.ext import commands
import main, config
from main import *
from config import *
from emoji import *

class KickS(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @nextcord.slash_command(name='kick', description='Kick a member')
  @commands.has_permissions(kick_members=True)
  @commands.bot_has_permissions(kick_members=True)
  async def KickS(
    self,
    interaction:nextcord.Interaction,
    member: nextcord.Member = nextcord.SlashOption(name='user', description='mention a user'),
    reason: str = nextcord.SlashOption(name='reason', description='Please provide a reason')
    ):
    user = interaction.user
    try:
      await member.kick(reason=reason)
      embKick = nextcord.Embed(title=f'{success} | Successfully Kicked', description=f"{user.mention} kicked {member.mention} for {reason}", colour=clr)
      embKick.set_footer(text=footer)
      await interaction.response.send_message(embed=embKick)
    except:
      pass
        
def setup(client):
  client.add_cog(KickS(client))