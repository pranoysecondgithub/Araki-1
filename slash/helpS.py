from nextcord.ext import commands
import nextcord
import os
import config
from config import *
from nextcord import ButtonStyle
from nextcord.ui import Button, View
import main
from main import *

class DropdownS(nextcord.ui.Select):
    def __init__(self):
      SelectOptions = [
        nextcord.SelectOption(label='Moderation', description='Show moderation commands', emoji='<:Admin:947068190901551116>'),
        nextcord.SelectOption(label='Economy', description='Show Economy commands', emoji='<:economy:948649700783960105>'),
        nextcord.SelectOption(label='Fun', description='Show the fun commands', emoji='<:fun:948144502940516412>'),
        nextcord.SelectOption(label='Config', description='Show the config commands', emoji='<:settings:947068267888013353>'),
        nextcord.SelectOption(label='Utility', description='Show the Utility commands', emoji='<:modd:947068138762166272>'),
        nextcord.SelectOption(label='Emotes', description='Show the Emotes commands', emoji='<:EmoteOk:951780893201170442>'),
      ]
      
      super().__init__(placeholder='Choose a command type...', min_values=1, max_values=1, options=SelectOptions)
    async def callback(self, interaction: nextcord.Interaction):
      Moderation = nextcord.Embed(title='Moderation commands', description='```Clear, Avatar, Mute, Unmute, Kick, Ban, Unban, Warn, Slowmode, Lock, Unlock```', colour=clr)
      Moderation.set_footer(text='Made by Pranoy#0140')

      Economy = nextcord.Embed(title='Economy commands', description='```Earn, Create, Arency, Work, Give, Coinflip, Slots, Shop, Buy, Inventory, Sell```', colour=clr)
      Economy.set_footer(text='Made by Pranoy#0140')

      Fun = nextcord.Embed(title='Fun commands', description='```Meme, Cool, Gay, Penis, Poll, HeadOrTail```', colour=clr)
      Fun.set_footer(text='Made by Pranoy#0140')

      Config = nextcord.Embed(title='Config commands', description='```Config-help, Setprefix, Set-welcome, Remove-welcome, Set-leave, Remove-leave```', colour=clr)
      Config.set_footer(text='Made by Pranoy#0140')

      Utility = nextcord.Embed(title='Utility commands', description='```Poll, Serverinfo, Userinfo, Membercount, Invite, Vote, Stats```', colour=clr)
      Utility.set_footer(text='Made by Pranoy#0140')

      Emote = nextcord.Embed(title='Emotes commands', description='```Cry, Smile, Dance, Blush, Sleepy, Thinking, Triggered```', colour=clr)
      Emote.set_footer(text='Made by Pranoy#0140')
      
      Music = nextcord.Embed(title='Config commands', description='```Play, Pause, Resume, Loop, Queue, Clearqueue, Suffle, Stop, Join, Leave,    Setvolume, Nowplaying,, Lyrics, Skip```', colour=clr)
      Music.set_footer(text='Made by Pranoy#0140')
      if self.values[0] == 'Moderation':
        await interaction.response.edit_message(embed=Moderation)
      if self.values[0] == 'Economy':
        await interaction.response.edit_message(embed=Economy)
      if self.values[0] == 'Fun':
        await interaction.response.edit_message(embed=Fun)
      if self.values[0] == 'Config':
        await interaction.response.edit_message(embed=Config)
      if self.values[0] == 'Utility':
        await interaction.response.edit_message(embed=Utility)
      if self.values[0] == 'Emotes':
        await interaction.response.edit_message(embed=Emote)
      if self.values[0] == 'Music':
        await interaction.response.edit_message(embed=Music)
        
class DropdownViewS(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(DropdownS())

class HelpPageS(commands.Cog):
  def __init__(self, client):
    self.client = client

  @nextcord.slash_command(name='help', description='show commands list!')
  async def helpS(self, interaction:nextcord.Interaction):
    check = await predb.find_one({"guild": interaction.guild.id})
    prefix = check['prefix']
    view = DropdownViewS()
    emb = nextcord.Embed(title="Araki's commands", description="Hi! Welcome to the help page of Araki bot.\n```Please use the Select Menu to explore corresponding category```", colour=clr)
    emb.add_field(name="Suport ?", value=f"Click here to join our [support server]({support_link})", inline=True)
    emb.add_field(name="Information", value=f"My prefix for this server is {prefix}\nIf you have any suggestions that you think will help improve Araki in any way, we urge you to join our official server and share them with us.", inline=True)
    emb.set_footer(text="Made by Pranoy#0140")
    emb.set_thumbnail(url=interaction.user.avatar.url)
    await interaction.response.send_message(embed=emb, view=view)

def setup(client):
  client.add_cog(HelpPageS(client))