import nextcord
from nextcord.ext import commands
import random
import main
from main import *

class CoolS(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @nextcord.slash_command(name='cool', description='your cool rate')
  async def CoolS(
    self, 
    interaction:nextcord.Interaction,
    user:nextcord.Member = nextcord.SlashOption(name='user', description='mention a user', required=False)
  ):
    if not user:
      user = interaction.user
      
    emb1 = nextcord.Embed(title='Cool rate', description=f"{user.name} is {random.randrange(101)}% cool.", color=clr)
    await interaction.response.send_message(embed=emb1)

def setup(client):
  client.add_cog(CoolS(client))