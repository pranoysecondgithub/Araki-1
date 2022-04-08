from nextcord.ext import *
from main import *
from config import *
from emoji import *

class Sell(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def Sell(self, ctx, item = None):
        find = await cursor.find_one({"id": ctx.author.id})
        pre = await predb.find_one({"guild": ctx.guild.id})
        prefix = pre['prefix']
        if item == None:
            await ctx.reply("Please entre a item id!")
        if find is None:
            await ctx.message.reply(f"You don't have a profile!\nPlease execute the `{prefix}create` command to create a profile!")
        else:
            bal = find['money']
            if item == "candy":
                inv_find = await inv.find_one({"id":ctx.author.id, "name": 'Candy'})
                amtold = inv_find['amount']
                if amtold > 0:
                    newamt = inv_find['amount'] - 1
                    await inv.update_one({"id":ctx.author.id, "name": 'Candy'}, {"$set": {"amount": newamt}})
                    newBal = bal + 700
                    await cursor.update_one({"id":ctx.author.id }, {"$set": {"money": newBal}})
                    
                    await ctx.send(f"{success} | You sold 1x {item}! and get 1000 {arency}.")
                else:
                    await ctx.reply(f"You dont have {item}")
                    
            if item == "fish":
                inv_find = await inv.find_one({"id":ctx.author.id, "name": 'Fish'})
                amtold2 = inv_find['amount']
                if amtold2 > 0:
                    newamt2 = inv_find['amount'] - 1
                    await inv.update_one({"id":ctx.author.id, "name": 'Fish'}, {"$set": {"amount": newamt2}})
                    newBal2 = bal + 3200
                    await cursor.update_one({"id":ctx.author.id }, {"$set": {"money": newBal2}})
                    
                    await ctx.send(f"{success} | You sold 1x {item}! and get 3200 {arency}.")
                else:
                    await ctx.reply(f"You dont have {item}")
                    
            if item == "cookie":
                inv_find = await inv.find_one({"id":ctx.author.id, "name": 'Cookie'})
                amtold3 = inv_find['amount']
                if amtold3 > 0:
                    newamt3 = inv_find['amount'] - 1
                    await inv.update_one({"id":ctx.author.id, "name": 'Cookie'}, {"$set": {"amount": newamt3}})
                    newBal3 = bal + 35000
                    await cursor.update_one({"id":ctx.author.id }, {"$set": {"money": newBal}})
                    
                    await ctx.send(f"{success} | You sold 1x {item}! and get 35000 {arency}.")
                else:
                    await ctx.reply(f"You dont have {item}")
                    
                    
            if item == "rose":
                inv_find = await inv.find_one({"id":ctx.author.id, "name": 'Rose'})
                amtold4 = inv_find['amount']
                if amtold4 > 0:
                    newamt4 = inv_find['amount'] - 1
                    await inv.update_one({"id":ctx.author.id, "name": 'Cookie'}, {"$set": {"amount": newamt4}})
                    newBal4 = bal + 49000
                    await cursor.update_one({"id":ctx.author.id }, {"$set": {"money": newBal4}})
                    
                    await ctx.send(f"{success} | You sold 1x {item}! and get 49000 {arency}.")
                else:
                    await ctx.reply(f"You dont have {item}")
                    
            if item == "rose":
                inv_find = await inv.find_one({"id":ctx.author.id, "name": 'Pizza'})
                amtold5 = inv_find['amount']
                if amtold5 > 0:
                    newamt5 = inv_find['amount'] - 1
                    await inv.update_one({"id":ctx.author.id, "name": 'Pizza'}, {"$set": {"amount": newamt5}})
                    newBal5 = bal + 69000
                    await cursor.update_one({"id":ctx.author.id }, {"$set": {"money": newBal5}})
                    
                    await ctx.send(f"{success} | You sold 1x {item}! and get 69000 {arency}.")
                else:
                    await ctx.reply(f"You dont have {item}")
                    
            if item == "frequent":
                inv_find = await inv.find_one({"id":ctx.author.id, "name": 'Frequent Circlet'})
                amtold6 = inv_find['amount']
                if amtold6 > 0:
                    newamt6 = inv_find['amount'] - 1
                    await inv.update_one({"id":ctx.author.id, "name": 'Frequent Circlet'}, {"$set": {"amount": newamt6}})
                    newBal6 = bal + 700000
                    await cursor.update_one({"id":ctx.author.id }, {"$set": {"money": newBal6}})
                    
                    await ctx.send(f"{success} | You sold 1x Frequent Circlet! and get 700000 {arency}.")
                else:
                    await ctx.reply(f"You dont have {item}")


    @nextcord.slash_command(name='sell', description='sell your items')
    async def SellS(
        self,
        intr:nextcord.Interaction,
        item: str = nextcord.SlashOption(name='item-id', description='Please provide a item id you want to sell!'
    )):
        find = await cursor.find_one({"id": intr.user.id})
        pre = await predb.find_one({"guild": intr.guild.id})
        prefix = pre['prefix']
        if find is None:
            await intr.response.send_message(f"You don't have a profile!\nPlease execute the `{prefix}create or /create` command to create a profile!")
        else:
            bal = find['money']
            if item == "candy":
                inv_find = await inv.find_one({"id": intr.user.id, "name": 'Candy'})
                amtold = inv_find['amount']
                if amtold > 0:
                    newamt = inv_find['amount'] - 1
                    await inv.update_one({"id": intr.user.id, "name": 'Candy'}, {"$set": {"amount": newamt}})
                    newBal = bal + 700
                    await cursor.update_one({"id":intr.user.id }, {"$set": {"money": newBal}})
                    await intr.response.send_message(f"{success} | You sold 1x {item}! and get 700 {arency}.")
                else:
                    await ctx.reply(f"You dont have {item}")
            if item == "fish":
                inv_find = await inv.find_one({"id":intr.user.id, "name": 'Fish'})
                amtold2 = inv_find['amount']
                if amtold2 > 0:
                    newamt2 = inv_find['amount'] - 1
                    await inv.update_one({"id":intr.user.id, "name": 'Fish'}, {"$set": {"amount": newamt2}})
                    newBal2 = bal + 3200
                    await cursor.update_one({"id":intr.user.id }, {"$set": {"money": newBal2}})
                    await intr.response.send_message(f"{success} | You sold 1x {item}! and get 3200 {arency}.")
                else:
                    await intr.response.send_message(f"You dont have {item}")
            if item == "cookie":
                inv_find = await inv.find_one({"id":intr.user.id, "name": 'Cookie'})
                amtold3 = inv_find['amount']
                if amtold3 > 0:
                    newamt3 = inv_find['amount'] - 1
                    await inv.update_one({"id":intr.user.id, "name": 'Cookie'}, {"$set": {"amount": newamt3}})
                    newBal3 = bal + 35000
                    await cursor.update_one({"id":intr.user.id }, {"$set": {"money": newBal}})
                    await intr.response.send_message(f"{success} | You sold 1x {item}! and get 35000 {arency}.")
                else:
                    await intr.response.send_message(f"You dont have {item}")
            if item == "rose":
                inv_find = await inv.find_one({"id":intr.user.id, "name": 'Rose'})
                amtold4 = inv_find['amount']
                if amtold4 > 0:
                    newamt4 = inv_find['amount'] - 1
                    await inv.update_one({"id":intr.user.id, "name": 'Cookie'}, {"$set": {"amount": newamt4}})
                    newBal4 = bal + 49000
                    await cursor.update_one({"id":intr.user.id }, {"$set": {"money": newBal4}})
                    await intr.response.send_message(f"{success} | You sold 1x {item}! and get 49000 {arency}.")
                else:
                    await intr.response.send_message(f"You dont have {item}")
            if item == "rose":
                inv_find = await inv.find_one({"id":intr.user.id, "name": 'Pizza'})
                amtold5 = inv_find['amount']
                if amtold5 > 0:
                    newamt5 = inv_find['amount'] - 1
                    await inv.update_one({"id":intr.user.id, "name": 'Pizza'}, {"$set": {"amount": newamt5}})
                    newBal5 = bal + 69000
                    await cursor.update_one({"id":intr.user.id }, {"$set": {"money": newBal5}})
                    await intr.response.send_message(f"{success} | You sold 1x {item}! and get 69000 {arency}.")
                else:
                    await intr.response.send_message(f"You dont have {item}")
            if item == "frequent":
                inv_find = await inv.find_one({"id":intr.user.id, "name": 'Frequent Circlet'})
                amtold6 = inv_find['amount']
                if amtold6 > 0:
                    newamt6 = inv_find['amount'] - 1
                    await inv.update_one({"id":intr.user.id, "name": 'Frequent Circlet'}, {"$set": {"amount": newamt6}})
                    newBal6 = bal + c
                    await cursor.update_one({"id":intr.user.id }, {"$set": {"money": newBal6}})
                    await intr.response.send_message(f"{success} | You sold 1x Frequent Circlet! and get 69000 {arency}.")
                else:
                    await intr.response.send_message(f"You dont have {item}")
                    
def setup(client):
    client.add_cog(Sell(client))