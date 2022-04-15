import nextcord, main, config, emoji
from nextcord.ext import commands
from config import *
from main import *
from emoji import *

class WelcomeReset(nextcord.ui.View):
  def __init__(self):
    super().__init__()

  @nextcord.ui.button(label="Author", style=nextcord.ButtonStyle.blurple)  
  async def btn1(self, button: nextcord.ui.Button, intr: nextcord.Interaction):
    find = await wlcm_msg.find_one({"guild": intr.guild.id})
    if intr.user.guild_permissions.manage_guild:
      if find is None:
        await intr.response.send_message("Welcome module is not enabled. Use /enable-welcome to enable the module.", ephemeral=True)
      else:
        await wlcm_msg.update_one({"guild": intr.guild.id}, {"$set": {"author": None}})
        await intr.response.send_message(f"{success} | Welcome embed update successfully.")
    else:
      await intr.response.send_message("You dont have permission.", ephemeral=True)
  
  @nextcord.ui.button(label="Author Icon", style=nextcord.ButtonStyle.blurple)  
  async def btn2(self, button: nextcord.ui.Button, intr: nextcord.Interaction):
    find = await wlcm_msg.find_one({"guild": intr.guild.id})
    if intr.user.guild_permissions.manage_guild:
      if find is None:
        await intr.response.send_message("Welcome module is not enabled. Use /enable-welcome to enable the module.", ephemeral=True)
      else:
        await wlcm_msg.update_one({"guild": intr.guild.id}, {"$set": {"author_icon": None}})
        await intr.response.send_message(f"{success} | Welcome embed update successfully.")
    else:
      await intr.response.send_message("You dont have permission.", ephemeral=True)

  @nextcord.ui.button(label="Title", style=nextcord.ButtonStyle.blurple)  
  async def btn3(self, button: nextcord.ui.Button, intr: nextcord.Interaction):
    find = await wlcm_msg.find_one({"guild": intr.guild.id})
    if intr.user.guild_permissions.manage_guild:
      if find is None:
        await intr.response.send_message("Welcome module is not enabled. Use /enable-welcome to enable the module.", ephemeral=True)
      else:
        await wlcm_msg.update_one({"guild": intr.guild.id}, {"$set": {"title": None}})
        await intr.response.send_message(f"{success} | Welcome embed update successfully.")
    else:
      await intr.response.send_message("You dont have permission.", ephemeral=True)
  @nextcord.ui.button(label="Description", style=nextcord.ButtonStyle.blurple)  
  async def btn4(self, button: nextcord.ui.Button, intr: nextcord.Interaction):
    find = await wlcm_msg.find_one({"guild": intr.guild.id})
    if intr.user.guild_permissions.manage_guild:
      if find is None:
        await intr.response.send_message("Welcome module is not enabled. Use /enable-welcome to enable the module.", ephemeral=True)
      else:
        await wlcm_msg.update_one({"guild": intr.guild.id}, {"$set": {"description": None}})
        await intr.response.send_message(f"{success} | Welcome embed update successfully.")
    else:
      await intr.response.send_message("You dont have permission.", ephemeral=True)

  @nextcord.ui.button(label="Image", style=nextcord.ButtonStyle.blurple)  
  async def btn5(self, button: nextcord.ui.Button, intr: nextcord.Interaction):
    find = await wlcm_msg.find_one({"guild": intr.guild.id})
    if intr.user.guild_permissions.manage_guild:
      if find is None:
        await intr.response.send_message("Welcome module is not enabled. Use /enable-welcome to enable the module.", ephemeral=True)
      else:
        await wlcm_msg.update_one({"guild": intr.guild.id}, {"$set": {"image": None}})
        await intr.response.send_message(f"{success} | Welcome embed update successfully.")
    else:
      await intr.response.send_message("You dont have permission.", ephemeral=True)

  @nextcord.ui.button(label="Thumbnail", style=nextcord.ButtonStyle.blurple)  
  async def btn6(self, button: nextcord.ui.Button, intr: nextcord.Interaction):
    find = await wlcm_msg.find_one({"guild": intr.guild.id})
    if intr.user.guild_permissions.manage_guild:
      if find is None:
        await intr.response.send_message("Welcome module is not enabled. Use /enable-welcome to enable the module.", ephemeral=True)
      else:
        await wlcm_msg.update_one({"guild": intr.guild.id}, {"$set": {"thumbnail": None}})
        await intr.response.send_message(f"{success} | Welcome embed update successfully.")
    else:
      await intr.response.send_message("You dont have permission.", ephemeral=True)
  @nextcord.ui.button(label="Footer", style=nextcord.ButtonStyle.blurple)  
  async def btn7(self, button: nextcord.ui.Button, intr: nextcord.Interaction):
    find = await wlcm_msg.find_one({"guild": intr.guild.id})
    if intr.user.guild_permissions.manage_guild:
      if find is None:
        await intr.response.send_message("Welcome module is not enabled. Use /enable-welcome to enable the module.", ephemeral=True)
      else:
        await wlcm_msg.update_one({"guild": intr.guild.id}, {"$set": {"footer": None}})
        await intr.response.send_message(f"{success} | Welcome embed update successfully.")
    else:
      await intr.response.send_message("You dont have permission.", ephemeral=True)
  @nextcord.ui.button(label="Footer Icon", style=nextcord.ButtonStyle.blurple)  
  async def btn8(self, button: nextcord.ui.Button, intr: nextcord.Interaction):
    find = await wlcm_msg.find_one({"guild": intr.guild.id})
    if intr.user.guild_permissions.manage_guild:
      if find is None:
        await intr.response.send_message("Welcome module is not enabled. Use /enable-welcome to enable the module.", ephemeral=True)
      else:
        await wlcm_msg.update_one({"guild": intr.guild.id}, {"$set": {"footer_icon": None}})
        await intr.response.send_message(f"{success} | Welcome embed update successfully.")
    else:
      await intr.response.send_message("You dont have permission.", ephemeral=True)

