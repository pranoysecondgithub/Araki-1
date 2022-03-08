import nextcord, motor, json, asyncio, random, config, main
from nextcord.ext.commands import BucketType, cooldown
from nextcord.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient
from config import *
from main import *

class Work(commands.Cog):
  def __init__ (self, client):
    self.client = client
  
  @commands.cooldown(1, 7200, commands.BucketType.user)
  @commands.command()
  async def work(self, ctx):
      user = ctx.author
      prefixcheck = await predb.find_one({"guild": ctx.guild.id})
      prefix = prefixcheck['prefix']
      check = await cursor.find_one({"id": user.id})
      if check is None:
        await ctx.message.reply(f"You don't have a profile!\nPlease execute the `{prefix}create` command to create a profile!")
        return
      else:
        job_names = ["Cashier", "McDonald's Worker", "Criminal", "Retail Worker", "Mechanic"]
        job = random.choice(job_names)
        amount = random.randint(100, 500)
        newBal = check['money'] + amount
        await cursor.update_one({"id": user.id}, {"$set": {"money": newBal}})
        emb4 = nextcord.Embed(
            title = "You have finished working!",
            description = f"You have worked as a **{job}** and earned **{amount} arency**!",
            color = clr
        )
        emb4.set_author(name="Work result",icon_url=ctx.author.avatar.url)
        await ctx.message.reply(embed=emb4)

def setup(client):
  client.add_cog(Work(client))