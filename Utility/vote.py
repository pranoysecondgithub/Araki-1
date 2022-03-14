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
    top = Button(label="Vote Me", url=topgg, emoji="<:topgg:952288172446998528>")
    embed = nextcord.Embed(title="Vote me please!", description="Click on the button to vote me!", colour = clr)
    myVote = View()
    myVote.add_item(top)
    await ctx.send(embed=embed, view=myVote)
def setup(client):
  client.add_cog(Vote(client))