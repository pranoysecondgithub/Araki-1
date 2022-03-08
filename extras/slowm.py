import nextcord
from nextcord.ext import commands
import main, config, emoji
from main import *
from config import *
from emoji import *
class Slowmode(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['sm'])
  @commands.has_permissions(manage_channels=True)
  async def slowmode(self, ctx, amount = None):
    if amount == None:
      await ctx.send(f"{success} | **Slowmode has been disabled**")
      await ctx.channel.edit(reason='Bot Slowmode Command', slowmode_delay=0)
    else:
        await ctx.channel.edit(reason='Action taken by Araki bot', slowmode_delay=int(amount))
        emb = nextcord.Embed(title=f'{success} | Slowmode Has been enabled', description=f"Slowmode has been enabled you can send message in every {amount}s", colour=clr)
        emb.add_field(name='If you want to disable slowmode', value="Type ```slowmode```", inline=True)
        emb.set_footer(text=footer)
        await ctx.send(embed=emb)

def setup(client):
  client.add_cog(Slowmode(client))