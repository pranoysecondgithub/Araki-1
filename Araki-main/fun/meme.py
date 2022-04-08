import nextcord
from nextcord.ext import commands
from nextcord.ui import view
import requests
import random
import main
from main import *

class Meme(commands.Cog, nextcord.ui.View):
	def __init__ (self, pranoyMeme):
		self.pranoyMeme = pranoyMeme
		self.value = None
    
	@commands.command()
	async def Meme(self, ctx):
		r = requests.get("https://memes.blademaker.tv/api?lang=en")
		res = r.json()
		title = res['title']
		ups = res['ups']
		meme = res['image']
		sub = res['subreddit']
		embed = nextcord.Embed(title=f"{title}\nSubreddit: {sub}", url=res['image'], color=clr)
		embed.set_image(url=meme)
		embed.set_footer(text=f"👍 {ups}")
		await ctx.reply(embed=embed)
def setup(pranoyMeme):
	pranoyMeme.add_cog(Meme(pranoyMeme))