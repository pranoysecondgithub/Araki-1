import nextcord
from nextcord.ext import commands
from nextcord.ui import view
import requests
import random
import main
from main import *

class MemeS(commands.Cog, nextcord.ui.View):
	def __init__ (self, pranoyMeme):
		self.pranoyMeme = pranoyMeme
		self.value = None
    
	@nextcord.slash_command(name='meme', description='This shows a random meme from reddit')
	async def MemeS(
		self,
		interaction:nextcord.Interaction,

	):
		r = requests.get("https://memes.blademaker.tv/api?lang=en")
		res = r.json()
		title = res['title']
		ups = res['ups']
		meme = res['image']
		sub = res['subreddit']
		embed = nextcord.Embed(title=f"{title}\nSubreddit: {sub}", url=res['image'], color=clr)
		embed.set_image(url=meme)
		embed.set_footer(text=f"👍 {ups}")
		await interaction.response.send_message(embed=embed)
def setup(pranoyMeme):
	pranoyMeme.add_cog(MemeS(pranoyMeme))