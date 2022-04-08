import nextcord
from nextcord.ext import commands
import config, main, emoji
from main import *
from config import *
from emoji import *

class Give(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.command()
  async def Give(self, ctx, user: nextcord.Member = None, amount = None):
    pre = await predb.find_one({"guild": ctx.guild.id})
    prefix = pre['prefix']
    if user == None:
      await ctx.reply("**Opps error**\n**Example:**\n```give @mention amount```")
    find = await cursor.find_one({"id": user.id})
    user_find = await cursor.find_one({"id": ctx.author.id})
    if find is None:
        await ctx.message.reply("User don't have a profile!")
        return
    elif user_find is None:
      await ctx.reply(f"You don't have a profile!\nPlease execute the `{prefix}create or /create` command to create a profile!")
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
              description = f"{ctx.author.mention} give {amount} to {user.mention}",
              colour = clr
          )
        await ctx.reply(embed=emb4)
  @nextcord.slash_command(name="give", description="Give arency to a user!")
  async def GiveS(self,
                 intr:nextcord.Interaction,
                 user: nextcord.Member = nextcord.SlashOption(name='user', description='mention a user'),
                 amount: int = nextcord.SlashOption(name="amount", description='Please provide a amount')
                 ):
    pre = await predb.find_one({"guild": intr.guild.id})
    prefix = pre['prefix']
    find = await cursor.find_one({"id": user.id})
    user_find = await cursor.find_one({"id": intr.user.id})
    if find is None:
        await intr.response.send_message("User don't have a profile!", ephemeral=True)
        return
    elif user_find is None:
      await intr.response.send_message(f"You don't have a profile!\nPlease execute the `{prefix}create or /create` command to create a profile!", ephemeral=True)
      return
    elif user == intr.user.mention:
      await intr.response.send_message("You cant do that!")
    elif amount > 1000000:
      await intr.response.send_message(f"You can't give more then 1000000 {arency}!")
    else:
      user_amount = int(amount)
      balance = user_find['money']
      newBal = find['money'] + int(amount)
      user_cut = user_find['money'] - int(amount)
      if balance <= 0:
        await intr.response.send_message("Your balance is too low!")
      elif balance < user_amount:
        await intr.response.send_message("Your balance is too low!")
      else:
        await cursor.update_one({"id": user.id}, {"$set": {"money": newBal}})
        await cursor.update_one({"id": intr.user.id}, {"$set": {"money": user_cut}})
        emb4 = nextcord.Embed(
              title = "Successful",
              description = f"{intr.user.mention} give {amount} to {user.mention}",
              colour = clr
          )
        await intr.response.send_message(embed=emb4)

def setup(client):
  client.add_cog(Give(client))