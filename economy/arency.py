import nextcord, motor, json, asyncio, random, config, main
from nextcord.ext.commands import BucketType, cooldown
from nextcord.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient
from config import *
from main import *

class Bal(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @commands.command(aliases=['bal', ',cash', 'balance'])
  # @commands.is_owner()
  async def Arency(self, ctx, member: nextcord.Member = None):
      author = ctx.author
      prefix_check = await predb.find_one({"guild": ctx.guild.id})
      prefix = prefix_check['prefix']
      if member is None:
        check = await cursor.find_one({"id": author.id})
        if check is None:
          await ctx.message.reply(f"You don't have a profile!\nPlease execute the `{prefix}create` command to create a profile!")
          return
        else:
          balance = check['money']
        #   emb = nextcord.Embed(
        #   title = "Your balance!",
        #         description = f"**Balance:** ${balance}",
        #         color = clr
        # )
        await ctx.message.reply(f"You have **{balance:,} arency!**")
        return
      else:
        check = await cursor.find_one({"id": member.id})
        if check is None:
          await ctx.message.reply("The user you have mentioned does not have a profile!")
          return
        else:
          balance = check['money']
        #   emb2 = nextcord.Embed(
        #   title = f"{member.name}'s Balance!",
        #         description = f"**Balance:** ${balance}",
        #         color = clr
        # )
          await ctx.message.reply(f"{member.name} have **{balance:,} arency!**")

def setup(client):
  client.add_cog(Bal(client))