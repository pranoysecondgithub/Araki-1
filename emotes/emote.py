import nextcord
from nextcord.ext import commands
from emo_config import *
from main import *
from config import *

class Emotes(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def Blush(self, ctx):
        Blush_img = random.choice(blush)
        embed = nextcord.Embed(title=f"{ctx.author.name} is blushing! cute", colour=clr)
        embed.set_image(url=Blush_img)
        await ctx.send(embed=embed)
        
    @commands.command()
    async def Cry(self, ctx):
        Cry_img = random.choice(cry)
        embed = nextcord.Embed(title=f"{ctx.author.name}'s cries...:'c", colour=clr)
        embed.set_image(url=Cry_img)
        await ctx.send(embed=embed)
        
    @commands.command()
    async def Smile(self, ctx):
        Smile_img = random.choice(smile)
        embed = nextcord.Embed(title=f"{ctx.author.name} has a grin!!", colour=clr)
        embed.set_image(url=Smile_img)
        await ctx.send(embed=embed)
        
        
    @commands.command()
    async def Dance(self, ctx):
        Dance_img = random.choice(dance)
        embed = nextcord.Embed(title=f"{ctx.author.name} loves to dance!", colour=clr)
        embed.set_image(url=Dance_img)
        await ctx.send(embed=embed)
        
        
    @commands.command()
    async def Sleepy(self, ctx):
        Sleep_img = random.choice(sleepy)
        embed = nextcord.Embed(title=f"{ctx.author.name} is tired...", colour=clr)
        embed.set_image(url=Sleep_img)
        await ctx.send(embed=embed)

    @commands.command()
    async def Thinking(self, ctx):
        Thinking_img = random.choice(thinking)
        embed = nextcord.Embed(title=f"{ctx.author.name} is thinking...", colour=clr)
        embed.set_image(url=Thinking_img)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def Triggered(self, ctx):
        Triggered_img = random.choice(trigger)
        embed = nextcord.Embed(title=f"{ctx.author.name} is triggered...", colour=clr)
        embed.set_image(url=Triggered_img)
        await ctx.send(embed=embed)
def setup(client):
    client.add_cog(Emotes(client))