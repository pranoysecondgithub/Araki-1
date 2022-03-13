import nextcord
from nextcord.ext import commands
from nextcord import ButtonStyle
from nextcord.ui import Button, View
import main, config
from main import *
from config import *

class Vote(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.command()
  async def Vote(self,ctx):
    dbl = Button(label="DBL", url=dbl_vote, emoji="<:dbl:952288060425519165>")
    top = Button(label="Top.gg", url=topgg, emoji="<:topgg:952288172446998528>")
    embed = nextcord.Embed(title="Vote me please!", description="Click on these button to vote me !", colour = clr)
    myVote = View()
    myVote.add_item(dbl)
    myVote.add_item(top)
    await ctx.send(embed=embed, view=myVote)
def setup(client):
  client.add_cog(Vote(client))