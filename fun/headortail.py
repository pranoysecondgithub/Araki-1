import nextcord
from nextcord.ext import commands
import main
from main import *

class HeadOrTail(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['hot'])
  async def headortails(self, ctx, answer=None):
    if random.choice(["heads", "tails"]) == answer:
        await ctx.reply("Congratulations")
    else:
        await ctx.reply("Sorry you lost")

def setup(client):
  client.add_cog(HeadOrTail(client))