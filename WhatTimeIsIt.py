import os
import discord
from discord import Intents
from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv
import numpy as np
import math
import random
from datetime import datetime
import asyncpraw
import requests
import json
import time
from googleapiclient.discovery import build

#Enables discord privalleged intents
intents=Intents.all() 

#Gets keys from .env
load_dotenv() 
TOKEN = os.getenv('DISCORD_TOKEN')
ID = os.getenv('CLIENT_ID')
SECRET = os.getenv('CLIENT_SECRET')
AGENT = os.getenv('USER_AGENT')
YT_KEY = os.getenv('API_KEY')

#Connects to Reddit and YT api
reddit = asyncpraw.Reddit(client_id = ID, client_secret = SECRET, user_agent = AGENT)
youtube = build('youtube', 'v3', developerKey=YT_KEY)

#Enables bot commands
bot = commands.Bot(command_prefix='$', intents = intents)

#Assign users in a specified server a specific role
@bot.event
async def on_member_join(member):
    server = bot.get_guild(949085413555974204)
    role = server.get_role(949092377161793627)
    await member.add_roles(role)

#Creates a list of possible Hour and Minutes digits
T1=np.linspace(1,12,12)
T2=np.linspace(0,5,6)
T3=np.linspace(0,9,10)

t1 = []
t2 = []
t3 = []

#Reformats the digits
for i in T1:
    s = math.trunc(i)
    t1.append(s)
    i+=1

for i in T2:
    s = math.trunc(i)
    t2.append(s)
    i+=1
    
for i in T3:
    s = math.trunc(i)
    t3.append(s)
    i+=1
    
t=[]

#Makes a list of all possible time arrangements    
for i in range(0,12):
    for j in t2:
        for k in t3:
            s = str(t1[i])+':'+str(t2[j])+str(t3[k])
            t.append(s)
            k+=1
        j+=1
    i+=1

#Adds some fancy easter eggs to the list of times
t.append("too late to apologize (it’s too late)")
t.append("too late to apologize (it’s too late)")
t.append("too late to apologize (it’s too late)")
t.append("too late to apologize (it’s too late)")
t.append("too late to apologize (it’s too late)")
t.append("too late to apologize (it’s too late)")
t.append("too late to apologize (it’s too late)")
t.append("too late to apologize (it’s too late)")
t.append("too late to apologize (it’s too late)")
t.append("too late to apologize (it’s too late)")
t.append("too late to apologize (it’s too late)")
t.append("too late to apologize (it’s too late)")
t.append("too late to apologize (it’s too late)")
t.append("too late to apologize (it’s too late)")
t.append("too late to apologize (it’s too late)")
t.append("too late to apologize (it’s too late)")
t.append("too late to apologize (it’s too late)")
t.append("time to get some bitches")
t.append("time to get some bitches")
t.append("time to get some bitches")
t.append("time to get some bitches")
t.append("time to get some bitches")
t.append("time to get some bitches")
t.append("time to get some bitches")
t.append("time to get some bitches")
t.append("time to get some bitches")
t.append("time to get some bitches")
t.append("time to get some bitches")
t.append("time to get some bitches")
t.append("time to get some bitches")
t.append("\n\u1CBC                        1 2 \n                11         ^         1 \n      10                  |                2 \n                            |\n 9                       ⊙-----------> Despacito'clock \n\n       8                                   4 \n                 7                   5 \n                            6                                                            ")
t.append("\n\u1CBC                        1 2 \n                11         ^         1 \n      10                  |                2 \n                            |\n 9                       ⊙-----------> Despacito'clock \n\n       8                                   4 \n                 7                   5 \n                            6                                                            ")
t.append("\n\u1CBC                        1 2 \n                11         ^         1 \n      10                  |                2 \n                            |\n 9                       ⊙-----------> Despacito'clock \n\n       8                                   4 \n                 7                   5 \n                            6                                                            ")
t.append("\n\u1CBC                        1 2 \n                11         ^         1 \n      10                  |                2 \n                            |\n 9                       ⊙-----------> Despacito'clock \n\n       8                                   4 \n                 7                   5 \n                            6                                                            ")
t.append("\n\u1CBC                        1 2 \n                11         ^         1 \n      10                  |                2 \n                            |\n 9                       ⊙-----------> Despacito'clock \n\n       8                                   4 \n                 7                   5 \n                            6                                                            ")
t.append("\n\u1CBC                        1 2 \n                11         ^         1 \n      10                  |                2 \n                            |\n 9                       ⊙-----------> Despacito'clock \n\n       8                                   4 \n                 7                   5 \n                            6                                                            ")
t.append("\n\u1CBC                        1 2 \n                11         ^         1 \n      10                  |                2 \n                            |\n 9                       ⊙-----------> Despacito'clock \n\n       8                                   4 \n                 7                   5 \n                            6                                                            ")
t.append("\n\u1CBC                        1 2 \n                11         ^         1 \n      10                  |                2 \n                            |\n 9                       ⊙-----------> Despacito'clock \n\n       8                                   4 \n                 7                   5 \n                            6                                                            ")
t.append("\n\u1CBC                        1 2 \n                11         ^         1 \n      10                  |                2 \n                            |\n 9                       ⊙-----------> Despacito'clock \n\n       8                                   4 \n                 7                   5 \n                            6                                                            ")
t.append("\n\u1CBC                        1 2 \n                11         ^         1 \n      10                  |                2 \n                            |\n 9                       ⊙-----------> Despacito'clock \n\n       8                                   4 \n                 7                   5 \n                            6                                                            ")

