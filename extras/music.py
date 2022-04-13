import nextcord, json, wavelink, os, asyncio, humanfriendly, aiohttp, datetime, main, re, yarl
from nextcord.ext import commands, menus
import spotipy
from wavelink.ext import spotify
from main import *
import tekore

class MessageDelete(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="Delete", style=nextcord.ButtonStyle.secondary, emoji="<:dustbin:949602736633167882>")  
    async def stop(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.message.delete()


def convert_time(seconds):
    m, s = divmod(seconds, 60)
    return "%02d:%02d" % (m, s)
class MyEmbedFieldPageSource(menus.ListPageSource):
    def __init__(self, data):
        super().__init__(data, per_page=10)

    async def format_page(self, menu, entries):
        embed = Embed(title="Entries")
        for entry in entries:
            embed.add_field(name=entry[0], value=entry[1], inline=True)
        embed.set_footer(text=f"Page {menu.current_page + 1}/{self.get_max_pages()}")
        return embed

class MyEmbedDescriptionPageSource(menus.ListPageSource):
    def __init__(self, data):
        super().__init__(data, per_page=10)

    async def format_page(self, menu, entries):
        embed = nextcord.Embed(title="Queue", description="\n".join(entries), colour=clr)
        embed.set_footer(text=f"Page {menu.current_page + 1}/{self.get_max_pages()}")
        return embed
class MusicController(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @nextcord.ui.button(style=nextcord.ButtonStyle.secondary, emoji="🔉")
    async def halfvolume(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        dj_role = nextcord.utils.get(interaction.guild.roles, name="Araki Dj")
        
        if dj_role in interaction.user.roles or interaction.user.permissions_in(interaction.channel).administrator:
            await interaction.response.send_message("Only Dj & Admins can use this option.")     
            if not interaction.guild.voice_client:
                embed = nextcord.Embed(description=f"📢 | Your are not playing a song.", color=clr)
                embed.set_author(name=f"{interaction.user.name}")
                await interaction.response.send_message(embed=embed, ephemeral=True)

            elif not getattr(interaction.user.voice, "channel", None):
                embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
                embed.set_author(name=f"{interaction.user.name}")
                await interaction.response.send_message(embed=embed, ephemeral=True)

            else:
                vc: wavelink.Player = interaction.guild.voice_client
                if vc.volume > 9:
                    newlow_vol = vc.volume - 10
                    await vc.set_volume(int(newlow_vol))
                    await interaction.response.send_message(f"Volume decrease to {vc.volume}", ephemeral=True)

                else:
                    await interaction.response.send_message("Volume is already too low!", ephemeral=True)
        else:
            await interaction.response.send_message("Only Dj & Admins can use this option.")     
            

          
    # @nextcord.ui.button(style=nextcord.ButtonStyle.secondary, emoji="🔈")
    # async def mute(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
              
    #     if not interaction.guild.voice_client:
    #         embed = nextcord.Embed(
    #             title="🔊 Set Volume Music", description=f"📢 | Your are not playing a song.", color=clr)
    #         embed.set_author(name=f"{interaction.user.avatar}",
    #                         icon_url=interaction.client.user.display_avatar)
    #         await interaction.response.send_message(embed=embed, ephemeral=True)

    #     elif not getattr(interaction.user.voice, "channel", None):
    #         embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
    #         embed.set_author(name=f"{interaction.user.name}")
    #         await interaction.response.send_message(embed=embed, ephemeral=True)

    #     else:
    #         vc: wavelink.Player = interaction.guild.voice_client

    
    #     await vc.set_volume(volume=0)
    #     await interaction.response.send_message("Successfully muted the player.", ephemeral=True)   
                                       
    # @nextcord.ui.button(style=nextcord.ButtonStyle.secondary, emoji="⏸️")
    # async def pause(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
       
    #     if not interaction.guild.voice_client:
    #         embed = nextcord.Embed(description=f"📢 | Your are not playing a song.", color=clr)
    #         embed.set_author(name=f"{interaction.user.name}")
    #         await interaction.response.send_message(embed=embed, ephemeral=True)

    #     elif not getattr(interaction.user.voice, "channel", None):
    #         embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
    #         embed.set_author(name=f"{interaction.user.name}")
    #         await interaction.response.send_message(embed=embed, ephemeral=True)

    #     else:
    #         vc: wavelink.Player = interaction.guild.voice_client

    #     embed = nextcord.Embed(description=f"📢 | ⏸️ Paused the player.", color=clr)
    #     embed.set_author(name=f"{interaction.user.name}")
    #     await vc.pause()
    #     await interaction.response.send_message(embed=embed, ephemeral=True)

    @nextcord.ui.button(style=nextcord.ButtonStyle.secondary, emoji="⏯️")
    async def resume(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if not interaction.guild.voice_client:
            embed = nextcord.Embed(description=f"📢 | Your are not playing a song.", color=clr)
            embed.set_author(name=f"{interaction.user.name}")
            await interaction.response.send_message(embed=embed, ephemeral=True)

        elif not getattr(interaction.user.voice, "channel", None):
            embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
            embed.set_author(name=f"{interaction.user.name}")
            await interaction.response.send_message(embed=embed, ephemeral=True)

        else:
            vc: wavelink.Player = interaction.guild.voice_client
            if not vc.is_paused():
                embedr = nextcord.Embed(description=f"📢 | ⏸️ Paused the player.", color=clr)
                embedr.set_author(name=f"{interaction.user.name}")
                await vc.pause()
                await interaction.response.send_message(embed=embedr, ephemeral=True)
            else:
                await vc.resume()
                embedp = nextcord.Embed(description=f"⏯️ Resumed the player.", color=clr)
                embedp.set_author(name=f"{interaction.user.name}")
                await interaction.response.send_message(embed=embedp, ephemeral=True)
            


    @nextcord.ui.button(style=nextcord.ButtonStyle.secondary, emoji="⏹️")
    async def stop(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if not interaction.guild.voice_client:
            embed = nextcord.Embed(description=f"📢 | Your are not playing a song.", color=clr)
            embed.set_author(name=f"{interaction.user.name}")
            await interaction.response.send_message(embed=embed, ephemeral=True)

        elif not getattr(interaction.user.voice, "channel", None):
            embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
            embed.set_author(name=f"{interaction.user.name}")
            await interaction.response.send_message(embed=embed, ephemeral=True)

        else:
            vc: wavelink.Player = interaction.guild.voice_client
        
        for child in self.children:
            child.disabled = True
            await interaction.message.edit(view=self)
        await vc.stop()
        await vc.disconnect()

    # @nextcord.ui.button(style=nextcord.ButtonStyle.secondary, emoji="🔉")
    # async def halfvolume(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
              
    #     if not interaction.guild.voice_client:
    #         embed = nextcord.Embed(description=f"📢 | Your are not playing a song.", color=clr)
    #         embed.set_author(name=f"{interaction.user.name}")
    #         await interaction.response.send_message(embed=embed, ephemeral=True)

    #     elif not getattr(interaction.user.voice, "channel", None):
    #         embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
    #         embed.set_author(name=f"{interaction.user.name}")
    #         await interaction.response.send_message(embed=embed, ephemeral=True)

    #     else:
    #         vc: wavelink.Player = interaction.guild.voice_client

    
    #     await vc.set_volume(volume=50)
    #     await interaction.response.send_message("Successfully set you volume to `50%`", ephemeral=True)    
       

    @nextcord.ui.button(style=nextcord.ButtonStyle.secondary, emoji="🔁")
    async def loop(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if not interaction.guild.voice_client:
            embed = nextcord.Embed(description=f"📢 | Your are not playing a song.", color=clr)
            embed.set_author(name=f"{interaction.user.name}")
            return await interaction.response.send_message(embed=embed, ephemeral=True)

        elif not getattr(interaction.user.voice, "channel", None):
            embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
            embed.set_author(name=f"{interaction.user.name}")
            return await interaction.response.send_message(embed=embed, ephemeral=True)

        else:
            vc: wavelink.Player = interaction.guild.voice_client

        try:
            vc.loop ^= True
        except Exception:
            setattr(vc, "loop", False)

        if vc.loop:
            return await interaction.response.send_message("Enabled Loop", ephemeral=True)        
        else:
            return await interaction.response.send_message("Disabled Loop", ephemeral=True)    

    @nextcord.ui.button(style=nextcord.ButtonStyle.secondary, emoji="🔊")
    async def fullvolume(self, button: nextcord.ui.Button, interaction= nextcord.Interaction):
              
        if not interaction.guild.voice_client:
            embed = nextcord.Embed(description=f"📢 | Your are not playing a song.", color=clr)
            embed.set_author(name=f"{interaction.user.name}")
            await interaction.response.send_message(embed=embed, ephemeral=True)

        elif not getattr(interaction.user.voice, "channel", None):
            embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
            embed.set_author(name=f"{interaction.user.name}")
            await interaction.response.send_message(embed=embed, ephemeral=True)

        else:
            vc: wavelink.Player = interaction.guild.voice_client
            if vc.volume <= 150:
                new_vol = vc.volume + 10
                await vc.set_volume(volume=int(new_vol))
                await interaction.response.send_message(f"Volume increase to {vc.volume}", ephemeral=True)
            else:
                await interaction.response.send_message("You can't increase volume more than 150", ephemeral=True)
                
    
        # await vc.set_volume(volume=1000)
        # await interaction.response.send_message("Successfully set you volume to `150%`", ephemeral=True)    
      

            
        
        
class Music(commands.Cog):

    COG_EMOJI = "🎶"
    
    def __init__(self, bot):
        self.bot = bot
        bot.loop.create_task(self.node_connect())

    async def node_connect(self):
        await self.bot.wait_until_ready()
        await wavelink.NodePool.create_node(bot=self.bot, 
                                            host="losingtime.dpaste.org", 
                                            port=2124, 
                                            password="SleepingOnTrains")
        await wavelink.NodePool.create_node(bot=self.bot, 
                                            host="lavalinkaraki1.herokuapp.com", 
                                            port=80, 
                                            password="youshallnotpass")

    @commands.Cog.listener()
    async def on_waveink_node_ready(self, node: wavelink.Node):
        print(f"Node <{node.identifier}> is ready!")

    @commands.Cog.listener()
    async def on_wavelink_track_end(self, player: wavelink.Player, track: wavelink.Track, reason):
        ctx = player.ctx
        vc: player = ctx.voice_client# Trank
        if vc.loop:
            return await vc.stop(), await vc.play(track), await songplayembed.edit(view=MusicController())

        elif vc.queue.is_empty and not vc.is_playing():
                return await vc.stop()

        else:
             
        
            next_song = vc.queue.get()

            view = MusicController()
            embed = nextcord.Embed(description=f"[{next_song.title}]({next_song.uri})", color=clr)
            embed.set_author(name=f"Now playing")
            embed.add_field(name="Duration", value=f"{convert_time(next_song.duration)}")
            embed.add_field(name="Default Volume", value=f"{vc.volume}")
            embed.add_field(name="Author", value=f"{next_song.author}")
            embed.set_thumbnail(url=next_song.thumbnail)
            await vc.stop()
            await vc.play(next_song)
            await songplayembed.edit(embed=embed, view=view)


                
    @commands.command(aliases=['p'])
    async def play(self, ctx: commands.Context, *, url: str):
            cn_id = ctx.channel.id

            if not ctx.voice_client:
                vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
                await ctx.send("Loading...", delete_after=0.2)

            if not ctx.author.voice:
                embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
                embed.set_author(name=f"{ctx.author.name}")
                return await ctx.send(embed=embed)

            elif not ctx.author.voice.channel == ctx.me.voice.channel:
                embed = nextcord.Embed(description="You are not in same voice channel.", color=clr)
                embed.set_author(name=f"{ctx.author.name}")
                await ctx.send(embed=embed)


            else:
            
                vc: wavelink.Player = ctx.voice_client
                # vc: wavelink.Player = ctx.voice_client
            # check spotify uri
            # decoded = spotify.decode_url(url)
            # # check spotify track
            # if decoded and decoded['type'] is spotify.SpotifySearchType.track:
            #     track = await spotify.SpotifyTrack.search(query=url)
            #     await vc.queue.put_wait(track)
            # # check spotify playlist
            # elif decoded and decoded['type'] is spotify.SpotifySearchType.playlist:
            #     async for track in spotify.SpotifyTrack.iterator(query=url, type=spotify.SpotifySearchType.playlist):
            #         await vc.queue.put_wait(track)
            # # check spotify album
            # elif decoded and decoded['type'] is spotify.SpotifySearchType.album:
            #     async for track in spotify.SpotifyTrack.iterator(query=url, type=spotify.SpotifySearchType.album):
            #         await vc.queue.put_wait(track)
            #         print(track.title)
            # check youtube uri
            # else:
                # check playlist or not
                check = yarl.URL(url)
                if check.query.get("list"):
                    playlist =  await wavelink.YouTubePlaylist.search(url)
                    for song in playlist.tracks:
                        await vc.queue.put_wait(song)
                    await ctx.reply(f"Added {len(playlist.tracks)} songs to the queue.", delete_after=10)
                else:
                    track = await wavelink.YouTubeTrack.search(query=url, return_first=True)
                    await vc.queue.put_wait(track)
                    if vc.is_playing():
                         embedq = nextcord.Embed(description=f"[{track.title}]({track.uri}) [{ctx.author.mention}]", color=clr)
                         embedq.set_author(name=f"Added Music to the queue.")
                         await ctx.reply(embed=embedq)

            if not vc.is_playing():
                tracks = await vc.play(vc.queue.get())
                embed = nextcord.Embed(description=f"[{vc.track.title}]({vc.track.uri})", color=clr)
                embed.set_author(name=f"Now playing")
                embed.add_field(name="Duration", value=f"{convert_time(vc.track.duration)}")
                embed.add_field(name="Default Volume", value=f"{vc.volume}")
                embed.add_field(name="Author", value=f"{vc.track.author}")
                embed.set_thumbnail(url=vc.track.thumbnail)
                global songplayembed
                songplayembed = await pranoy.get_channel(cn_id).send(embed=embed, view=MusicController())
            vc.ctx = ctx
            setattr(vc, "loop", False)

    # @commands.command(name="play", description="▶️ Plays a song for you that you want.", usage="<song name>", aliases=['p'])
    # async def play(self, ctx: commands.Context, *, search: str):
    #     if not ctx.voice_client:
    #         vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)

    #     elif not ctx.author.voice:
    #         embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
    #         embed.set_author(name=f"{ctx.author.name}")
    #         return await ctx.send(embed=embed)

    #     elif not ctx.author.voice.channel == ctx.me.voice.channel:
    #         embed = nextcord.Embed(description="You are not in same voice channel.", color=clr)
    #         embed.set_author(name=f"{ctx.author.name}")
    #         await ctx.send(embed=embed)

            
    #     else:
    
    #         vc: wavelink.Player = ctx.voice_client

    #     if not vc.is_playing():

    #             check = yarl.URL(url)
    #             if check.query.get("list"):
    #                 playlist =  await wavelink.YouTubePlaylist.search(url)
    #                 for song in playlist.tracks:
    #                     await vc.queue.put_wait(song)
    #                 await ctx.reply(f"Added {len(playlist.tracks)} songs to the queue.", delete_after=10)
    #             else:
    #                 track = await wavelink.YouTubeTrack.search(query=url, return_first=True)
    #                 await vc.queue.put_wait(track)
    #                 embedq = nextcord.Embed(description=f"[{track.title}]({track.uri}) [{ctx.author.mention}]", color=clr)
    #                 embedq.set_author(name=f"Added Music to the queue.")
    #                 await ctx.reply(embed=embedq)
    #             view = MusicController()
    #             embed = nextcord.Embed(description=f"[{search.title}]({search.uri})", color=clr)
    #             embed.set_author(name=f"Now playing")
    #             embed.add_field(name="Duration", value=f"{humanfriendly.format_timespan(search.duration)}")
    #             embed.add_field(name="Default Volume", value=f"{vc.volume}")
    #             embed.add_field(name="Author", value=f"{search.author}")
    #             embed.set_thumbnail(url=search.thumbnail)
    #             await vc.play(vc.queue.get())
    #             global songplayembed 
    #             songplayembed = await ctx.send(embed=embed, view=view)

    #     else:
    #         check = yarl.URL(url)
    #         if check.query.get("list"):
    #             playlist =  await wavelink.YouTubePlaylist.search(url)
    #             for song in playlist.tracks:
    #                 await vc.queue.put_wait(song)
    #             await ctx.reply(f"Added {len(playlist.tracks)} songs to the queue.", delete_after=10)
    #         else:
    #             track = await wavelink.YouTubeTrack.search(query=url, return_first=True)
    #             await vc.queue.put_wait(track)
    #             embedq = nextcord.Embed(description=f"[{track.title}]({track.uri}) [{ctx.author.mention}]", color=clr)
    #             embedq.set_author(name=f"Added Music to the queue.")
    #             await ctx.reply(embed=embedq)
    #         # await vc.queue.put_wait(search)
    #         # embed = nextcord.Embed(description=f"[{search.title}]({search.uri}) [{ctx.author.mention}]", color=clr)
    #         # embed.set_author(name=f"Added Music to the queue.")
    #         # msg = await ctx.send(embed=embed)
            
  
    #     vc.ctx = ctx
    #     setattr(vc, "loop", False)

    @commands.command(name="pause", description="⏸️ Pauses playing song.")
    async def pause(self, ctx: commands.Context):
        if not ctx.voice_client:
            embed = nextcord.Embed(description=f"📢 | Your are not playing a song.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            await ctx.send(embed=embed)

        elif not ctx.author.voice:
            embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            await ctx.send(embed=embed)

        else:
            vc: wavelink.Player = ctx.voice_client

        embed = nextcord.Embed(description=f"📢 | ⏸️ Paused the player.", color=clr)
        embed.set_author(name=f"{ctx.author.name}")
        await vc.pause()
        await ctx.send(embed=embed, view=None)

    @commands.command(name="resume", description="⏯️ Resumes playing song.")
    async def resume(self, ctx: commands.Context):
        if not ctx.voice_client:
            embed = nextcord.Embed(description=f"📢 | Your are not playing a song.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            await ctx.send(embed=embed)

        elif not getattr(ctx.author.voice, "channel", None):
            embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            await ctx.send(embed=embed)

        else:
            vc: wavelink.Player = ctx.voice_client

        embed = nextcord.Embed(description=f"⏯️ Resumed the player.", color=clr)
        embed.set_author(name=f"{ctx.author.name}")
        await vc.resume()
        await ctx.send(embed=embed)

    @commands.command(name="loop", description="Enables Looping")
    async def loop(self, ctx: commands.Context):
        if not ctx.voice_client:
            embed = nextcord.Embed(description=f"📢 | Your are not playing a song.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            await ctx.send(embed=embed)

        elif not getattr(ctx.author.voice, "channel", None):
            embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            await ctx.send(embed=embed)

        else:
            vc: wavelink.Player = ctx.voice_client

        try:
            vc.loop ^= True
        except Exception:
            setattr(vc, "loop", False)

        if vc.loop:
            return await ctx.send("Enabled Loop")        
        else:
            return await ctx.send("Disabled Loop")        


    @commands.command(name="queue", description="Queues a song..", aliases=['q'])
    async def queue(self, ctx: commands.Context):
        if not ctx.voice_client:
            embed = nextcord.Embed(description=f"📢 | Your are not playing a song.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            message = await ctx.send(embed=embed)
            return message, await asyncio.sleep(5), await message.delete()

        elif not getattr(ctx.author.voice, "channel", None):
            embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            message = await ctx.send(embed=embed)
            return message,await asyncio.sleep(5),await message.delete()

        else:
            vc: wavelink.Player = ctx.voice_client    

        if vc.queue.is_empty:
            embede = nextcord.Embed(description=f"📢 | The queue is empty.", colour=clr)
            embede.set_author(name=f"{ctx.author.name}")
            await ctx.send(embed=embede, view=MessageDelete())
        else:



            upcoming = []
            total_duration = 0             
            embed = nextcord.Embed(title="Queue",description=f"To skip on a perticular song use /skipto <song number>",colour=clr)
            queue = vc.queue.copy()
            song_count = 0
            for song in queue:
                song_count +=1
                upcoming.append(f"{song_count} - [{song.title}]({song.uri})")
            pages = menus.ButtonMenuPages(
            source=MyEmbedDescriptionPageSource(upcoming),
            clear_buttons_after=True,
    )   
            await pages.start(ctx)

    @commands.command(name="clearq", aliases=["clq", "clearqueue"])
    async def clearq(self, ctx: commands.Context):
        """Clear the player's queue."""
        if not ctx.voice_client:
            embed = nextcord.Embed(description=f"📢 | Your are not playing a song.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            await ctx.send(embed=embed)


        elif not getattr(ctx.author.voice, "channel", None):
            embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            await ctx.send(embed=embed)
        else:
            vc: wavelink.Player = ctx.voice_client
            if vc.queue.is_empty:
                await ctx.reply("Queue is empty tho, No things to clear!", delete_after=10)
            else:
                vc.queue.clear()
                await ctx.reply("Queue has been cleared!", delete_after=10)

    @commands.command()
    async def suffle(self, ctx: commands.Context):
        """Clear the player's queue."""
        if not ctx.voice_client:
            embed = nextcord.Embed(description=f"📢 | Your are not playing a song.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            await ctx.send(embed=embed)

        elif not getattr(ctx.author.voice, "channel", None):
            embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            await ctx.send(embed=embed)
        else:
            vc: wavelink.Player = ctx.voice_client
            if vc.queue.is_empty:
                await ctx.reply("Queue is empty tho, No things to clear!", delete_after=10)
            else:
                random.shuffle(vc.queue._queue)
                await ctx.reply("Queue is now shuffle!")

    
    

    @commands.command(name="stop", description="⏸ Stops playing song.")
    async def stop(self, ctx: commands.Context):
        if not ctx.voice_client:
            embed = nextcord.Embed(description=f"📢 | Your are not playing a song.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            message = await ctx.send(embed=embed)
            return message, await asyncio.sleep(5), await message.delete()

        elif not getattr(ctx.author.voice, "channel", None):
            embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            message = await ctx.send(embed=embed)
            return message, await asyncio.sleep(5), await message.delete()

        else:
            vc: wavelink.Player = ctx.voice_client

        embed = nextcord.Embed(description=f"📢 | ⏸️ Stoped the player.", color=clr)
        embed.set_author(name=f"{ctx.author.name}")
        await vc.stop()
        message = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await message.delete()

    @commands.command(name="disconnect", aliases=["dc"], description="🔌 Disconnects from the vc.")
    async def vcdisconnect(self, ctx: commands.Context):
        if not ctx.voice_client:
            embed = nextcord.Embed(description=f"📢 | Your are not playing a song.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            message = await ctx.send(embed=embed)
            return message
            await asyncio.sleep(5)
            await message.delete()

        elif not getattr(ctx.author.voice, "channel", None):
            embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            message = await ctx.send(embed=embed)
            return message
            await asyncio.sleep(5)
            await message.delete()

        else:
            vc: wavelink.Player = ctx.voice_client

        embed = nextcord.Embed(description=f"📢 |🔌 Disconnected Successfully.", color=clr)
        embed.set_author(name=f"{ctx.author.name}")
        await vc.disconnect()
        message = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await message.delete()

    @commands.command(name="connect", description="🔌 Connects from the vc.", aliases=['join'])
    async def connect(self, ctx: commands.Context):
        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)

        elif not getattr(ctx.author.voice, "channel", None):
            embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            message = await ctx.send(embed=embed)
            return message, await asyncio.sleep(5), await message.delete()

        else:
            vc: wavelink.Player = ctx.voice_client

        embed = nextcord.Embed(description=f"📢 |🔌 Connected Successfully.", color=clr)
        embed.set_author(name=f"{ctx.author.name}")
        await vc.connect(timeout=14, reconnect=True)
        message = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await message.delete()

    @commands.command(name="volume", aliases=["setvolume", "changevolume"], descrtiption="Sets the volume of the player.")
    async def setvolume(self, ctx: commands.Context, *, volume: int):
        if not ctx.voice_client:
            embed = nextcord.Embed(description="📢 | I am not in a voice channel.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            message = await ctx.send(embed=embed)
            return message, await asyncio.sleep(4), message.delete()

        elif not ctx.author.voice:
            embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            message = await ctx.send(embed=embed)
            return message, await asyncio.sleep(4), message.delete()

            
        else:
            vc: wavelink.Player = ctx.voice_client

        if volume > 150:
            msg = await ctx.send(":angry: It's too much high.")    
            await asyncio.sleep(4)
            await msg.delete()

        elif volume < 0:
            msg = await ctx.send(":angry: It's too low.")    
            await asyncio.sleep(4)
            await msg.delete()
           
        else:   

            msg = await ctx.send(f"Set your 🔊 volume to `{volume}%`")   
            return await vc.set_volume(volume), msg,  await asyncio.sleep(3), await msg.delete()



    @commands.command(name="nowplaying", aliases=["np", "songinfo"], description="Shows the info about the currently playing song.")
    async def nowplaying(self, ctx: commands.Context):
        if not ctx.voice_client:
            embed = nextcord.Embed(description="📢 | I am not in a voice channel.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            message = await ctx.send(embed=embed)
            return message, await asyncio.sleep(4), message.delete()

        elif not ctx.author.voice:
            embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            message = await ctx.send(embed=embed)
            return message, await asyncio.sleep(4), message.delete()

            
        else:
            vc: wavelink.Player = ctx.voice_client

        if not vc.is_playing():
            embed = nextcord.Embed(description="📢 | You are not even playing a music.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            message = await ctx.send(embed=embed)
            return message, await asyncio.sleep(4), message.delete()

        embed = nextcord.Embed(title="Now Playing", description=f"{vc.track.title}", color=clr)
        embed.add_field(name='Author', value=vc.track.author)
        embed.add_field(name="Duration", value=f"{convert_time(vc.position)}/{convert_time(vc.track.duration)}")
        embed.set_thumbnail(url=vc.track.thumbnail)
        await ctx.send(embed=embed, view=MessageDelete())    



    @commands.command(name="lyrics", description="Sends the lyrics of the song.", usage="<song name>")
    async def lyrics(self, ctx):
        vc: wavelink.Player = ctx.voice_client
        url = f"https://some-random-api.ml/lyrics?title={vc.track.title}"


        async with ctx.typing():
            async with aiohttp.request("GET", url+vc.track.title, headers={}) as r :
                try:
                    if not r.status == 200:
                        view = MessageDelete()
                        embed = nextcord.Embed(title="Aw Snap!",description="I wasn't able to find the lyrics of that song.",color = clr)
                        await ctx.send(embed=embed, view=view)

                    data = await r.json()
                    if len(data["lyrics"]) > 2000:
                        view = MessageDelete()
                        return await ctx.send(f"The lyrcis exceeded the limit so here is the link for the lyrics: <{data['links']['genius']}>", view=view)

                    view = MessageDelete()
                    embed = nextcord.Embed(title=data["title"], description=data["lyrics"], colour=clr) 
                    embed.set_author(name=data["author"])
                    embed.set_thumbnail(url=data["thumbnail"]["genius"])  
                    await ctx.send(embed=embed, view=view) 

                except KeyError:
                    pass

    @commands.command()
    async def skip(self, ctx):
        vc: player = ctx.voice_client


        if not ctx.voice_client:
            embed = nextcord.Embed(description=f"📢 | Your are not playing a song.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            message = await ctx.send(embed=embed)
            return message
            await asyncio.sleep(5)
            await message.delete()

        elif not ctx.author.voice:
            embed = nextcord.Embed(description="📢 | Join a voice channel please.", color=clr)
            embed.set_author(name=f"{ctx.author.name}")
            message = await ctx.send(embed=embed)
            return message
            await asyncio.sleep(5)
            await message.delete()

        elif vc.loop:
            return
        else:

            if vc.queue.is_empty:
                await ctx.reply("There is nothing to skip!")
            elif vc.loop:
                await vc.stop()
                await ctx.send("There is nothing to skip. Song Stop!")
            else:
                await vc.stop()
                await ctx.send("Song skipped")

        
def setup(bot):
    bot.add_cog(Music(bot))
