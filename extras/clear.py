import nextcord
from nextcord.ext import commands
import asyncio

class Clear(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @commands.command(aliases = ['c'])
  @commands.has_permissions(manage_messages = True)
  async def clear(self, ctx, amount = 1):
        try:
            await ctx.channel.purge(limit = amount + 1)
        except:
            await ctx.reply('Something went wrong')


def setup(client):
  client.add_cog(Clear(client))