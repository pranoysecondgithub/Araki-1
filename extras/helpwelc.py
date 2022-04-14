import nextcord, main, config, emoji
from nextcord.ext import commands
from config import *
from main import *
from emoji import *

class HelpWelcome(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.command(aliases=['help config', 'config-help'])
  async def Config(self, ctx):
    prefix = await predb.find_one({"guild": ctx.guild.id})
    pre = prefix['prefix']
    embed = nextcord.Embed(title='Setprefix', description='It will change the server prefix.', colour=clr)
    embed.add_field(name=f"{pre}set-welcome", value="It will set the welcome channel for you")
    embed.add_field(name=f"{pre}remove-welcome", value="It will remove the welcome channel for you")
    embed.add_field(name=f"{pre}set-leave", value="It will set the leave channel for you")
    embed.add_field(name=f"{pre}remove-leave", value="It will remove the leave channel for you")    
    embed.set_footer(text=footer, icon_url=ctx.author.avatar.url)
    embed.set_author(name="Config help.", icon_url=ctx.author.avatar.url)
    await ctx.send(embed=embed)

  @commands.command()
  async def welcome(self, ctx):
    embed = nextcord.Embed(title='Welcome Setup', description='Well these are the few steps that you can setup welcome easyly.', colour=clr)
    embed.add_field(name='Variables', value="``[user]``` Mentions the new member.\n```[userName]``` New member name without mentioning\n```[memberCount]``` Amount of members reached\n```[server]``` Server name\n")
    embed.add_field(name='Welcome setup commands', value='```\nenable-welcome, Set-welcome, welcome-author, welcome-author-icon, welcome-title, welcome-description, welcome-thumbnail, welcome-image, welcome-footer, welcome-footer-icon\n```')
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)
def setup(client):
  client.add_cog(HelpWelcome(client))
