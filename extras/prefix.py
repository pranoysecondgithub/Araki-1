import nextcord, motor, config
from nextcord.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient
from config import *
import main, emoji
from main import *
from emoji import *
class Prefix(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def setprefix(self, ctx, new_prefix = None):
    cluster = AsyncIOMotorClient(['mongodb+srv://pranoycasito:ricky&casito@cluster0.m9at5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'])
    db = cluster["main"]
    predb = db["prefix"]
    if new_prefix == None:
      embed1 = nextcord.Embed(title=f"{error} | Error",description="Please provide a prefix",colour=clr)
      embed1.set_footer(text=footer)
      await ctx.send(embed=embed1)
    else:
      new_prefix = str(new_prefix)
      stats = await predb.find_one({"guild": ctx.guild.id})
      if stats is None:
        updated = {"guild": ctx.guild.id, "prefix": new_prefix}
        await predb.insert_one(updated)
        embed2 = nextcord.Embed(title=f"{success} | Prefix updated",description=f"This server prefix is now {new_prefix}",colour=clr)
        embed2.set_footer(text=footer)
        await ctx.send(embed=embed2)
      else:
        await predb.update_one({"guild": ctx.guild.id}, {"$set": {"prefix": new_prefix}})
        embed3 = nextcord.Embed(title=f"{success} | Prefix updated",description=f"This server prefix is now {new_prefix}",colour=clr)
        embed3.set_footer(text=footer)
        await ctx.send(embed=embed3)
def setup(client):
    client.add_cog(Prefix(client))