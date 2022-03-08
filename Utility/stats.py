import nextcord, main, config, emoji, psutil
from nextcord.ext import commands
from main import *
from emoji import *
from config import *
from psutil import Process, virtual_memory
from platform import python_version
from datetime import datetime, timedelta

class Stats(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def Stats(self, ctx):
    prefix = await predb.find_one({"guild": ctx.guild.id})
    embed = nextcord.Embed(
      title=f"{pranoy.user}'s stats",
      description=f"Here's a little bit of information! If you need help with commands, type ```{prefix['prefix']}help```.",
      colour=clr,
    )
    proc = Process()
    with proc.oneshot():
      uptime = timedelta(seconds= time()-proc.create_item())
      mem_total = virtual_memory().total / (1024**2)
    embed.add_field(name="Devloper", value="Pranoy#0140", inline=True)
    embed.add_field(name="Bot Stats", value=f"Total users :- {pranoy.guilds.member_count}\nTotal servers :- {pranoy.guilds}\nPython version :- {python_version()}\nNextcord version :- {nextcord_version}\nUptime :- {uptime}\Total memory :- {mem_total}", inline=True)
    await ctx.send(embed=embed)
def setup(client):
  client.add_cog(Stats(client))