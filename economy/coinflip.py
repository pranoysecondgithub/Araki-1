import nextcord
from nextcord.ext import commands
import random, config, main
from config import *
from main import *
from emoji import *

class CoinFlip(commands.Cog):
  def __init__ (self, client):
    self.client = client
    
    
    
  @commands.cooldown(2, 20, commands.BucketType.user)
  @commands.command(aliases=['Coinflip', 'cf', 'f'])
  async def Flip(self, ctx, amount = "1", ht = 'heads'):
    rand_flip = [2, 1, 0, 3, 4, 5]
    user = ctx.author
    coinflip_check = await cursor.find_one({"id": user.id})
    pre = await predb.find_one({"guild": ctx.guild.id})
    prefix = pre['prefix']
    if coinflip_check is None:
      await ctx.message.reply(f"You don't have a profile!\nPlease execute the `{prefix}create` command to create a profile!")
    else:
      balance = coinflip_check['money']
            
      embflip = nextcord.Embed(title=f"{ctx.author} spend <:CoinBlue:948794998952980500> {amount} and chose {ht}", description="<a:coin_blue_animate:948795258165141545> The coin spins...", colour=clr)
      embflip.set_footer(text="Spinning", icon_url=ctx.author.avatar.url)
      if balance <= 0:
        await ctx.reply("Your balance is too low!")
      elif balance < int(amount):
        await ctx.reply("Your balance is too low!")
        
      elif amount > "100000":
        await ctx.reply(f"You can't use more then {100000:,} arency to spin!")
        
        
      elif int(amount) < 1:
        await ctx.reply("**You cant do that**!")
                
      elif random.choice(rand_flip) == 1:
        message = await ctx.send(embed=embflip)
        await asyncio.sleep(5)
        emb1edit = nextcord.Embed(title=f"U had your luck !!", description=f"<:CoinBlue:948794998952980500> The coin spins and you won {int(amount) + int(amount)} {arency}", colour=clr)
        emb1edit.set_footer(text=f"U had your luck", icon_url=ctx.author.avatar.url)
        await message.edit(embed=emb1edit)
        NewBal = coinflip_check['money'] + int(amount)
        await cursor.update_one({"id": user.id}, {"$set": {"money": NewBal}})
                
      elif random.choice(rand_flip) == 2:
                
        message = await ctx.send(embed=embflip)
        await asyncio.sleep(5)
        emb2edit = nextcord.Embed(title=f"Better luck next time !!", description=f"<:CoinBlue:948794998952980500> The coin spins and you lost all", colour=clr)
        emb2edit.set_footer(text=f"Bettter luck next time", icon_url=ctx.author.avatar.url)
        await message.edit(embed=emb2edit)
        NewBal2 = coinflip_check['money'] - int(amount)
        await cursor.update_one({"id": user.id}, {"$set": {"money": NewBal2}})
      elif random.choice(rand_flip) == 3:
        message = await ctx.send(embed=embflip)
        await asyncio.sleep(5)
        emb3edit = nextcord.Embed(title=f"U had your luck !!", description=f"<:CoinBlue:948794998952980500> The coin spins and you won {amount} {arency}", colour=clr)
        emb3edit.set_footer(text=f"U had your luck", icon_url=ctx.author.avatar.url)
        await message.edit(embed=emb3edit)
        
      elif random.choice(rand_flip) == 4:
        message = await ctx.send(embed=embflip)
        await asyncio.sleep(5)
        emb4edit = nextcord.Embed(title=f"U had your luck !!", description=f"<:CoinBlue:948794998952980500> The coin spins and you won {amount} {arency}", colour=clr)
        emb4edit.set_footer(text=f"U had your luck", icon_url=ctx.author.avatar.url)
        await message.edit(embed=emb4edit)
      
      elif random.choice(rand_flip) == 5:
        message = await ctx.send(embed=embflip)
        await asyncio.sleep(5)
        emb5edit = nextcord.Embed(title=f"U had your luck !!", description=f"<:CoinBlue:948794998952980500> The coin spins and you won {amount} {arency}", colour=clr)
        emb5edit.set_footer(text=f"U had your luck", icon_url=ctx.author.avatar.url)
        await message.edit(embed=emb5edit)
      elif random.choice(rand_flip) == 0:
        message = await ctx.send(embed=embflip)
        await asyncio.sleep(5)
        emb6edit = nextcord.Embed(title=f"Better luck next time !!", description=f"<:CoinBlue:948794998952980500> The coin spins and you lost all", colour=clr)
        emb6edit.set_footer(text=f"Bettter luck next time", icon_url=ctx.author.avatar.url)
        await message.edit(embed=emb6edit)
        NewBal6 = coinflip_check['money'] - int(amount)
        await cursor.update_one({"id": user.id}, {"$set": {"money": NewBal6}})
          
  
def setup(client):
  client.add_cog(CoinFlip(client))