merd = ['AM', 'PM']

#Prints a list of all servers the bot is connected to when on startup
@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
        )
#Gets a random quote that will be used in the shrimper command
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

#Chooses a random time from the list of times
@bot.command(name='time')
async def time(ctx):
   time = random.choice(t)
   merd2 = random.choice(merd)
   response = "It is currently" + " " + str(time) + " " + merd2
   await ctx.send(response)

#Secret command with an invisble character to return the correct time
@bot.command(name='time\u1CBC')
async def timer(ctx):
    now = datetime.now()
    current_time = now.strftime('%I:%M %p')
    response =("It is currently " + current_time)
    await ctx.send(response)

#Tracks Toontown invasion status
@bot.command(name='inv')
async def inv(ctx):
    res = requests.get('https://www.toontownrewritten.com/api/invasions')
    res_json = res.json()
    if res.status_code != 200:
        await ctx.send("Can't help you with that one.\nSorry, retard.")
    else:
        response = "```\n"
        for location in res_json['invasions'].keys():
            response += f"{res_json['invasions'][location]['type']}\n{location}\n{res_json['invasions'][location]['progress']} cogs\n\n"
        response += '```'
        await ctx.send(response)

#Checks if the actual shrimp bot 
@bot.command(name='shrimp')
async def shrimp(ctx):
    try:
        if ctx.guild.get_member(925895595334438953).raw_status != "online":
           await ctx.send("The Shrimp Boat Has Left")
    except:
        return

#Gets a random picture from the top 50 list on r/shrimptank and combines it with a quote
@bot.command(name='shrimper')
async def shrimper(ctx):
    sub = await reddit.subreddit('shrimptank')
    posts = []
    count = 0
    LIMIT = 50
    async for submission in sub.hot(limit=LIMIT):
        url = str(submission.url)
        if (url.endswith('jpg') or url.endswith('jpeg') or url.endswith('png')):
            posts.append(url)
            if count == LIMIT:
                break
    quote=get_quote()
    response = random.choice(posts)
    sub = None
    await ctx.send(response)
    await ctx.send(quote)

#Checks the youtube api every 30 minutes for soarviverforevers most recent video and posts the link if it differs from the previously stored video id
@tasks.loop(minutes=30.0, count=None)
async def job():
    await bot.wait_until_ready()
    request = youtube.playlistItems().list(
            part="snippet",
            maxResults=1,
            playlistId="UUKg6MTw48peEyW-z1u1z2jQ"
        )
    response = request.execute()
    for (k, v) in response.items():
        if(k == 'items'):
            video_ids = [pli['snippet']['resourceId']['videoId'] for pli in v if pli['snippet']['resourceId']['kind']=='youtube#video']
    recent = video_ids
    print(video_ids)
    channel = bot.get_channel(id=937430616306233385)
    print(channel)
    op = open("yt_id.txt", "r")
    saved = op.read()
    op.read()
    if video_ids[0] != saved:
        fo = open("yt_id.txt", "w")
        fo.write(video_ids[0])
        fo.close()
        await channel.send('https://www.youtube.com/watch?v='+str(recent[0]))
job.start()

bot.run(TOKEN)



