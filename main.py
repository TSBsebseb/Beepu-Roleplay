import os
import nextcord
import random 
import datetime
import dotenv
from nextcord.ext import commands
from nextcord.utils import get
from nextcord.ext.commands import has_role

intents = nextcord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="Br."or'br.',intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        
        
            
      print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})')
my_secret = os.environ['TOKEN']

@client.command(name = 'setup', help= 'sets up bot and blacklist channels')
async def make_chan(ctx):
  user = ctx.message.author
  #servers = await guild.create_text_channel('Blacklist logs')

  if ctx.guild.owner_id != user.id:
    await ctx.send('you are not the owner')
  
  else:
    await ctx.send('Starting setup please wait......')
    Chan_name = []
    for channel in ctx.guild.text_channels:
      if str(channel.type) == 'text':

        Chan_name.append(channel.name)

    
       
      
    
    
    
    await ctx.send('Creating blacklist logs....')
    if "blacklist_logs" not in Chan_name:
      await ctx.message.guild.create_text_channel("blacklist_logs")
    else:
      await ctx.send('Blacklist logs already created ')

    await ctx.send('Creating broadcast alerts')
    if "broadcast_alerts" not in Chan_name:
      await ctx.message.guild.create_text_channel("broadcast_alerts")
    else:
      await ctx.send('Broadcast alerts already created')
      
      return

    await ctx.send('Setup finished')


#set a list of maps by urban and milsim 
urban = ['Suburbia', 
         'Backstreets', 
         'quarantine', 
         'Vacant', 
         'The Hook 2.0']

milsim = ["Downfall",
      "Kashlan",
      "Al-Madinah",
      "Paradise",
      "Sand",
      "Frostbite",
      "Ashes in the Snow",
      "The Hook 2.0"]


#make map command to get a random map 
@client.command(name = 'map',help = 'generates a map for rp ') 
async def maps(ctx, *, map = None ):
  if map =='urban':
   map = urban
  elif map == 'milsim':
    map = milsim
  map_choice = random.choice(map)
  await ctx.send(f'your map is {map_choice}')







client.run('TOKEN')