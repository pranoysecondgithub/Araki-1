from time import time
from nextcord.ext import commands
from inspect import getsource
import nextcord, main, config, emoji
import sys
import os, main
from main import *
from emoji import *
from config import *


class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['fl', 'force', 'fleave'], name='forceleave')
    @commands.is_owner()
    async def dev_force_leave(self, ctx, server: nextcord.Guild):
        guild = server
        await guild.leave()
        await ctx.send(f"Leaved {server}")


def setup(client):
    client.add_cog(Owner(client))