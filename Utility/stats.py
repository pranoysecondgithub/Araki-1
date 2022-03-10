import nextcord, config, main, psutil, datetime
from nextcord.ext import commands
from config import *
from main import *
from psutil import *


class Stats(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    @commands.command()
    async def Stats(self, ctx):
        delta_uptime = dt.datetime.utcnow() - pranoy.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        embed = nextcord.Embed(
            title=f"Python version",
            description="3.10.2",
            colour=clr
        )
        embed.add_field(name="Nextcord version", value="2.0.0a9", inline=True)
        embed.add_field(name="Devloper", value="Pranoy#0140", inline=True)
        embed.add_field(name="Team members", value='''! ADARSH 👑#2392\nItz"Pritam2.0#5204\nAkshat..............?#0016\n! "Itz_SPIDEY" (•‿•)#8213''', inline=True)
        embed.add_field(name="Bot Uptime", value=f"{days}d, {hours}h, {minutes}m, {seconds}s", inline=True)
        embed.add_field(name = 'Memory Usage', value = f'{psutil.virtual_memory().percent}%', inline = False)
        embed.add_field(name = 'CPU Usage', value = f'{psutil.cpu_percent()}%', inline = False)
        embed.set_author(name=f"{pranoy.user}'stats")
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)
        
def setup(client):
    client.add_cog(Stats(client))