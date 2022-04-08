import nextcord, motor, json, asyncio, random, config, main
from nextcord.ext.commands import BucketType, cooldown
from nextcord.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient
from config import *
from main import *

class BalS(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @nextcord.slash_command(name='arency', description='This show the arency of the user')
  async def ArencyS(
    self,
    interaction:nextcord.Interaction,
    member: nextcord.Member = nextcord.SlashOption(name='user', description='mention a user', required=False)
    ):
      prefix_check = await predb.find_one({"guild": interaction.guild.id})
      prefix = prefix_check['prefix']
      if not member:
        check = await cursor.find_one({"id": interaction.user.id})
        if check is None:
          await interaction.response.send_message(f"You don't have a profile!\nPlease execute the `{prefix}create or /create` command to create a profile!")
          return
        else:
          balance = check['money']
        #   emb = nextcord.Embed(
        #   title = "Your balance!",
        #         description = f"**Balance:** ${balance}",
        #         color = clr
        # )
        await interaction.response.send_message(f"You have **{balance:,} arency!**")
        return
      else:
        check = await cursor.find_one({"id": member.id})
        if check is None:
          await interaction.response.send_message("The user you have mentioned does not have a profile!")
          return
        else:
          balance = check['money']
          await interaction.response.send_message(f"{member.name} have **{balance:,} arency!**")

def setup(client):
  client.add_cog(BalS(client))