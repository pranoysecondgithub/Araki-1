import nextcord
from nextcord.ext import commands
import main
from main import *

class PingS(commands.Cog):
  def __init__(self, client):
    self.client = client

  @nextcord.slash_command(name='ping', description='This shows the bot ping')
  async def PingS(self, interaction:nextcord.Interaction):
    _ping = round(pranoy.latency * 1000)
    pingEmbed = nextcord.Embed(title="Bot Ping", description= _ping, colour=0x303136)
    pingEmbed.set_footer(text='Made by Pranoy#0140')
    pingEmbed.set_thumbnail(url=interaction.user.avatar.url)
    await interaction.response.send_message(embed=pingEmbed)

def setup(client):
  client.add_cog(PingS(client))