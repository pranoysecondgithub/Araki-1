import nextcord
from nextcord.ext import commands
import main
from main import *

class UserInfoS(commands.Cog):
  def __init__(self, client):
    self.client = client

  @nextcord.slash_command(name='user-info', description='This show the targeted user info')
  async def UserinfoS(
    self,
    interaction: nextcord.Interaction,
    member: nextcord.Member = nextcord.SlashOption(name='user', description='mention a user', required=False)
  ):
    date_format = "%a, %d %b %Y %I:%M %p"
    if not member:
      member = interaction.user
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in member.guild_permissions if p[1]])
    embed = nextcord.Embed(title=f"{member}'s info", color=clr)
    embed.add_field(name="Name", value=f"{member.name}", inline=True)
    embed.add_field(name="ID", value=f"{member.id}", inline=True)
    embed.add_field(name="User Joined", value=member.joined_at.strftime(date_format), inline=True)
    embed.add_field(name="Account Age", value=member.created_at.strftime(date_format), inline=True)
    if len(member.roles) > 1:
        role_string = ' '.join([r.mention for r in member.roles][1:])
        embed.add_field(name="Member Roles", value=role_string, inline=True)
    embed.add_field(name="Guild Permission", value=perm_string, inline=True)
    embed.set_footer(text='Made by Pranoy#0410')
    await interaction.response.send_message(embed=embed)
def setup(client):
  client.add_cog(UserInfoS(client))