import nextcord
from nextcord.ext import commands
import main
from main import *

class ServerS(commands.Cog):
  def __init__(self, client):
    self.client = client

  @nextcord.slash_command(name='server-info', description='This shows the server info')
  async def ServerinfoS(self, interaction:nextcord.Interaction):
    guild = interaction.guild
    roles_count = len(interaction.guild.roles)
    list_of_bots = [bot.mention for bot in interaction.guild.members if bot.bot]
    embed = nextcord.Embed(title=f"{guild}'s info", colour=clr)
    embed.add_field(name='Guild Name', value=f"{interaction.guild.name}", inline=True)
    embed.add_field(name='Owner', value=f"{interaction.guild.owner.mention}", inline=True)
    embed.add_field(name='Guild Id', value=f"{interaction.guild.id}", inline=True)
    embed.add_field(name='Owner Id', value=f"{interaction.guild.owner.id}", inline=True)
    embed.add_field(name='Verification Level', value=f"{interaction.guild.verification_level}", inline=True)
    embed.add_field(name='Total Members', value=f"{interaction.guild.member_count}", inline=True)
    embed.add_field(name='Number Of Roles', value=f"{roles_count}", inline=True)
    embed.add_field(name='Bots', value=f"{list_of_bots}", inline=True)
    embed.add_field(name='Highest Role', value=f"{interaction.guild.roles[-2]}", inline=True)
    embed.add_field(name='Guild created at', value=f"{interaction.guild.created_at}", inline=True)
    await interaction.response.send_message(embed=embed)

def setup(client):
  client.add_cog(ServerS(client))