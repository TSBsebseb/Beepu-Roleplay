import keep_alive

import os
import nextcord
import random 
import datetime
import statcord
from datetime import datetime
from datetime import timedelta
import dotenv
from nextcord import invite
from nextcord.ext import commands
from nextcord.utils import get
from nextcord.ext.commands import has_role
os.getenv("TOKEN")
intents = nextcord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix=["Br.",'br.'],intents=intents)

@client.event
async def on_ready():
  print(f'{client.user} is connected to the following guild:\n')
  for guild in client.guilds:
    print(f'{guild.name}(id: {guild.id})')


@client.command(name = 'setup', help= 'sets up bot and blacklist channels')
async def make_chan(ctx):
  user = ctx.message.author
  

  if ctx.guild.owner_id != user.id:
    await ctx.send('you are not the owner')
  
  else:
    await ctx.send('Starting setup please wait......')
    Chan_name = []
    for channel in ctx.guild.text_channels:
      if str(channel.type) == 'text':

        Chan_name.append(channel.name)

    
    member_role =[]
    for role1 in ctx.guild.roles:
      member_role.append(role1.name)
      
    
    
    
    await ctx.send('Creating event sessions....')
    if "roleplay-sessions" not in Chan_name:
      await ctx.message.guild.create_text_channel("event sessions")
    else:
      await ctx.send('event session  already created ')

    await ctx.send('Creating broadcast alerts')
    if "broadcast_alerts" not in Chan_name:
      await ctx.message.guild.create_text_channel("broadcast_alerts")
    else:
      await ctx.send('Broadcast alerts already created')
    
    await ctx.send('creating roleplay role')
    if 'Roleplay' not in member_role:
      await ctx.guild.create_role(name='Roleplay')
    else:
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


# Rp command 
@client.command(name='rp' ,help= 'creates an event Syntax: rp(name) (in how many hours from now is it starting) (details of the event)')
async def rp(ctx, name=None,hour = None, *, reason = None):
  location = nextcord.EntityMetadata(location='roleplay-sessions')
  external = nextcord.ScheduledEventEntityType.external
  
  time = datetime.now() + timedelta(hours = int(hour))
  end = time + timedelta(hours = 3)

  await ctx.guild.create_scheduled_event(name=name, start_time = time, end_time = end, description = reason, entity_type = external , metadata = location)
  await ctx.send(f'created {name}')


@client.command(name = 'event.all', help = 'shows all active events')
async def event(ctx):
  event = []
  for events in ctx.guild.scheduled_events:
    event.append(events.name)

    
   
  delimeter = ' ' 
  event = delimeter.join(event)
  beepu =nextcord.Embed(title=f"Events for {ctx.guild.name}")
  beepu.add_field(name = "below is all events and info", value = f'\n{event}')
  await ctx.send(embed = beepu)


@client.command(name = 'event.link', help = 'get the invite link for an event')
async def look_up(ctx, *, name = None):
  for event in ctx.guild.scheduled_events:
    if name == event.name:
      id_event = event.id
      i = 0
      channel = ctx.guild.text_channels[i] 
      link= await channel.create_invite(max_age=300,max_uses=0)
      invite_link = str(link) + f'?event={id_event}'
    
      await ctx.send(f'here your event {invite_link}')
    
  




@client.command(name='invite', help='give the bot invite link')
async def link(ctx):
    beepu =nextcord.Embed(title="Invite me")
    beepu.add_field(name="Click below to invite me to your guild", value=f"[Click here to invite](https://discord.com/api/oauth2/authorize?client_id=930091339029303366&permissions=8858518545&scope=bot)")
    await ctx.send(embed=beepu)


@client.command(name= "code", help= "creates a 4 digit code")
async def fuck(ctx):
    boy = num = random.randint(1000,9999)
    await ctx.send(boy)


# Create invite 
@client.command(name='link', help='')
@commands.is_owner()
async def createinvite(ctx, guildid: int):
  try:
    guild = client.get_guild(guildid)
    invitelink = ""
    i = 0
    while invitelink == "":
      channel = guild.text_channels[i]
      link = await channel.create_invite(max_age=300,max_uses=1)
      invitelink = str(link)
      i += 1
    await ctx.send(invitelink)
  except Exception:
    await ctx.send("Something went wrong")

    
# SERVERS COMMAND GIVES ALL SERVERS AND IDS 
@client.command(name='servers', help='')
@commands.is_owner()
async def servers(self):
        messages = []
        for guild in client.guilds:
             messages.append(f"{guild.name} (id: {guild.id})")
        beepu= ("\n".join(messages))
        embed=nextcord.Embed(title="Beepu roleplay", description= beepu, color=0xFF5733)
        await self.send(embed=embed)

key = "statcord.com-OuutdmjoweWTlipszvvC"
api = statcord.Client(client,key)
api.start_loop()

@client.event
async def on_command(ctx):
    api.command_run(ctx)




client.run('')

