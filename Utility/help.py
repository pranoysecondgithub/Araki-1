from nextcord.ext import commands
import nextcord
import os
import config
from config import *
from nextcord import ButtonStyle
from nextcord.ui import Button, View
import main
from main import *

class Dropdown(nextcord.ui.Select):
    def __init__(self):
      SelectOptions = [
        nextcord.SelectOption(label='Moderation', description='Show moderation commands', emoji='<:Admin:947068190901551116>'),
        nextcord.SelectOption(label='Economy', description='Show Economy commands', emoji='<:economy:948649700783960105>'),
        nextcord.SelectOption(label='Fun', description='Show the fun commands', emoji='<:fun:948144502940516412>'),
        nextcord.SelectOption(label='Config', description='Show the config commands', emoji='<:settings:947068267888013353>'),
        nextcord.SelectOption(label='Utility', description='Show the Utility commands', emoji='<:modd:947068138762166272>'),
      ]
      
      super().__init__(placeholder='Choose a command type...', min_values=1, max_values=1, options=SelectOptions)
    async def callback(self, interaction: nextcord.Interaction):
      Moderation = nextcord.Embed(title='Moderation commands', description='```Clear, Avatar, Mute, Unmute, Kick, Ban, Unban, Warn, Slowmode, Lock, Unlock```', colour=clr)
      Moderation.set_footer(text='Made by Pranoy#0140')

      Economy = nextcord.Embed(title='Economy commands', description='```Earn, Create, Arency, Work, Give, Coinflip, Slots```', colour=clr)
      Economy.set_footer(text='Made by Pranoy#0140')

      Fun = nextcord.Embed(title='Fun commands', description='```Meme, Cool, Gay, Penis, Poll, HeadOrTail```', colour=clr)
      Fun.set_footer(text='Made by Pranoy#0140')

      Config = nextcord.Embed(title='Config commands', description='```Config-help, Setprefix, Set-welcome, Remove-welcome, Set-leave, Remove-leave```', colour=clr)
      Config.set_footer(text='Made by Pranoy#0140')

      Utility = nextcord.Embed(title='Utility commands', description='```Poll, Serverinfo, Userinfo, Membercount, Invite, Vote, Stats```', colour=clr)
      Utility.set_footer(text='Made by Pranoy#0140')
      if self.values[0] == 'Moderation':
        await interaction.response.send_message(embed=Moderation, ephemeral=True)
      if self.values[0] == 'Economy':
        await interaction.response.send_message(embed=Economy, ephemeral=True)
      if self.values[0] == 'Fun':
        await interaction.response.send_message(embed=Fun, ephemeral=True)
      if self.values[0] == 'Config':
        await interaction.response.send_message(embed=Config, ephemeral=True)
      if self.values[0] == 'Utility':
        await interaction.response.send_message(embed=Utility, ephemeral=True)

class DropdownView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())

class HelpPage(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def help(self, ctx):
    check = await predb.find_one({"guild": ctx.guild.id})
    prefix = check['prefix']
    view = DropdownView()
    emb = nextcord.Embed(title="Araki's commands", description="Hi! Welcome to the help page of Araki bot.\n```Please use the Select Menu to explore corresponding category```", colour=clr)
    emb.add_field(name="Suport ?", value=f"Click here to join our [support server]({support_link})", inline=True)
    emb.add_field(name="Information", value=f"My prefix for this server is {prefix}\nThis bot is under devlopement if you have any ideas or anything related to imporvement of our bot you can join our [Support server]({support_link})", inline=True)
    emb.set_footer(text="Made by Pranoy#0140")
    emb.set_thumbnail(url=ctx.author.avatar.url)
    await ctx.send(embed=emb, view=view)

def setup(client):
  client.add_cog(HelpPage(client))