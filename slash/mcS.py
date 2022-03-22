import nextcord
from nextcord.ext import commands
import main
from main import *

class MemberCountS(commands.Cog):
  def __init__(self, client):
    self.client = client

  @nextcord.slash_command(name='membercount', description='This shows the guild member count')
  async def MemberCountS(self, interaction:nextcord.Interaction):
    embed = nextcord.Embed(
      title=f"Member count of {interaction.guild.name}",
      description=f"```{interaction.guild.member_count}```",
      colour=clr
    )
    await interaction.response.send_message(embed=embed)

def setup(client):
  client.add_cog(MemberCountS(client))