import nextcord
from nextcord.ext import commands
from nextcord import ButtonStyle
from nextcord.ui import Button, View
import main, config, email
from main import *
from config import *
from emoji import *

class Vote(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.command()
  async def Vote(self,ctx):
      top = Button(label="Top.gg", url=topgg, emoji="<:topgg:952288172446998528>")
      embed = nextcord.Embed(title="Vote me", description="You can vote in every 12hr and claim these rewards.", colour = clr)
    embed.add_field(name="Rewards:-", value=f":fish: Fish ```1x```\n{arency} Arency 1000")
    embed.set_footer(text="Vote me to get these rewards.")
      myVote.add_item(top)
      await ctx.send(embed=embed, view=myVote)
def setup(client):
  client.add_cog(Vote(client))