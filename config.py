TOKEN=""
OWNERS=['943571992722944041']
support_link = "https://araki.social/support"
invite_link = "https://araki.social/invite"
footer = "Made by Pranoy#0140"
dbl_vote = "https://discordbotlist.com/bots/araki/upvote"
topgg = "https://araki.social/vote"
import nextcord, motor, json, asyncio, random
from nextcord.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient
cluster = AsyncIOMotorClient(['mongodb+srv://pranoycasito:ricky&casito@cluster0.m9at5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'])
db = cluster["main"]
cursor = db["economy"]
# welcome
db = cluster["main"]
welcome = db["welcome"]

# leave
db = cluster["main"]
leave = db["leave"]

# Marry

db = cluster["main"]
marrydb = db['marry']
# Shop

db = cluster["main"]
inv = db["inv"]
mainshop = [
      {"name": "Frequent Circlet ```ID - 1```", "price": 100000, "value": '<:frequentcirclet:949535577806626836>'},
      {"name": "Scarce Circlet ```ID - 2```", "price": 300000, "value": '<:scarcecirclet:949535658291105822>'},
      {"name": "Rare Circlet ```ID - 3```", "price": 500000, "value": '<:rarecirclet:949535438044037142>'},
      {"name": "Saga Circlet ```ID - 4```", "price": 1000000, "value": '<:sagacirclet:949535347145068574>'}
    ]

db = cluster["main"]
wlcm_msg = db['wlcm_msg']
