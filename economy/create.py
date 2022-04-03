import nextcord, motor, json, asyncio, random, config, main
from nextcord.ext.commands import BucketType, cooldown
from nextcord.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient
from config import *
from main import *
from nextcord.ui import Button, View


class CreateS(commands.Cog):
    def __init__(self, client):
        self.client = client
      
    # with open ("./data.json") as file:
    #   data = json.load(file)
  
    @nextcord.slash_command(name="create", description="Create a profile")
    # @commands.is_owner()
    async def createS(self, intr:nextcord.Interaction):
        user = intr.user
        
        check = await cursor.find_one({"id": user.id})
      
        if check is None:
            emblogin = nextcord.Embed(title="Araki Bot Rules", description='''Any actions performed to gain an unfair advantage over other users are explicitly against the rules. 
This includes but not limited to:Using macros/scripts for any commands
Using multiple accounts for any reason.

Do not use any exploits and report any bugs found in the bot

You can not sell/trade arency or any bot goods for anything outside of the bot

 If you have any questions or reswap lost amount Join our support server

Click on Accept to accept rules.''', colour=clr)
            class Accept1(nextcord.ui.View):
                def __init__(self):
                    super().__init__()
                    self.value = True
                @nextcord.ui.button(label="Accept", style=nextcord.ButtonStyle.green, emoji="👍")
                async def accept2(self, button: nextcord.ui.Button, intrbtn: nextcord.Interaction):
                    if intr.user.id == intrbtn.user.id:
                        user = intr.user
                        insert = {
                            "id": user.id,
                            "name": user.name,
                            "tags": user.discriminator,
                            "money": 100
                        }
                        button.disabled = True
                        await cursor.insert_one(insert)
                        await intrbtn.response.edit_message(view=self)
                        await intrbtn.channel.send("You have successfully created a profile!")
                    else:
                        await intr.response.send_message("This is not for you!", ephemeral=True)
            view = Accept1()
            await intr.respose.send_message(embed=emblogin, view=view)
            return
        
        else:
            await intr.response.send_message("You have an existing profile!")

    @commands.command()
    # @commands.is_owner()
    async def create(self, ctx):
        user = ctx.author
        
        check = await cursor.find_one({"id": user.id})
      
        if check is None:
            emblogin = nextcord.Embed(title="Araki Bot Rules", description='''Any actions performed to gain an unfair advantage over other users are explicitly against the rules. 
This includes but not limited to:Using macros/scripts for any commands
Using multiple accounts for any reason.

Do not use any exploits and report any bugs found in the bot

You can not sell/trade arency or any bot goods for anything outside of the bot

 If you have any questions or reswap lost amount Join our support server

Click on Accept to accept rules.''', colour=clr)
            class Accept2(nextcord.ui.View):
                def __init__(self):
                    super().__init__()
                    self.value = True
                @nextcord.ui.button(label="Accept", style=nextcord.ButtonStyle.green, emoji="👍")
                async def accept(self, button: nextcord.ui.Button, intr: nextcord.Interaction):
                    if ctx.user.id == intr.user.id:
                        user = intr.user
                        insert = {
                            "id": user.id,
                            "name": user.name,
                            "tags": user.discriminator,
                            "money": 100
                        }
                        button.disabled = True
                        await cursor.insert_one(insert)
                        await intr.response.edit_message(view=self)
                        await intr.channel.send("You have successfully created a profile!")
                    else:
                        await intr.response.send_message("This is not for you!", ephemeral=True)
            view = Accept2()
            await ctx.send(embed=emblogin, view=view)
            return
        
        else:
            await ctx.reply("You have an existing profile!")


def setup(client):
    client.add_cog(CreateS(client))