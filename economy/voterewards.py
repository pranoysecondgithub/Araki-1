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
            user_object = pranoy.get_user(int(user)) or await pranoy.fetch_user(int(user))
            user=user_object
            find = await cursor.find_one({"id": user_object.id})
            if find is None:
                return
            else:
                balance = find['money']
                newBal = balance + 1000
                await cursor.update_one({"id": user_object.id}, {"$set": {"money": newBal}})
                
                embed = nextcord.Embed(title="Thanks for voting!", description=f"You get 1000 arency for voting!", colour=clr)
                embed.set_footer(text=f"You can vote in every 12hr!")
                await user_object.send(embed=embed)
            
def setup(client):
    client.add_cog(VoteRewards(client))