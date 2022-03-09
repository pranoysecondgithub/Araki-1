import nextcord, main, config, emoji
from nextcord.ext import commands
from config import *
from main import *
from emoji import *

class HelpWelcome(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.command(aliases=['help welcome', 'welcome-help'])
  async def Welcome(self, ctx):
    prefix = await predb.find_one({"guild": ctx.guild.id})
    pre = prefix['prefix']
    embed = nextcord.Embed(title='Want help to setup welcome ?', description='This way you can setup welcome easyly.', colour=clr)
    embed.add_field(name=f"{pre}set-welcome", value="It will set the welcome channel for you")
    embed.add_field(name=f"{pre}remove-welcome", value="It will remove the welcome channel for you")
    embed.set_footer(text=footer, icon_url=ctx.author.avatar.url)
    await ctx.send(embed=embed)
      
def setup(client):
  client.add_cog(HelpWelcome(client))