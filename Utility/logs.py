import nextcord, config, emoji, main
from main import *
from emoji import *
from config import *


class Logs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        embed = nextcord.Embed(title='Guild name',
                               description=f"{guild.name}",
                               colour=clr)
        embed.set_author(name="Bot joins a new server!")
        embed.add_field(name="Guild id", value=f"{guild.id}", inline=True)
        embed.add_field(name="Guild owner",
                        value=f"{guild.owner}",
                        inline=True)
        embed.add_field(name="Guild members",
                        value=f"{guild.owner.id}",
                        inline=True)
        embed.add_field(name="Total guilds",
                        value=f"{len(pranoy.guilds)}",
                        inline=True)
        msg = pranoy.get_channel(945290809996083220)
        await msg.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        embed = nextcord.Embed(title='Guild name',
                               description=f"{guild.name}",
                               colour=clr)
        embed.set_author(name=f"Bot remove from {guild.name} server!")
        embed.add_field(name="Guild id", value=f"{guild.id}", inline=True)
        embed.add_field(name="Guild owner",
                        value=f"{guild.owner}",
                        inline=True)
        embed.add_field(name="Guild members",
                        value=f"{guild.owner.id}",
                        inline=True)
        embed.add_field(name="Total guilds",
                        value=f"{len(pranoy.guilds)}",
                        inline=True)
        msg = pranoy.get_channel(945290810977583194)
        await msg.send(embed=embed)


def setup(client):
    client.add_cog(Logs(client))
