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
        pre = await predb.find_one({"guild": ctx.guild.id})
        prefix = pre['prefix']
        embed = nextcord.Embed(description=f"Here's a little bit of information! If you need help with commands, type ```{prefix}help.```", colour=clr)
        embed.add_field(name="Stats", value=f'Devloper :- [Pranoy#0140](https://discord.com/users/942683245106065448)\nTeam Members :- [! ADARSH 👑#2392](https://discord.com/users/609358846585995264), [Itz"Pritam2.0#5204](https://discord.com/users/595549200796745728), [Akshat..............?#0016](https://discord.com/users/921356594699182090), [! "Itz_SPIDEY" (•‿•)#8213](https://discord.com/users/715447259700920352)\nBot Uptime :- {days}d, {hours}h, {minutes}m, {seconds}s\nMemory Usage :- {psutil.virtual_memory().percent}%\nCPU Usage :- {psutil.cpu_percent()}%\nTotal Servers :- {len(pranoy.guilds)}\nTotal Users :- {len(pranoy.users)}')
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)

    @nextcord.slash_command(name='stats', description='Show the bot stats')
    async def StatsS(self, intr:nextcord.Interaction):
        delta_uptime = dt.datetime.utcnow() - pranoy.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        pre = await predb.find_one({"guild": intr.guild.id})
        prefix = pre['prefix']
        embed = nextcord.Embed(description=f"Here's a little bit of information! If you need help with commands, type ```{prefix}help.```", colour=clr)
        embed.add_field(name="Stats", value=f'Devloper :- [Pranoy#0140](https://discord.com/users/942683245106065448)\nTeam Members :- [! ADARSH 👑#2392](https://discord.com/users/609358846585995264), [Itz"Pritam2.0#5204](https://discord.com/users/595549200796745728), [Akshat..............?#0016](https://discord.com/users/921356594699182090), [! "Itz_SPIDEY" (•‿•)#8213](https://discord.com/users/715447259700920352)\nBot Uptime :- {days}d, {hours}h, {minutes}m, {seconds}s\nMemory Usage :- {psutil.virtual_memory().percent}%\nCPU Usage :- {psutil.cpu_percent()}%\nTotal Servers :- {len(pranoy.guilds)}\nTotal Users :- {len(pranoy.users)}')
        embed.set_footer(text=footer)
        await intr.response.send_message(embed=embed)
        
def setup(client):
    client.add_cog(Stats(client))