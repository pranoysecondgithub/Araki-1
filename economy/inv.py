from nextcord.ext import *
from main import *
from config import *
from emoji import *

class Inv(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
    @commands.command(aliases=['inv'])
    async def Inventory(self, ctx):
        find = await cursor.find_one({"id": ctx.author.id})
        pre = await predb.find_one({"guild": ctx.guild.id})
        prefix = pre['prefix']
        if find is None:
            await ctx.message.reply(f"You don't have a profile!\nPlease execute the `{prefix}create` command to create a profile!")
            return
        else:
            inv_find = await inv.find_one({"id": ctx.author.id})
            if inv_find is None:
                msg = await ctx.send(f"{loading} | Your inventory is blank!")
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
                await msg.edit(content=f"{success} | You successfully created your inventory! Run again this command to view your inventory!")
            else:
                embed = nextcord.Embed(description=f"To sell any item type {prefix}sell item_id", colour=clr)
                embed.set_author(name=f"{ctx.author.name}'s Inventory")

                Candy = await inv.find_one({"id": ctx.author.id, "name": 'Candy'})
                amt1 = Candy['amount']
                embed.add_field(name=f":candy: Candy -- {amt1}", value=f"ID -- candy")

                Fish = await inv.find_one({"id": ctx.author.id,"name": 'Fish'})
                amt2 = Fish['amount']
                embed.add_field(name=f":fish: Fish -- {amt2}", value=f"ID -- fish")

                Cookie = await inv.find_one({"id": ctx.author.id, "name": 'Cookie'})
                amt3 = Cookie['amount']
                embed.add_field(name=f":cookie: Cookie -- {amt3}", value=f"ID -- cookie")

                Rose = await inv.find_one({"id": ctx.author.id, "name": 'Rose'})
                amt4 = Rose['amount']
                embed.add_field(name=f":rose: Rose -- {amt4}", value=f"ID -- rose")

                Pizza = await inv.find_one({"id": ctx.author.id, "name": 'Pizza'})
                amt5 = Pizza['amount']
                embed.add_field(name=f":pizza: Pizza -- {amt5}", value=f"ID -- pizza")

                Frequent = await inv.find_one({"id": ctx.author.id, "name": 'Frequent Circlet'})
                amt6 = Frequent['amount']
                embed.add_field(name=f"<:frequentcirclet:949535577806626836> Frequent Circlet -- {amt6}", value=f"ID -- frequent")
                await ctx.send(embed=embed)
            
def setup(client):
    client.add_cog(Inv(client))