class WelcomeDropdown(nextcord.ui.Select):
    def __init__(self):

        # Set the options that will be presented inside the dropdown
        options = [
            nextcord.SelectOption(label='Author'),
            nextcord.SelectOption(label='Author Icon'),
            nextcord.SelectOption(label='Title'),
            nextcord.SelectOption(label='Description'),
            nextcord.SelectOption(label='Image'),
            nextcord.SelectOption(label='Thumbnail'),
            nextcord.SelectOption(label='Footer'),
            nextcord.SelectOption(label='Footer Icon'),
            nextcord.SelectOption(label='Message')
        ]
        super().__init__(placeholder='Choose a option and edit...', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: nextcord.Interaction):
      find = await wlcm_msg.find_one({"guild": interaction.guild.id})
      if interaction.user.guild_permissions.manage_guild:
        if self.values[0] == 'Author':
          if find is None:
            await interaction.response.send_message("Welcome module is not enabled. Please use /welcome-enable to enable the module!", ephemeral=True)
          else:
            await interaction.response.send_message("Please send author message under 60 Seconds.")
            def is_correct(m):
              return m.author == interaction.user
            try:
              author_msg = await pranoy.wait_for('message', check=is_correct, timeout=60)
            except asyncio.TimeoutError:
              return await interaction.channel.send(f'Sorry, time over.')
            await wlcm_msg.update_one({"guild": interaction.guild.id}, {"$set": {"author": author_msg.content}})
            await interaction.channel.send(f"{success} | Welcome embed successfully updated.")
        if self.values[0] == 'Author Icon':
          if find is None:
            await interaction.response.send_message("Welcome module is not enabled. Please use /welcome-enable to enable the module!", ephemeral=True)
          else:
            await interaction.response.send_message("Please send author icon url under 60 Seconds.")
            def is_correct(m):
              return m.author == interaction.user
            try:
              author_icon = await pranoy.wait_for('message', check=is_correct, timeout=60)
            except asyncio.TimeoutError:
              return await interaction.channel.send(f'Sorry, time over.')
            await wlcm_msg.update_one({"guild": interaction.guild.id}, {"$set": {"author_icon": author_icon.content}})
            await interaction.channel.send(f"{success} | Welcome embed successfully updated.")
        if self.values[0] == 'Title':
          if find is None:
            await interaction.response.send_message("Welcome module is not enabled. Please use /welcome-enable to enable the module!", ephemeral=True)
          else:
            await interaction.response.send_message("Please send title message under 60 Seconds.")
            def is_correct(m):
              return m.author == interaction.user
            try:
              title = await pranoy.wait_for('message', check=is_correct, timeout=60)
            except asyncio.TimeoutError:
              return await interaction.channel.send(f'Sorry, time over.')
            await wlcm_msg.update_one({"guild": interaction.guild.id}, {"$set": {"title": title.content}})
            await interaction.channel.send(f"{success} | Welcome embed successfully updated.")

        if self.values[0] == 'Description':
          if find is None:
            await interaction.response.send_message("Welcome module is not enabled. Please use /welcome-enable to enable the module!", ephemeral=True)
          else:
            await interaction.response.send_message("Please send description message under 2 Minutes.")
            def is_correct(m):
              return m.author == interaction.user
            try:
              desc = await pranoy.wait_for('message', check=is_correct, timeout=120)
            except asyncio.TimeoutError:
              return await interaction.channel.send(f'Sorry, time over.')
            await wlcm_msg.update_one({"guild": interaction.guild.id}, {"$set": {"description": desc.content}})
            await interaction.channel.send(f"{success} | Welcome embed successfully updated.")

        if self.values[0] == 'Image':
          if find is None:
            await interaction.response.send_message("Welcome module is not enabled. Please use /welcome-enable to enable the module!", ephemeral=True)
          else:
            await interaction.response.send_message("Please send image url under 60 Seconds.")
            def is_correct(m):
              return m.author == interaction.user
            try:
              image = await pranoy.wait_for('message', check=is_correct, timeout=60)
            except asyncio.TimeoutError:
              return await interaction.channel.send(f'Sorry, time over.')
            await wlcm_msg.update_one({"guild": interaction.guild.id}, {"$set": {"image": image.content}})
            await interaction.channel.send(f"{success} | Welcome embed successfully updated.")

        if self.values[0] == 'Thumbnail':
          if find is None:
            await interaction.response.send_message("Welcome module is not enabled. Please use /welcome-enable to enable the module!", ephemeral=True)
          else:
            await interaction.response.send_message("Please send thumbnail url under 60 Seconds.")
            def is_correct(m):
              return m.author == interaction.user
            try:
              thumbnail = await pranoy.wait_for('message', check=is_correct, timeout=60)
            except asyncio.TimeoutError:
              return await interaction.channel.send(f'Sorry, time over.')
            await wlcm_msg.update_one({"guild": interaction.guild.id}, {"$set": {"thumbnail": thumbnail.content}})
            await interaction.channel.send(f"{success} | Welcome embed successfully updated.")

        if self.values[0] == 'Footer':
          if find is None:
            await interaction.response.send_message("Welcome module is not enabled. Please use /welcome-enable to enable the module!", ephemeral=True)
          else:
            await interaction.response.send_message("Please send footer message under 60 Seconds.")
            def is_correct(m):
              return m.author == interaction.user
            try:
              footer = await pranoy.wait_for('message', check=is_correct, timeout=60)
            except asyncio.TimeoutError:
              return await interaction.channel.send(f'Sorry, time over.')
            await wlcm_msg.update_one({"guild": interaction.guild.id}, {"$set": {"footer": footer.content}})
            await interaction.channel.send(f"{success} | Welcome embed successfully updated.")

        if self.values[0] == 'Footer Icon':
          if find is None:
            await interaction.response.send_message("Welcome module is not enabled. Please use /welcome-enable to enable the module!", ephemeral=True)
          else:
            await interaction.response.send_message("Please send footer icon url under 60 Seconds.")
            def is_correct(m):
              return m.author == interaction.user
            try:
              footer_icon = await pranoy.wait_for('message', check=is_correct, timeout=60)
            except asyncio.TimeoutError:
              return await interaction.channel.send(f'Sorry, time over.')
            await wlcm_msg.update_one({"guild": interaction.guild.id}, {"$set": {"footer_icon": footer_icon.content}})
            await interaction.channel.send(f"{success} | Welcome embed successfully updated.")

        if self.values[0] == 'Message':
          if find is None:
            await interaction.response.send_message("Welcome module is not enabled. Please use /welcome-enable to enable the module!", ephemeral=True)
          else:
            await interaction.response.send_message("Please send welcome message under 60 Seconds.")
            def is_correct(m):
              return m.author == interaction.user
            try:
              message = await pranoy.wait_for('message', check=is_correct, timeout=60)
            except asyncio.TimeoutError:
              return await interaction.channel.send(f'Sorry, time over.')
            await wlcm_msg.update_one({"guild": interaction.guild.id}, {"$set": {"message": message.content}})
            await interaction.channel.send(f"{success} | Welcome embed successfully updated.")
      else:
           await interaction.response.send_message("You dont have permissions", ephemeral=True)

