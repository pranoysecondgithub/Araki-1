import nextcord, main
from nextcord.ext import commands
from main import *
import asyncio

class ClearS(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @nextcord.slash_command(name='clear', description='Delete some messages')
  @application_checks.has_permissions(manage_messages=True)
  async def ClearS(
    self,
    interaction:nextcord.Interaction,
    amount: int = nextcord.SlashOption(name='amount', description='How many messages you want to delete ?')
    ):
        try:
            await interaction.response.send_message("Deleting messages...")
            await interaction.channel.purge(limit = amount + 1)
        except:
          pass


def setup(client):
  client.add_cog(ClearS(client))