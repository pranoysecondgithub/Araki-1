import nextcord
from nextcord.ext import commands
import main, emoji, config
from main import *
from emoji import *
from config import *

class BanS(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @nextcord.slash_command(name='ban', description='Ban a member')
  @application_checks.has_permissions(ban_members=True)
  async def BanS(
    self,
    interaction:nextcord.Interaction,
    member: nextcord.Member = nextcord.SlashOption(name='user', description='mention a user'),
    reason: str = nextcord.SlashOption(name='reason', description='Please provide a reason')
  ):
    try:
        await member.ban(reason=reason)
        emb = nextcord.Embed(title=f'{success} | Successfully Banned', description=f"{interaction.user.mention} banned {member.mention} for {reason}", colour=clr)
        emb.set_footer(text=footer)
        await interaction.response.send_message(embed=emb)
    except:
      pass

def setup(client):
  client.add_cog(BanS(client))