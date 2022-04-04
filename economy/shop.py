from nextcord.ext import commands
from main import *
from config import *
from emoji import *

class Shop(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @commands.command()
    async def Shop(self, ctx):
        pre = await predb.find_one({"guild": ctx.guild.id})
        prefix = pre['prefix']
        embed = nextcord.Embed( colour=clr)
        embed.set_author(name=f"{ctx.author.name}'s Inventory")
        embed.set_footer(text=f"To check your inventory type {prefix}inv", icon_url=ctx.author.avatar.url)
        embed.add_field(name=f":candy: Candy -- 1000 | {arency}", value=f"To buy this item type ```{prefix}buy candy```")
        embed.add_field(name=f":fish: Fish -- 5000 | {arency}", value=f"To buy this item type ```{prefix}buy fish```")
        embed.add_field(name=f":cookie: Cookie -- 50000 | {arency}", value=f"To buy this item type ```{prefix}buy cookie```")
        embed.add_field(name=f":rose: Rose -- 70000 | {arency}", value=f"To buy this item type ```{prefix}buy rose```")
        embed.add_field(name=f":pizza: Pizza -- 100000 | {arency}", value=f"To buy this item type ```{prefix}buy pizza```")
        embed.add_field(name=f"<:frequentcirclet:949535577806626836> Frequent Circlet -- 1000000 | {arency}", value=f"To buy this item type ```{prefix}buy frequent```")
        await ctx.send(embed=embed)

    @nextcord.slash_command(name='shop', description='View the shop')
    async def Shop(self, ctx:nextcord.Interaction):
        pre = await predb.find_one({"guild": ctx.guild.id})
        prefix = pre['prefix']
        embed = nextcord.Embed( colour=clr)
        embed.set_author(name=f"{ctx.user.name}'s Inventory")
        embed.set_footer(text=f"To check your inventory type {prefix}inv", icon_url=ctx.user.avatar.url)
        embed.add_field(name=f":candy: Candy -- 1000 | {arency}", value=f"To buy this item type ```{prefix}buy candy```")
        embed.add_field(name=f":fish: Fish -- 5000 | {arency}", value=f"To buy this item type ```{prefix}buy fish```")
        embed.add_field(name=f":cookie: Cookie -- 50000 | {arency}", value=f"To buy this item type ```{prefix}buy cookie```")
        embed.add_field(name=f":rose: Rose -- 70000 | {arency}", value=f"To buy this item type ```{prefix}buy rose```")
        embed.add_field(name=f":pizza: Pizza -- 100000 | {arency}", value=f"To buy this item type ```{prefix}buy pizza```")
        embed.add_field(name=f"<:frequentcirclet:949535577806626836> Frequent Circlet -- 1000000 | {arency}", value=f"To buy this item type ```{prefix}buy frequent```")
        await ctx.response.send_message(embed=embed)
    
    @commands.command()
    async def Buy(self, ctx, item = None):
        if item == None:
            await ctx.reply("Please entre a item id!")
        find = await cursor.find_one({"id": ctx.author.id})
        pre = await predb.find_one({"guild": ctx.guild.id})
        prefix = pre['prefix']
        inv_find = await inv.find_one({"id": ctx.author.id})
        if find is None:
            await ctx.message.reply(f"You don't have a profile!\nPlease execute the `{prefix}create` command to create a profile!")
            return
        else:
            bal_find = await cursor.find_one({"id": ctx.author.id})
            balance = bal_find['money']
            if inv_find is None:
                insert = {"id": ctx.author.id, "name": 'Candy', "amount": 0}
                insert2 = {"id": ctx.author.id, "name": 'Fish', "amount": 0}
                insert3 = {"id": ctx.author.id, "name": 'Cookie', "amount": 0}
                insert4 = {"id": ctx.author.id, "name": 'Rose', "amount": 0}
                insert5 = {"id": ctx.author.id, "name": 'Pizza', "amount": 0}
                insert6 = {"id": ctx.author.id, "name": 'Frequent Circlet', "amount": 0}
                await inv.insert_one(insert)
                await inv.insert_one(insert2)
                await inv.insert_one(insert3)
                await inv.insert_one(insert4)
                await inv.insert_one(insert5)
                await inv.insert_one(insert6)
                if item == "candy":
                    if balance > 999:
                        candy_find = await inv.find_one({"id": ctx.author.id, "name": 'Candy'})
                        newAmt = candy_find['amount'] + 1
                        newBal = int(balance) - 1000
                        await cursor.update_one({"id": ctx.author.id}, {"$set": {"money": newBal}})
                        await inv.update_one({"id": ctx.author.id, "name": 'Candy'}, {"$set": {"amount": newAmt}})
                        await ctx.send(f"{success} | You bought 1x candy")
                    else:
                        await ctx.reply("You dont have arency to buy this item!")
                        
                if item == "fish":
                        if balance > 4999:
                            fish_find = await inv.find_one({"id": ctx.author.id, "name": 'Fish'})
                            newAmt = fish_find['amount'] + 1
                            newBal = balance - 5000
                            await cursor.update_one({"id": ctx.author.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.author.id, "name": 'Fish'}, {"$set": {"amount": newAmt}})
                            await ctx.send(f"{success} | You bought 1x fish")
                        else:
                            await ctx.reply("You dont have arency to buy this item!")
                if item == "cookie":
                        if balance > 4999:
                            cookie_find = await inv.find_one({"id": ctx.author.id, "name": 'Cookie'})
                            newAmt = cookie_find['amount'] + 1
                            newBal = balance - 5000
                            await cursor.update_one({"id": ctx.author.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.author.id, "name": 'Cookie'}, {"$set": {"amount": newAmt}})
                            await ctx.send(f"{success} | You bought 1x Cookie")
                   
                        else:
                            await ctx.reply("You dont have arency to buy this item!")
                
                if item == "rose":
                        if balance > 69999:
                            rose_find = await inv.find_one({"id": ctx.author.id, "name": 'Rose'})
                            newAmt = rose_find['amount'] + 1
                            newBal = balance - 70000
                            await cursor.update_one({"id": ctx.author.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.author.id, "name": 'Rose'}, {"$set": {"amount": newAmt}})
                            await ctx.send(f"{success} | You bought 1x Rose")
                    
                        else:
                            await ctx.reply("You dont have arency to buy this item!")
                
                if item == "pizza":
                        if balance > 99999:
                            pizza_find = await inv.find_one({"id": ctx.author.id, "name": 'Pizza'})
                            newAmt = pizza_find['amount'] + 1
                            newBal = balance - 100000
                            await cursor.update_one({"id": ctx.author.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.author.id, "name": 'Pizza'}, {"$set": {"amount": newAmt}})
                            await ctx.send(f"{success} | You bought 1x Pizza")
                    
                        else:
                            await ctx.reply("You dont have arency to buy this item!")
                    
                if item == "frequent":
                        if balance > 999999:
                            freq_find = await inv.find_one({"id": ctx.author.id, "name": 'Frequent Circlet'})
                            newAmt = freq_find['amount'] + 1
                            newBal = balance - 1000000
                            await cursor.update_one({"id": ctx.author.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.author.id, "name": 'Frequent Circlet'}, {"$set": {"amount": newAmt}})
                            await ctx.send(f"{success} | You bought 1x Frequent Circlet")
                    
                        else:
                            await ctx.reply("You dont have arency to buy this item!")
            #2ns
            else:
                if item == "candy":
                    if balance > 999:
                        candy_find = await inv.find_one({"id": ctx.author.id, "name": 'Candy'})
                        newAmt = candy_find['amount'] + 1
                        newBal = balance - 1000
                        await cursor.update_one({"id": ctx.author.id}, {"$set": {"money": newBal}})
                        await inv.update_one({"id": ctx.author.id,"name": 'Candy'}, {"$set": {"amount": newAmt}})
                        await ctx.send(f"{success} | You bought 1x Candy")
                    else:
                        await ctx.reply("You dont have arency to buy this item!")
                        
                if item == "fish":
                        if balance > 4999:
                            fish_find = await inv.find_one({"id": ctx.author.id, "name": 'Fish'})
                            newAmt = fish_find['amount'] + 1
                            newBal = balance - 5000
                            await cursor.update_one({"id": ctx.author.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.author.id, "name": 'Fish'}, {"$set": {"amount": newAmt}})
                            await ctx.send(f"{success} | You bought 1x Fish")
                    
                        else:
                            await ctx.reply("You dont have arency to buy this item!")
                
                if item == "cookie":
                        if balance > 4999:
                            cookie_find = await inv.find_one({"id": ctx.author.id, "name": 'Cookie'})
                            newAmt = cookie_find['amount'] + 1
                            newBal = balance - 5000
                            await cursor.update_one({"id": ctx.author.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.author.id, "name": 'Cookie'}, {"$set": {"amount": newAmt}})
                            await ctx.send(f"{success} | You bought 1x Cookie")
                    
                        else:
                            await ctx.reply("You dont have arency to buy this item!")
                
                if item == "rose":
                        if balance > 69999:
                            rose_find = await inv.find_one({"id": ctx.author.id, "name": 'Rose'})
                            newAmt = rose_find['amount'] + 1
                            newBal = balance - 70000
                            await cursor.update_one({"id": ctx.author.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.author.id, "name": 'Rose'}, {"$set": {"amount": newAmt}})
                            await ctx.send(f"{success} | You bought 1x Rose")
                    
                        else:
                            await ctx.reply("You dont have arency to buy this item!")
                    
                if item == "pizza":
                        if balance > 99999:
                            pizza_find = await inv.find_one({"id": ctx.author.id, "name": 'Pizza'})
                            newAmt = pizza_find['amount'] + 1
                            newBal = balance - 100000
                            await cursor.update_one({"id": ctx.author.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.author.id, "name": 'Pizza'}, {"$set": {"amount": newAmt}})
                            await ctx.send(f"{success} | You bought 1x Pizza")
                    
                        else:
                            await ctx.reply("You dont have arency to buy this item!")
                    
                if item == "frequent":
                        if balance > 999999:
                            freq_find = await inv.find_one({"id": ctx.author.id, "name": 'Frequent Circlet'})
                            newAmt = freq_find['amount'] + 1
                            newBal = balance - 1000000
                            await cursor.update_one({"id": ctx.author.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.author.id, "name": 'Frequent Circlet'}, {"$set": {"amount": newAmt}})
                            await ctx.send(f"{success} | You bought 1x Frequent Circlet")
                    
                        else:
                            await ctx.reply("You dont have arency to buy this item!")

    @nextcord.slash_command(name='buy', description='Buy a item')
    async def Buys(
        self,
        ctx:nextcord.Interaction,
        item: str = nextcord.SlashOption(name='item-id', description='Please provide a item id.')

        ):
        find = await cursor.find_one({"id": ctx.user.id})
        pre = await predb.find_one({"guild": ctx.guild.id})
        prefix = pre['prefix']
        inv_find = await inv.find_one({"id": ctx.user.id})
        if find is None:
            await ctx.response.send_message(f"You don't have a profile!\nPlease execute the `{prefix}create or /create` command to create a profile!", ephemeral=True)
            return
        else:
            bal_find = await cursor.find_one({"id": ctx.user.id})
            balance = bal_find['money']
            if inv_find is None:
                insert = {"id": ctx.user.id, "name": 'Candy', "amount": 0}
                insert2 = {"id": ctx.user.id, "name": 'Fish', "amount": 0}
                insert3 = {"id": ctx.user.id, "name": 'Cookie', "amount": 0}
                insert4 = {"id": ctx.user.id, "name": 'Rose', "amount": 0}
                insert5 = {"id": ctx.user.id, "name": 'Pizza', "amount": 0}
                insert6 = {"id": ctx.user.id, "name": 'Frequent Circlet', "amount": 0}
                await inv.insert_one(insert)
                await inv.insert_one(insert2)
                await inv.insert_one(insert3)
                await inv.insert_one(insert4)
                await inv.insert_one(insert5)
                await inv.insert_one(insert6)
                if item == "candy":
                    if balance > 999:
                        candy_find = await inv.find_one({"id": ctx.user.id, "name": 'Candy'})
                        newAmt = candy_find['amount'] + 1
                        newBal = int(balance) - 1000
                        await cursor.update_one({"id": ctx.user.id}, {"$set": {"money": newBal}})
                        await inv.update_one({"id": ctx.user.id, "name": 'Candy'}, {"$set": {"amount": newAmt}})
                        await ctx.response.send_message(f"{success} | You bought 1x candy")
                    else:
                        await ctx.response.send_message("You dont have arency to buy this item!")
                        
                if item == "fish":
                        if balance > 4999:
                            fish_find = await inv.find_one({"id": ctx.user.id, "name": 'Fish'})
                            newAmt = fish_find['amount'] + 1
                            newBal = balance - 5000
                            await cursor.update_one({"id": ctx.user.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.user.id, "name": 'Fish'}, {"$set": {"amount": newAmt}})
                            await ctx.response.send_message(f"{success} | You bought 1x fish")
                        else:
                            await ctx.response.send_message("You dont have arency to buy this item!")
                if item == "cookie":
                        if balance > 4999:
                            cookie_find = await inv.find_one({"id": ctx.user.id, "name": 'Cookie'})
                            newAmt = cookie_find['amount'] + 1
                            newBal = balance - 5000
                            await cursor.update_one({"id": ctx.user.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.user.id, "name": 'Cookie'}, {"$set": {"amount": newAmt}})
                            await ctx.response.send_message(f"{success} | You bought 1x Cookie")
                   
                        else:
                            await ctx.response.send_message("You dont have arency to buy this item!")
                
                if item == "rose":
                        if balance > 69999:
                            rose_find = await inv.find_one({"id": ctx.user.id, "name": 'Rose'})
                            newAmt = rose_find['amount'] + 1
                            newBal = balance - 70000
                            await cursor.update_one({"id": ctx.user.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.user.id, "name": 'Rose'}, {"$set": {"amount": newAmt}})
                            await ctx.response.send_message(f"{success} | You bought 1x Rose")
                    
                        else:
                            await ctx.response.send_message("You dont have arency to buy this item!")
                
                if item == "pizza":
                        if balance > 99999:
                            pizza_find = await inv.find_one({"id": ctx.user.id, "name": 'Pizza'})
                            newAmt = pizza_find['amount'] + 1
                            newBal = balance - 100000
                            await cursor.update_one({"id": ctx.user.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.user.id, "name": 'Pizza'}, {"$set": {"amount": newAmt}})
                            await ctx.response.send_message(f"{success} | You bought 1x Pizza")
                    
                        else:
                            await ctx.response.send_message("You dont have arency to buy this item!")
                    
                if item == "frequent":
                        if balance > 999999:
                            freq_find = await inv.find_one({"id": ctx.user.id, "name": 'Frequent Circlet'})
                            newAmt = freq_find['amount'] + 1
                            newBal = balance - 1000000
                            await cursor.update_one({"id": ctx.user.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.user.id, "name": 'Frequent Circlet'}, {"$set": {"amount": newAmt}})
                            await ctx.response.send_message(f"{success} | You bought 1x Frequent Circlet")
                    
                        else:
                            await ctx.response.send_message("You dont have arency to buy this item!")
            #2ns
            else:
                if item == "candy":
                    if balance > 999:
                        candy_find = await inv.find_one({"id": ctx.user.id, "name": 'Candy'})
                        newAmt = candy_find['amount'] + 1
                        newBal = balance - 1000
                        await cursor.update_one({"id": ctx.user.id}, {"$set": {"money": newBal}})
                        await inv.update_one({"id": ctx.user.id,"name": 'Candy'}, {"$set": {"amount": newAmt}})
                        await ctx.response.send_message(f"{success} | You bought 1x Candy")
                    else:
                        await ctx.response.send_message("You dont have arency to buy this item!")
                        
                if item == "fish":
                        if balance > 4999:
                            fish_find = await inv.find_one({"id": ctx.user.id, "name": 'Fish'})
                            newAmt = fish_find['amount'] + 1
                            newBal = balance - 5000
                            await cursor.update_one({"id": ctx.user.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.user.id, "name": 'Fish'}, {"$set": {"amount": newAmt}})
                            await ctx.response.send_message(f"{success} | You bought 1x Fish")
                    
                        else:
                            await ctx.response.send_message("You dont have arency to buy this item!")
                
                if item == "cookie":
                        if balance > 4999:
                            cookie_find = await inv.find_one({"id": ctx.user.id, "name": 'Cookie'})
                            newAmt = cookie_find['amount'] + 1
                            newBal = balance - 5000
                            await cursor.update_one({"id": ctx.user.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.user.id, "name": 'Cookie'}, {"$set": {"amount": newAmt}})
                            await ctx.response.send_message(f"{success} | You bought 1x Cookie")
                    
                        else:
                            await ctx.response.send_message("You dont have arency to buy this item!")
                
                if item == "rose":
                        if balance > 69999:
                            rose_find = await inv.find_one({"id": ctx.user.id, "name": 'Rose'})
                            newAmt = rose_find['amount'] + 1
                            newBal = balance - 70000
                            await cursor.update_one({"id": ctx.user.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.user.id, "name": 'Rose'}, {"$set": {"amount": newAmt}})
                            await ctx.response.send_message(f"{success} | You bought 1x Rose")
                    
                        else:
                            await ctx.response.send_message("You dont have arency to buy this item!")
                    
                if item == "pizza":
                        if balance > 99999:
                            pizza_find = await inv.find_one({"id": ctx.user.id, "name": 'Pizza'})
                            newAmt = pizza_find['amount'] + 1
                            newBal = balance - 100000
                            await cursor.update_one({"id": ctx.user.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.user.id, "name": 'Pizza'}, {"$set": {"amount": newAmt}})
                            await ctx.response.send_message(f"{success} | You bought 1x Pizza")
                    
                        else:
                            await ctx.response.send_message("You dont have arency to buy this item!")
                    
                if item == "frequent":
                        if balance > 999999:
                            freq_find = await inv.find_one({"id": ctx.user.id, "name": 'Frequent Circlet'})
                            newAmt = freq_find['amount'] + 1
                            newBal = balance - 1000000
                            await cursor.update_one({"id": ctx.user.id}, {"$set": {"money": newBal}})
                            await inv.update_one({"id": ctx.user.id, "name": 'Frequent Circlet'}, {"$set": {"amount": newAmt}})
                            await ctx.response.send_message(f"{success} | You bought 1x Frequent Circlet")
                    
                        else:
                            await ctx.response.send_message("You dont have arency to buy this item!")
                
def setup(client):
    client.add_cog(Shop(client))