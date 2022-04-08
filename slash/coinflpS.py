import nextcord
from nextcord.ext import commands
import random, config, main
from config import *
from main import *
from emoji import *

class CoinFlipS(commands.Cog):
  def __init__ (self, client):
    self.client = client
        
        
        
  @commands.cooldown(2, 30, commands.BucketType.user)
  @nextcord.slash_command(name='coin-flip', description='flip a coin')
  async def FlipS(
    self,
    intr: nextcord.Interaction,
    amount: int = nextcord.SlashOption(name='amount', description='Please entre a aount')
    
    ):
    rand_flip = [2, 1, 0, 3, 4, 5]
    user = intr.user
    coinflip_check = await cursor.find_one({"id": user.id})
    pre = await predb.find_one({"guild": intr.guild.id})
    prefix = pre['prefix']
    if coinflip_check is None:
      await intr.response.send_message(f"You don't have a profile!\nPlease execute the `{prefix}create or /create` command to create a profile!")
    elif amount > 50000:
      await intr.response.send_message("You can't spin more than 50000 arency!")
    else:
      balance = coinflip_check['money']
                  
      embflip = nextcord.Embed(title=f"{user} spend <:CoinBlue:948794998952980500> {amount}!", description="<a:coin_blue_animate:948795258165141545> The coin spins...", colour=clr)
      embflip.set_footer(text="Spinning", icon_url=user.avatar.url)
      if balance <= 0:
        await intr.response.send_message("Your balance is too low!")
      elif balance < int(amount):
        await intr.response.send_message("Your balance is too low!")
                
                
                
      elif int(amount) < 1:
        await intr.response.send_message("**You cant do that**!")
                        
      elif random.choice(rand_flip) == 1:
        await intr.response.send_message(embed=embflip, delete_after=5)
        await asyncio.sleep(5)
        emb1edit = nextcord.Embed(title=f"U had your luck !!", description=f"<:CoinBlue:948794998952980500> The coin spins and you won {int(amount) + int(amount)} {arency}", colour=clr)
        emb1edit.set_footer(text=f"U had your luck", icon_url=user.avatar.url)
        await intr.channel.send(embed=emb1edit)
        NewBal = coinflip_check['money'] + int(amount)
        await cursor.update_one({"id": user.id}, {"$set": {"money": NewBal}})
      elif random.choice(rand_flip) == 2:
                        
        await intr.response.send_message(embed=embflip, delete_after=5)
        await asyncio.sleep(5)
        emb2edit = nextcord.Embed(title=f"Better luck next time !!", description=f"<:CoinBlue:948794998952980500> The coin spins and you lost all", colour=clr)
        emb2edit.set_footer(text=f"Bettter luck next time", icon_url=user.avatar.url)
        await intr.channel.send(embed=emb2edit)
        NewBal2 = coinflip_check['money'] - int(amount)
        await cursor.update_one({"id": user.id}, {"$set": {"money": NewBal2}})
      elif random.choice(rand_flip) == 3:
        await intr.response.send_message(embed=embflip, delete_after=5)
        await asyncio.sleep(5)
        emb3edit = nextcord.Embed(title=f"U had your luck !!", description=f"<:CoinBlue:948794998952980500> The coin spins and you won {amount} {arency}", colour=clr)
        emb3edit.set_footer(text=f"U had your luck", icon_url=user.avatar.url)
        await intr.channel.send(embed=emb3edit)
                
      elif random.choice(rand_flip) == 4:
        await intr.response.send_message(embed=embflip, delete_after=5)
        await asyncio.sleep(5)
        emb4edit = nextcord.Embed(title=f"U had your luck !!", description=f"<:CoinBlue:948794998952980500> The coin spins and you won {amount} {arency}", colour=clr)
        emb4edit.set_footer(text=f"U had your luck", icon_url=user.avatar.url)
        await intr.channel.send(embed=emb4edit)
              
      elif random.choice(rand_flip) == 5:
        await intr.response.send_message(embed=embflip, delete_after=5)
        await asyncio.sleep(5)
        emb5edit = nextcord.Embed(title=f"U had your luck !!", description=f"<:CoinBlue:948794998952980500> The coin spins and you won {amount} {arency}", colour=clr)
        emb5edit.set_footer(text=f"U had your luck", icon_url=user.avatar.url)
        await intr.channel.send(embed=emb5edit)
      elif random.choice(rand_flip) == 0:
        await intr.response.send_message(embed=embflip, delete_after=5)
        await asyncio.sleep(5)
        emb6edit = nextcord.Embed(title=f"Better luck next time !!", description=f"<:CoinBlue:948794998952980500> The coin spins and you lost all", colour=clr)
        emb6edit.set_footer(text=f"Bettter luck next time", icon_url=user.avatar.url)
        await intr.channel.send(embed=emb6edit)
        NewBal6 = coinflip_check['money'] - int(amount)
        await cursor.update_one({"id": user.id}, {"$set": {"money": NewBal6}})


        
def setup(client):
    client.add_cog(CoinFlipS(client))