import nextcord, motor, config
from nextcord.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient
from config import *
import main, emoji
from main import *
from emoji import *
class PrefixS(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @nextcord.slash_command(name='set-prefix', description='This will change the bot prefix')
  @commands.has_permissions(administrator=True)
  async def setprefixS(
    self,
    interaction: nextcord.Interaction,
    new_prefix: str = nextcord.SlashOption(name='new-prefix', description='Please entre a new prefix')
    ):
    cluster = AsyncIOMotorClient(['mongodb+srv://pranoycasito:ricky&casito@cluster0.m9at5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'])
    db = cluster["main"]
    predb = db["prefix"]
    stats = await predb.find_one({"guild": interaction.guild.id})
    if stats is None:
      updated = {"guild": interaction.guild.id, "prefix": new_prefix}
      await predb.insert_one(updated)
      embed2 = nextcord.Embed(title=f"{success} | Prefix updated",description=f"This server prefix is now {new_prefix}",colour=clr)
      embed2.set_footer(text=footer)
      await interaction.response.send_message(embed=embed2)
    else:
      await predb.update_one({"guild": interaction.guild.id}, {"$set": {"prefix": new_prefix}})
      embed3 = nextcord.Embed(title=f"{success} | Prefix updated",description=f"This server prefix is now {new_prefix}",colour=clr)
      embed3.set_footer(text=footer)
      await interaction.response.send_message(embed=embed3)
def setup(client):
    client.add_cog(PrefixS(client))