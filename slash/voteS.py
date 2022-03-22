import nextcord
from nextcord.ext import commands
from nextcord import ButtonStyle
from nextcord.ui import Button, View
import main, config
from main import *
from config import *

class VoteS(commands.Cog):
  def __init__(self, client):
    self.client = client


  @nextcord.slash_command(name='vote', description='please vote me')
  async def VoteS(self,interaction: nextcord.Interaction):
    top = Button(label="Top.gg", url=topgg, emoji="<:topgg:952288172446998528>")
    embed = nextcord.Embed(title="Vote me please!", description="Click on the button to vote me !", colour = clr)
    myVote = View()
    myVote.add_item(top)
    await interaction.response.send_message(embed=embed, view=myVote)
def setup(client):
  client.add_cog(VoteS(client))