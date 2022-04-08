import nextcord
from nextcord.ext import commands

# A new nextcord view
class DelBtn(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="Delete", style=nextcord.ButtonStyle.secondary, emoji="<:dustbin:949602736633167882>")  
    async def stop(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.message.delete()

class Idk(commands.Cog):
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(Idk(client))