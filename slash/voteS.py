import nextcord
from nextcord.ext import commands
from nextcord import ButtonStyle
from nextcord.ui import Button, View
import main, config, emoji
from main import *
from config import *
from emoji import *

class VoteS(commands.Cog):
  def __init__(self, client):
    self.client = client


  @nextcord.slash_command(name='vote', description='please vote me')
  async def VoteS(self,interaction: nextcord.Interaction):
    top = Button(label="Top.gg", url=topgg, emoji="<:topgg:952288172446998528>")
    embed = nextcord.Embed(title="Vote me", description="You can vote in every 12hr and claim these rewards.", colour = clr)
    embed.add_field(name="Rewards:-", value=f":fish: Fish ```1x```\n{arency} Arency 1000")
    embed.set_footer(text="Vote me to get these rewards.")
    myVote = View()
    myVote.add_item(top)
    await interaction.response.send_message(embed=embed, view=myVote)
def setup(client):
  client.add_cog(VoteS(client))