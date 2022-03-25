import nextcord, main, config, emoji
from nextcord.ext import commands
from config import *
from main import *
from emoji import *

class HelpConfigS(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @nextcord.slash_command(name='help-config', description='This shows the help page of config')
  async def ConfigS(
    self,
    interaction:nextcord.Interaction
    ):
    embed = nextcord.Embed(title='/Setprefix', description='It will change the server prefix.', colour=clr)
    embed.add_field(name=f"/set-welcome", value="It will set the welcome channel for you")
    embed.add_field(name=f"/remove-welcome", value="It will remove the welcome channel for you")
    embed.add_field(name=f"/set-leave", value="It will set the leave channel for you")
    embed.add_field(name=f"/remove-leave", value="It will remove the leave channel for you")    
    embed.set_footer(text=footer, icon_url=interaction.user.avatar.url)
    embed.set_author(name="Config help.", icon_url=interaction.user.avatar.url)
    await interaction.response.send_message(embed=embed, ephemeral=True)
      
def setup(client):
  client.add_cog(HelpConfigS(client))