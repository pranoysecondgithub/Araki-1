import nextcord, main
from nextcord.ext import commands
from nextcord import ButtonStyle
from nextcord.ui import Button, View
import config
from config import *
from main import *

class InviteS(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @nextcord.slash_command(name='invite', description='invite me please')
  async def InviteS(self, interaction:nextcord.Interaction):
    support = Button(label='Suport server', url=support_link)
    invite = Button(label='Invite Me', url=invite_link)
    embed = nextcord.Embed(title='Links', color=0x303136)
    embed.add_field(name='My Invite Link', value=f'[Invite Me]({invite_link})', inline=True)
    embed.add_field(name='My Support Server Link', value=f'[Support Server]({support_link})', inline=True)
    embed.set_footer(text='Made by Pranoy#0140')
    embed.set_thumbnail(url=interaction.user.avatar.url)
    myView = View()
    myView.add_item(support)
    myView.add_item(invite)
    await interaction.response.send_message(embed=embed, view=myView)

def setup(client):
  client.add_cog(InviteS(client))