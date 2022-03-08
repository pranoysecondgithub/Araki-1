import nextcord, motor, json, asyncio, random, config, main
from nextcord.ext.commands import BucketType, cooldown
from nextcord.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient
from config import *
from main import *

class Create(commands.Cog):
    def __init__(self, client):
        self.client = client
      
    # with open ("./data.json") as file:
    #   data = json.load(file)
  
    @commands.command()
    # @commands.is_owner()
    async def create(self, ctx):
        user = ctx.author
        
        check = await cursor.find_one({"id": user.id})
      
        if check is None:
            insert = {
                "id": user.id,
                "name": user.name,
                "tags": user.discriminator,
                "money": 100
            }
          
            await cursor.insert_one(insert)
          
            await ctx.message.reply("You have successfully created a profile!")
            return
        
        else:
            await ctx.message.reply("You have an existing profile!")
def setup(client):
    client.add_cog(Create(client))