from nextcord.ext import commands
from main import *
from config import *
import re

class VoteRewards(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_message(self, message):
        
        if message.channel.id == 952278017571442750:
            data = message.content.split(" ")
            user = re.sub("\D", "", data[4])
             
            user_object = pranoy.get_user(user) or await pranoy.fetch_user(user)
            user=user_object
            find = await cursor.find_one({"id": user.id})
            inv_find = await inv.find_one({"id": user.id, "name": 'Fish'})
            embed = nextcord.Embed(title="Thanks for voting!", description=f"You can vote in every 12hr!", colour=clr)
            if find is None:
                return
            else:
                balance = find['money']
                newBal = balance + 1000

                await cursor.update_one({"id": user.id}, {"$set": {"money": newBal}})
                embed.add_field(name="Arency", value="1000 Arency added to your wallet for voting!")
                
                embed.set_footer(text=f"You can vote in every 12hr!")
                await user_object.send(embed=embed)
            if inv_find is None:
              return
            else:
                newAmt = inv_find['amount'] + 1
                await inv.update_one({"id": user.id, "name": 'Fish'}, {"$set": {"amount": newAmt}})
                embed.add_field(name='Inventory', value='1x Fish added to your inventory for voting!')
            embed.set_footer(text=f"You can vote in every 12hr!")

            await user_object.send(embed=embed)
def setup(client):
    client.add_cog(VoteRewards(client))