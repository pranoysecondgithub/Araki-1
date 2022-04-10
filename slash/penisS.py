import nextcord
from nextcord.ext import commands
import random
import main
from main import *

class PenisS(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @nextcord.slash_command(name='penis', description='This show your penis size')
  @application_checks.is_nsfw()
  async def PenisS(
    self,
    interaction:nextcord.Interaction,
    user: nextcord.Member = nextcord.SlashOption(name='user', description='mention a user', required=False)
  ):
      if not user:
        user = interaction.user
      emb1 = nextcord.Embed(title='Nunnu measuring tape', description=f"{user.name}'s penis size is {random.randrange(11)}inch.", color=clr)
      await interaction.response.send_message(embed=emb1)

def setup(client):
  client.add_cog(PenisS(client))