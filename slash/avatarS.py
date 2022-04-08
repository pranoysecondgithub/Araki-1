from nextcord.ext import commands
import nextcord, main
from nextcord.ui import Button, View
import os
from main import *

class AvatarS(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="avatar", description="Fetch the avatar of a user")
    async def AvatarS(
      self,
      interaction:nextcord.Interaction,
      member: nextcord.Member = nextcord.SlashOption(name="user", description='fetch the avarar of a user')
    ):
     amb = nextcord.Embed(title=f"{member.name}'s avatar",colour=clr)
     amb.set_image(url=member.avatar.url)
     amb.set_footer(text=footer)
     await interaction.response.send_message(embed=amb, ephemeral=True)
      
def setup(client):
  client.add_cog(AvatarS(client))
