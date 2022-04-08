import nextcord
from nextcord.ext import commands
import main
from main import *

class Ping(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def Ping(self, ctx):
    _ping = round(pranoy.latency * 1000)
    pingEmbed = nextcord.Embed(title="Bot Ping", description= _ping, colour=0x303136)
    pingEmbed.set_footer(text='Made by Pranoy#0140')
    pingEmbed.set_thumbnail(url=ctx.author.avatar.url)
    await ctx.reply(embed=pingEmbed)

def setup(client):
  client.add_cog(Ping(client))