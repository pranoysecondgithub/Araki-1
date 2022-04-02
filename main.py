from nextcord import Interaction, SlashOption, ChannelType, ButtonStyle
from nextcord.abc import GuildChannel
from nextcord.ext import commands
from nextcord.ui import Button, View
import nextcord, asyncio
import os
import config
import datetime as dt
import time
from datetime import datetime
from config import *
from motor.motor_asyncio import AsyncIOMotorClient
from time import strftime
from nextcord.ext import application_checks

intents = nextcord.Intents.all()
intents.members = True

db = cluster["main"]
predb = db["prefix"]


async def get_prefix(client, message):
    stats = await predb.find_one({"guild": message.guild.id})

    if stats is None:
        updated = {"guild": message.guild.id, "prefix": "a."}
        await predb.insert_one(updated)
        extras = "a."
        return commands.when_mentioned_or(extras)(client, message)
    else:
        extras = stats["prefix"]
        return commands.when_mentioned_or(extras)(client, message)


pranoy = commands.Bot(command_prefix=get_prefix,
                      help_command=None,
                      case_insensitive=True,
                      intents=intents,
                      owner_ids=['852786941842030594'])

clr = 0x303136


@pranoy.event
async def on_ready():
    pranoy.launch_time = dt.datetime.utcnow()
    await pranoy.change_presence(activity=nextcord.Activity(
        type=nextcord.ActivityType.listening,
        name=f"a.help | Total Servers {len(pranoy.guilds)}"))
    print(f'Logged in as {pranoy.user} (ID: {pranoy.user.id})')


for fn in os.listdir('./Utility'):
    if fn.endswith('.py'):
        pranoy.load_extension(f'Utility.{fn[:-3]}')

for fn in os.listdir('./fun'):
    if fn.endswith('.py'):
        pranoy.load_extension(f'fun.{fn[:-3]}')

for fn in os.listdir('./slash'):
    if fn.endswith('.py'):
        pranoy.load_extension(f'slash.{fn[:-3]}')

for fn in os.listdir('./extras'):
    if fn.endswith('.py'):
        pranoy.load_extension(f'extras.{fn[:-3]}')

for fn in os.listdir('./economy'):
    if fn.endswith('.py'):
        pranoy.load_extension(f'economy.{fn[:-3]}')

for fn in os.listdir('./emotes'):
    if fn.endswith('.py'):
        pranoy.load_extension(f"emotes.{fn[:-3]}")


@pranoy.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        em = nextcord.Embed(title=f"Error",
                            description=f"Command not found.",
                            colour=clr)
        em.set_footer(text='Made by Pranoy#0140')
        await ctx.send(embed=em)


@pranoy.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'Still on cooldown, please try again in {:.2f}s.'.format(
            error.retry_after)
        em13 = nextcord.Embed(title="**Error Block**", color=clr)
        em13.add_field(name="__Slowmode Error:__", value=msg)
        await ctx.send(embed=em13)
    if isinstance(error, commands.MissingRequiredArgument):
        msg2 = "Please enter all the required arguments!"
        em14 = nextcord.Embed(title="Error Block", color=clr)
        em14.add_field(name="__Missing Required Arguments:__", value=msg2)
        await ctx.send(embed=em14)  #sending the embed
    if isinstance(error, commands.MissingPermissions):
        msg3 = "You are missing permissions to use that command!"
        em15 = nextcord.Embed(title="**Error Block**", color=clr)
        em15.add_field(name="__Missing Permissions:__", value=msg3)
        await ctx.send(embed=em15)
    if isinstance(error, commands.BotMissingPermissions):
        embed200 = nextcord.Embed(
            title="__Missing Permissions__",
            description="I dont have proper permissions to perform this action",
            colour=clr)
        try:
            await ctx.author.send(embed=embed200)
        except:
            await ctx.send(embed=embed200)


@pranoy.event
async def on_guild_join(guild):
    pre = await predb.find_one({"guild": guild.id})
    prefix = pre['prefix']
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embedHi = nextcord.Embed(
                title="Thanks for adding me!",
                description=f"Use /help or {prefix}help to get a commands list",
                url=support_link,
                colour=clr)
            embedHi.set_footer(text=f"© {footer}")
            embedHi.add_field(
                name='Information',
                value=
                f"My prefix for this server is {prefix}\nIf you have any suggestions that you think will help improve Araki in any way, we urge you to join our official server and share them with us."
            )
            support_vtn = Button(label='Support Server', url=support_link)
            view = View()
            view.add_item(support_vtn)
            await channel.send(embed=embedHi, view=view)
        break


pranoy.run(TOKEN)
