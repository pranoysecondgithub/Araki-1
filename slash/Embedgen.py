import nextcord, main, config, emoji
from nextcord import Embed
from nextcord.ext import commands
from main import *
from emoji import *
from config import *

class EmbedGen(commands.Cog):
    def __init__(self, client):
        self.client = client


    @nextcord.slash_command(name="embed-create", description="Create a embed")
    async def embedS(
            self,
            intr:nextcord.Interaction,
            embChannel: nextcord.abc.GuildChannel = nextcord.SlashOption(channel_types=[ChannelType.text], name="channel", description="Please provide a channel where you want to send this embed"),
            embTitle: str = nextcord.SlashOption(name="embed-title", description="What you wanna write in embed title ?"),
            embDescription: str = nextcord.SlashOption(name="embed-description", description="Please provide a embed description"),
            embAuthor: str = nextcord.SlashOption(name="embed-author", description="What you wanna write in embed author ?", required=False),
            embFooter: str = nextcord.SlashOption(name="embed-footer", description="Please provide a embed footer", required=False),
            embImage: str = nextcord.SlashOption(name="embed-image", description="Please provide a embed image", required=False),
            embThumbnail: str = nextcord.SlashOption(name="embed-thumbnail", description="Please provide a embed thumbnail", required=False),
            
        ):
        ConfirmEmbed = Embed(colour=clr)
        if embAuthor:
            ConfirmEmbed.set_author(name=embAuthor)
        if embTitle:
            ConfirmEmbed.title=embTitle
        if embDescription:
            ConfirmEmbed.description=embDescription
        if embFooter:
            ConfirmEmbed.set_footer(text=embFooter)
        if embImage:
            ConfirmEmbed.set_image(url=embImage)
        if embThumbnail:
            ConfirmEmbed.set_thumbnail(url=embThumbnail)
        if not embAuthor and embDescription and embFooter and embImage and embThumbnail and embTitle:
            await intr.response.send_message("Please write any of these values!")
        else:
            await embChannel.send(embed=ConfirmEmbed)
            await intr.response.send_message(f"{success} | Embed send successfully.")        
        

def setup(client):
    client.add_cog(EmbedGen(client))