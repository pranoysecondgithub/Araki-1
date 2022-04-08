import nextcord
from nextcord.ext import commands
from emo_config import *
from main import *
from config import *

class EmotesS(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @nextcord.slash_command(name='blush', description='This is blush command')
    async def BlushS(
        self,
        interaction:nextcord.Interaction
    ):
        Blush_img = random.choice(blush)
        embed = nextcord.Embed(title=f"{interaction.user.name} is blushing! cute", colour=clr)
        embed.set_image(url=Blush_img)
        await interaction.response.send_message(embed=embed)
        
    @nextcord.slash_command(name='cry', description='This is cry command')
    async def CryS(
        self,
        interaction:nextcord.Interaction
    ):
        Cry_img = random.choice(cry)
        embed = nextcord.Embed(title=f"{interaction.user.name}'s cries...:'c", colour=clr)
        embed.set_image(url=Cry_img)
        await interaction.response.send_message(embed=embed)
        
    @nextcord.slash_command(name='smile', description='This is smile command')
    async def SmileS(
        self,
        interaction:nextcord.Interaction
    ):
        Smile_img = random.choice(smile)
        embed = nextcord.Embed(title=f"{interaction.user.name} has a grin!!", colour=clr)
        embed.set_image(url=Smile_img)
        await interaction.response.send_message(embed=embed)
        
        
    @nextcord.slash_command(name='dance', description='This is dancing command')
    async def DanceS(
        self,
        interaction:nextcord.Interaction
    ):
        Dance_img = random.choice(dance)
        embed = nextcord.Embed(title=f"{interaction.user.name} loves to dance!", colour=clr)
        embed.set_image(url=Dance_img)
        await interaction.response.send_message(embed=embed)
        
        
    @nextcord.slash_command(name='sleepy', description='This is sleepy command')
    async def SleepyS(
        self,
        interaction:nextcord.Interaction
    ):
        Sleep_img = random.choice(sleepy)
        embed = nextcord.Embed(title=f"{interaction.user.name} is tired...", colour=clr)
        embed.set_image(url=Sleep_img)
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name='thinking', description='This is thinking command')
    async def ThinkingS(
        self,
        interaction:nextcord.Interaction
    ):
        Thinking_img = random.choice(thinking)
        embed = nextcord.Embed(title=f"{interaction.user.name} is thinking...", colour=clr)
        embed.set_image(url=Thinking_img)
        await interaction.response.send_message(embed=embed)
    
    @nextcord.slash_command(name='triggered', description='This is triggered command')
    async def TriggeredS(
        self,
        interaction:nextcord.Interaction
    ):
        Triggered_img = random.choice(trigger)
        embed = nextcord.Embed(title=f"{interaction.user.name} is triggered...", colour=clr)
        embed.set_image(url=Triggered_img)
        await interaction.response.send_message(embed=embed)
def setup(client):
    client.add_cog(EmotesS(client))