class WelcomeView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(WelcomeDropdown())


class wlcm_setup(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(name='setup-welcome')
    @commands.has_permissions(manage_guild=True)
    async def setup_welcome(self, ctx):
      embed = nextcord.Embed(title='Welcome Setup', description='Well these are the few steps that you can setup welcome easyly.', colour=clr)
      embed.add_field(name='Variables', value="``[user]``` Mentions the new member.\n```[userName]``` New member name without mentioning\n```[memberCount]``` Amount of members reached\n```[server]``` Server name\n```[userAvatar]``` Get url of user avatar")
      embed.set_footer(text=footer)
      await ctx.send(embed=embed, view=WelcomeView())

    @nextcord.slash_command(name='setup-welcome', description='Setup welcome message')
    @application_checks.has_permissions(manage_guild=True)
    async def setup_welcomeS(self, ctx:nextcord.Interaction):
      embed = nextcord.Embed(title='Welcome Setup', description='Well these are the few steps that you can setup welcome easyly.', colour=clr)
      embed.add_field(name='Variables', value="```[user]``` Mentions the new member.\n```[userName]``` New member name without mentioning\n```[memberCount]``` Amount of members reached\n```[server]``` Server name\n```[userAvatar]``` Get url of user avatar")
      embed.set_footer(text=footer)
      await ctx.response.send_message(embed=embed, view=WelcomeView())

    @commands.command(name='reset-welcome')
    @commands.has_permissions(manage_guild=True)
    async def reset_welcomeS(self, ctx):
      await ctx.send("Which components you want to reset ?", view=WelcomeReset())

    @nextcord.slash_command(name='reset-welcome', description='Reset welcome message')
    @application_checks.has_permissions(manage_guild=True)
    async def reset_welcome(self, ctx:nextcord.Interaction):
      await ctx.response.send_message("Which components you want to reset ?", view=WelcomeReset())

    @commands.command(name='test-welcome')
    async def _test_welcome(self, ctx):
      find = await welcome.find_one({"guild": ctx.guild.id})
      find_msg = await wlcm_msg.find_one({"guild": ctx.guild.id})
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
            author = author.replace('[userName]', ctx.author.name)
        if author != '' and author != None:
          if '[server]' in author:
            author = author.replace('[server]', ctx.guild.name)
        if author != '' and author != None:
          if '[memberCount]' in author:
            author = author.replace('[memberCount]', len(ctx.guild.members))

        #title
        if title != '' and title != None:
          if '[userName]' in title:
            title = title.replace('[userName]', ctx.author.name)
        if title != '' and title != None:
          if '[user]' in title:
            title = title.replace('[user]', ctx.author.mention)
        if title != '' and title != None:
          if '[memberCount]' in title:
            title = title.replace('[memberCount]', len(ctx.guild.members))
        if title != '' and title != None:
          if '[server]' in title:
            title = title.replace('[server]', ctx.guild.name)
        #desc 
        if desc != '' and desc != None:
          if '[userName]' in desc:
            desc = desc.replace('[userName]', ctx.author.name)
        if desc != '' and desc != None:
          if '[user]' in desc:
            desc = desc.replace('[user]', ctx.author.mention)
        if desc != '' and title != None:
          if '[memberCount]' in desc:
            desc = desc.replace('[memberCount]', len(ctx.guild.members))
        if desc != '' and desc != None:
          if '[server]' in desc:
            desc = desc.replace('[server]', ctx.guild.name)

        #message
        if msg != '' and msg != None:
          if '[user]' in msg:
            msg = msg.replace('[user]', ctx.author.mention)
        if msg != '' and msg != None:
          if '[userName]' in msg:
            msg = msg.replace('[userName]', ctx.author.name)
        if msg != '' and msg != None:
          if '[server]' in msg:
            msg = msg.replace('[server]', ctx.guild.name)

        # images
        if author_icon != '' and author_icon != None:
          if '[avatar]' in avatar_icon:
            avatar_icon = avatar_icon.replace('[avatar]', ctx.author.avatar.url)
        if thumbnail != '' and thumbnail != None:
          if '[avatar]' in thumbnail:
            thumbnail = thumbnail.replace('[avatar]', ctx.author.avatar.url)
        if footer_icon != '' and footer_icon != None:
          if '[avatar]' in footer_icon:
            footer_icon = footer_icon.replace('[avatar]', ctx.author.avatar.url)
        if image != '' and image != None:
          if '[avatar]' in image:
            image = image.replace('[avatar]', ctx.author.avatar.url)

        #footer
        if footer != '' and footer != None:
          if '[user]' in footer:
            footer = footer.replace('[user]', ctx.author.mention)
        if footer != '' and footer != None:
          if '[userName]' in footer:
            footer = footer.replace('[userName]', ctx.author.name)
        if footer != '' and footer != None:
          if '[server]' in footer:
            footer = footer.replace('[server]', ctx.guild.name)



        if author != None:
          embed.set_author(name=author)
        if author_icon != None:
          embed.set_author(icon_url=f"{author_icon}")
        if title != None:
          embed.title=title
        if desc != None:
          embed.description=desc
        if image != None:
          embed.set_image(url=f"{image}")
        if thumbnail != None:
          embed.set_thumbnail(url=f"{thumbnail}")
        if footer != None:
          embed.set_footer(text=footer)
        if footer_icon != None:
          embed.set_footer(icon_url=f"{footer_icon}")
        if msg != None :
          await pranoy.get_channel(channel).send(msg, embed=embed)
        else:
          await pranoy.get_channel(channel).send(embed=embed)


def setup(client):
    client.add_cog(wlcm_setup(client))