import nextcord, datetime
from nextcord.ext import commands
from config import *
from main import *
from emoji import *
import datetime

class Welcome(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.command(name='welcome-enable')
  @commands.has_permissions(manage_guild=True)
  async def welcome_enable(self, ctx):
    find = await wlcm_msg.find_one({"guild": ctx.guild.id})
    if find is None:
      insert = {
        "guild": ctx.guild.id,
        "author": None,
        "author_icon": None,
        "title": None,
        "description": None,
        "image": None,
        "thumbnail": None,
        "footer": None,
        "footer_icon": None,
        "message": None,
        "colour": None
      }
      await wlcm_msg.insert_one(insert)
      await ctx.send(f"{success} | Welcome enabled.")
    else:
      await ctx.reply("Welcome is already enabled")
  @nextcord.slash_command(name='enable-welcome', description='Enable the welcome module')
  @application_checks.has_permissions(manage_guild=True)
  async def welcome_enableS(self, ctx:nextcord.Interaction):
    find = await wlcm_msg.find_one({"guild": ctx.guild.id})
    if find is None:
      insert = {
        "guild": ctx.guild.id,
        "author": None,
        "author_icon": None,
        "title": None,
        "description": None,
        "image": None,
        "thumbnail": None,
        "footer": None,
        "footer_icon": None,
        "message": None,
        "colour": None
      }
      await wlcm_msg.insert_one(insert)
      await ctx.response.send_message(f"{success} | Welcome enabled.")
    else:
      await ctx.response.send_message("Welcome is already enabled", ephemeral=True)


  @commands.command(aliases=['Set-welcome'])
  @commands.has_permissions(manage_guild=True)
  async def set_welcome(self, ctx, channel:nextcord.TextChannel = None):
    if channel == None:
      channel = ctx.channel
    find = await welcome.find_one({"guild": ctx.guild.id})
    if find is None:
      insert = {"guild": ctx.guild.id, "channel": channel.id}
      await welcome.insert_one(insert)
      await ctx.send(f"{success} | Welcome channel set to {channel}")
    elif channel == find['channel']:
      await ctx.reply(f"{error} | This channel is already registered for welcome")
    else:
      await welcome.update_one({"guild": ctx.guild.id}, {"$set": {"channel": channel.id}})
      await ctx.send(f"{success} | Welcome channel changed to {channel}")

  @nextcord.slash_command(name='set-welcome-channel', description='Set the welcome channel')
  @application_checks.has_permissions(manage_guild=True)
  async def set_welcomeS(
    self,
    ctx:nextcord.Interaction,
    channel: nextcord.abc.GuildChannel = nextcord.SlashOption(channel_types=[ChannelType.text], name='channel', description='Please mention a channel.', required=False)
  ):
    if not channel:
      channel = ctx.channel
    find = await welcome.find_one({"guild": ctx.guild.id})
    if find is None:
      insert = {"guild": ctx.guild.id, "channel": channel.id}
      await welcome.insert_one(insert)
      await ctx.response.send_message(f"{success} | Welcome channel set to {channel}")
    elif channel == find['channel']:
      await ctx.response.send_message(f"{error} | This channel is already registered for welcome")
    else:
      await welcome.update_one({"guild": ctx.guild.id}, {"$set": {"channel": channel.id}})
      await ctx.response.send_message(f"{success} | Welcome channel changed to {channel}")
  @commands.command(aliases=['Remove-welcome'])
  @commands.has_permissions(manage_guild=True)
  async def remove_welcome(self, ctx, channel:nextcord.TextChannel = None):
    if channel == None:
      channel = ctx.channel
    find = await welcome.find_one({"guild": ctx.guild.id, "channel": ctx.channel.id})
    find = await wlcm_msg.find_one({"guild": ctx.guild.id})
    if find is None:
      await ctx.reply(f"{error} | This is not a welcome channel!")
    else:
      await welcome.delete_one({"guild": ctx.guild.id, "channel": ctx.channel.id})
      try:
        await wlcm_msg.update_one({"guild": ctx.guild.id}, {"$set": {"author": None, "author_icon": None, "title": None, "description": None, "image": None, "thumbnail": None, "footer": None, "footer_icon":None, "message": None}})
      except:
        pass
      await ctx.send(f"{success} | Welcome channel removed!")
  @nextcord.slash_command(name='remove-welcome-channel', description='Remove the welcome channel')
  @commands.has_permissions(manage_guild=True)
  async def remove_welcomeS(
    self,
    ctx:nextcord.Interaction,
    channel: nextcord.abc.GuildChannel = nextcord.SlashOption(channel_types=[ChannelType.text], name='channel', description='Please mention a channel.', required=False)
  ):
    if not channel:
      channel = ctx.channel
    find = await welcome.find_one({"guild": ctx.guild.id, "channel": ctx.channel.id})
    if find is None:
      await ctx.response.send_message(f"{error} | This is not a welcome channel!", ephemeral=True)
    else:
      await welcome.delete_one({"guild": ctx.guild.id, "channel": ctx.channel.id})
      try:
        await wlcm_msg.update_one({"guild": ctx.guild.id}, {"$set": {"author": None, "author_icon": None, "title": None, "description": None, "image": None, "thumbnail": None, "footer": None, "footer_icon":None, "message": None}})
      except:
        pass
      await ctx.response.send_message(f"{success} | Welcome channel removed!")
      
  @commands.Cog.listener()
  async def on_member_join(self,member):
    find = await welcome.find_one({"guild": member.guild.id})
    find_msg = await wlcm_msg.find_one({"guild": member.guild.id})
    author = find_msg['author']
    author_icon = find_msg['author_icon']
    title = find_msg['title']
    desc = find_msg['description']
    image = find_msg['image']
    thumbnail = find_msg['thumbnail']
    footer = find_msg['footer']
    footer_icon = find_msg['footer_icon']
    msg = find_msg['message']
    if find and find_msg is None:
      return
    elif author == None and author_icon == None and title == None and desc == None and image == None and thumbnail == None and footer == None and footer_icon == None and msg == None:
      return
    else:
      author = find_msg['author']
      author_icon = find_msg['author_icon']
      title = find_msg['title']
      desc = find_msg['description']
      image = find_msg['image']
      thumbnail = find_msg['thumbnail']
      footer = find_msg['footer']
      footer_icon = find_msg['footer_icon']
      msg = find_msg['message']
      channel = find['channel']

      embed = nextcord.Embed(colour=clr)
      if author != '' and author != None:
        if '[userName]' in author:
          author = author.replace('[userName]', member.name)
      if author != '' and author != None:
        if '[server]' in author:
          author = author.replace('[server]', member.guild.name)
      if author != '' and author != None:
        if '[memberCount]' in author:
          author = author.replace('[memberCount]', len(member.guild.members))

      #title
      if title != '' and title != None:
        if '[userName]' in title:
          title = title.replace('[userName]', member.name)
      if title != '' and title != None:
        if '[user]' in title:
          title = title.replace('[user]', member.mention)
      if title != '' and title != None:
        if '[memberCount]' in title:
          title = title.replace('[memberCount]', len(member.guild.members))
      if title != '' and title != None:
        if '[server]' in title:
          title = title.replace('[server]', member.guild.name)
      #desc 
      if desc != '' and desc != None:
        if '[userName]' in desc:
          desc = desc.replace('[userName]', member.name)
      if desc != '' and desc != None:
        if '[user]' in desc:
          desc = desc.replace('[user]', member.mention)
      if desc != '' and title != None:
        if '[memberCount]' in desc:
          desc = desc.replace('[memberCount]', len(member.guild.members))
      if desc != '' and desc != None:
        if '[server]' in desc:
          desc = desc.replace('[server]', member.guild.name)

      #message
      if msg != '' and msg != None:
        if '[user]' in msg:
          msg = msg.replace('[user]', member.mention)
      if msg != '' and msg != None:
        if '[userName]' in msg:
          msg = msg.replace('[userName]', member.name)
      if msg != '' and msg != None:
        if '[server]' in msg:
          msg = msg.replace('[server]', member.guild.name)

      # images
      if author_icon != '' and author_icon != None:
        if '[avatar]' in avatar_icon:
          avatar_icon = avatar_icon.replace('[avatar]', member.avatar.url)
      if thumbnail != '' and thumbnail != None:
        if '[avatar]' in thumbnail:
          thumbnail = thumbnail.replace('[avatar]', member.avatar.url)
      if footer_icon != '' and footer_icon != None:
        if '[avatar]' in footer_icon:
          footer_icon = footer_icon.replace('[avatar]', member.avatar.url)
      if image != '' and image != None:
        if '[avatar]' in image:
          image = image.replace('[avatar]', member.avatar.url)

      #footer
      if footer != '' and footer != None:
        if '[user]' in footer:
          footer = footer.replace('[user]', member.mention)
      if footer != '' and footer != None:
        if '[userName]' in footer:
          footer = footer.replace('[userName]', member.name)
      if footer != '' and footer != None:
        if '[server]' in footer:
          footer = footer.replace('[server]', member.guild.name)
      
        

      if author != None:
        embed.set_author(name=author)
      if author_icon != None:
        embed.set_author(icon_url=author_icon)
      if title != None:
        embed.title=title
      if desc != None:
        embed.description=desc
      if image != None:
        embed.set_image(url=image)
      if thumbnail != None:
        embed.set_thumbnail(url=thumbnail)
      if footer != None:
        embed.set_footer(text=footer)
      if footer_icon != None:
        embed.set_footer(icon_url=footer_icon)
      if msg != None :
        await pranoy.get_channel(channel).send(msg, embed=embed)
      else:
        await pranoy.get_channel(channel).send(embed=embed)
def setup(client):
  client.add_cog(Welcome(client))