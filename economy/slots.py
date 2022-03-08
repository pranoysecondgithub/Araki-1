import nextcord, config, emoji, main, random
from main import *
from config import *
from emoji import *
from nextcord.ext import commands

class Slots(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command()
  async def Slots(self, ctx, amount = 1):
    prefixcheck = await predb.find_one({"guild": ctx.guild.id})
    prefix = prefixcheck['prefix']
    check = await cursor.find_one({"id": ctx.author.id})
    if check is None:
        await ctx.message.reply(f"You don't have a profile!\nPlease execute the `{prefix}create` command to create a profile!")
        return
    else:
      balance = check['money']
      if balance <= 0:
        await ctx.reply("Your balance is too low!")
      elif balance < int(amount):
        await ctx.reply("Your balance is too low!")
      else:
      
        slots = ['bus', 'train', 'horse', 'tiger', 'monkey', 'cow']
        slot1 = slots[random.randint(0, 5)]
        slot2 = slots[random.randint(0, 5)]
        slot3 = slots[random.randint(0, 5)]
        slotOutput = '| :{}: | :{}: | :{}: |\n'.format(slot1, slot2, slot3)
        embed1 = nextcord.Embed(title = "Slots Machine", color = clr)
        embed1.add_field(name = "{}\nWon".format(slotOutput), value = f'You won {amount + amount} arency')
        embed1.set_footer(text=f"You have currently {check['money']} arency", icon_url=ctx.author.avatar.url)
        newBal1 = check['money'] + amount

        won = nextcord.Embed(title = "Slots Machine", color = clr)
        won.add_field(name = "{}\nWon".format(slotOutput), value = f'You won {amount + amount + amount} arency')
        won.set_footer(text=f"You have currently {check['money']} arency", icon_url=ctx.author.avatar.url)
        newBal2 = check['money'] + amount + amount + amount

        lost = nextcord.Embed(title = "Slots Machine", color = clr)
        lost.add_field(name = "{}\nLost".format(slotOutput), value = f'You lost {amount} arency')
        lost.set_footer(text=f"You have currently {check['money']} arency", icon_url=ctx.author.avatar.url)
        newBal3 = check['money'] - amount
        if slot1 == slot2 == slot3:
           await ctx.send(embedw=won)
           await cursor.update_one({"id": ctx.author.id}, {"$set": {"money": newBal1}})
           await ctx.send(embed=won)

        if slot1 == slot2:
          await cursor.update_one({"id": ctx.author.id}, {"$set": {"money": newBal2}})
          await ctx.send(embed=embed1)
        else:
          await ctx.send(embed = lost)
          await cursor.update_one({"id": ctx.author.id}, {"$set": {"money": newBal3}})
          return
def setup(client):
  client.add_cog(Slots(client))