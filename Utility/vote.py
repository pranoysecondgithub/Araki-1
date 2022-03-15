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
      top = Button(label="Top.gg", url=topgg, emoji="<:topgg:952288172446998528>")
      embed = nextcord.Embed(title=f"{ctx.author.name} Vote me please!", description="Click on this button to vote me!", colour = clr)
      embed.set_footer(text="You can vote in every 12hr!")
      myVote = View()
      myVote.add_item(top)
      await ctx.send(embed=embed, view=myVote)
def setup(client):
  client.add_cog(Vote(client))