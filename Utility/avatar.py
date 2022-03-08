from nextcord.ext import commands
import nextcord
from nextcord.ui import Button, View
import os

class Avatar(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['av'])
    async def Avatar(self, ctx, member: nextcord.Member = None):
      if member == None:
        member = ctx.author
      memberAvatar = member.display_avatar


      avaEmbed = nextcord.Embed(title=f"{member.name}'Avatar",  colour=0x303136)
      avaEmbed.set_image(url = memberAvatar)
      avaEmbed.set_footer(text="Made by Pranoy#0140")
      
     
      
      await ctx.send(embed=avaEmbed)
      
def setup(client):
  client.add_cog(Avatar(client))
