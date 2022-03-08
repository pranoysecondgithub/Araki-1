import nextcord
from nextcord.ext import commands
import main
from main import *

class Poll(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @commands.command()
  async def poll(self, ctx, *, message = None):
    emb = nextcord.Embed(title='📢 Poll', description=f"{message}", color=clr)
    emb.set_footer(text="Made by Pranoy#0140")
    if message == None:
      await ctx.reply("Missing description.")
    else:
      msg = await ctx.channel.send(embed=emb)
      await msg.add_reaction('👍')
      await msg.add_reaction('👎')

def setup(client):
  client.add_cog(Poll(client))