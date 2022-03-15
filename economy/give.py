import nextcord
from nextcord.ext import commands
import config, main
from main import *
from config import *

class Give(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.command()
  async def Give(self, ctx, user: nextcord.Member = None, amount = None):
    if user == None:
      await ctx.reply("**Opps error**\n**Example:**\n```give @mention amount```")
    find = await cursor.find_one({"id": user.id})
    user_find = await cursor.find_one({"id": ctx.author.id})
    if find is None:
        await ctx.message.reply("User don't have a profile!")
        return
    elif user_find is None:
      await ctx.reply(f"You don't have a profile!\nPlease execute the `create` command to create a profile!")
      return
    elif user == ctx.author.mention:
      await ctx.reply("You cant do that!")
    elif amount == None:
      await ctx.reply("**Opps error**\n**Example:**\n```give @mention amount```")
    else:
      user_amount = int(amount)
      balance = user_find['money']
      newBal = find['money'] + int(amount)
      user_cut = user_find['money'] - int(amount)
      if balance <= 0:
        await ctx.reply("Your balance is too low!")
      elif balance < user_amount:
        await ctx.reply("Your balance is too low!")
      else:
        await cursor.update_one({"id": user.id}, {"$set": {"money": newBal}})
        await cursor.update_one({"id": ctx.author.id}, {"$set": {"money": user_cut}})
        emb4 = nextcord.Embed(
              title = "Successful",
              description = f"{ctx.author.mention} give {amount:,} to {user.mention}",
              color = clr
          )
        await ctx.reply(embed=emb4)

def setup(client):
  client.add_cog(Give(client))