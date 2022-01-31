import discord
from discord.ext import commands
from discord_components import *
import aiohttp
import urllib
import io
import pyjokes
import datetime
import randfacts
import requests
import json
import random
import asyncio

client = commands.Bot(command_prefix = "m;", help_command=None, activity=discord.Game(name="m;help", type=3))

@client.event
async def on_ready():
    print(f'{client.user.name} is booted up!')
    
# Variables

general = f'''
**{client.command_prefix}inspire** - Inspirational Quotes.
**{client.command_prefix}fact** - Fun Facts.
**{client.command_prefix}weather** - Weather in a certain city.
**{client.command_prefix}calc** - Fires up a calculator.
'''

animal_fact_list = f'''
**{client.command_prefix}panda** - Facts about Pandas.
**{client.command_prefix}dog** - Facts about Dogs.
**{client.command_prefix}cat** - Facts about Cats.
**{client.command_prefix}fox** - Facts about Foxes.
**{client.command_prefix}koala** - Facts about Koala Bears.
**{client.command_prefix}bird** - Facts about Birds.
**{client.command_prefix}whale** - Facts about Whales.
'''

gamey = f'''
**{client.command_prefix}sus** - New tech: Sussometer.
**{client.command_prefix}joke** - Jokes (warning: most of them are programmer related).
**{client.command_prefix}trigger** - Triggers a user.
**{client.command_prefix}deepfry** - Deepfries a user.
''' 

moderation = f'''
**{client.command_prefix}ban** - Bans a member.
**{client.command_prefix}unban** - Unbans a member.
**{client.command_prefix}kick** - Kicks a member.
**{client.command_prefix}mute** - The mentioned user cannot ping in the server until unmuted.
**{client.command_prefix}unmute** - Unmutes the mentioned user.
'''

about = f'''
**{client.command_prefix}dev** - Developer Info.
**{client.command_prefix}link** - Developer Page.
**{client.command_prefix}about** - Who's Moon Knight?
'''

page1 = discord.Embed(title = "General Commands", description = general, color = 0xf5f6fa)
page2 = discord.Embed(title = "Animal Facts", description = animal_fact_list, color = 0xfeca57)
page3 = discord.Embed(title = "Gamey Commands", description = gamey, color = 0xff6b6b)
page4 = discord.Embed(title = "Moderation Commands", description = moderation, color = 0x5f27cd)
page5 = discord.Embed(title = "About Section", description = about, color = 0xf5f6fa)

client.help_pages = [page1, page2, page3, page4, page5]

splash_screen = [
    "Loading the calculator, hold on!",
    "Just a minute, the calculators waking from it's grave.",
    "The dark lord.. I mean, the dark calculator is arriving on his broomstick!",
    "Buckle up, calculator's loading!",
    "Yo, life needs patience, so wait 2 secs until I load!",
]

# API References

api_key = "fcbb98321e257dd2bfe82725efeb394c"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

def get_panda():
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/facts/panda")
    if 300 > resp.status_code >= 200:
        content = resp.json()
        content = content["fact"]
    else:
        content = f"Error {resp.status_code}."
        
    return content
def get_dog():
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/facts/dog")
    if 300 > resp.status_code >= 200:
        content = resp.json()
        content = content["fact"]
    else:
        content = f"Error {resp.status_code}."
        
    return content
def get_cat():
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/facts/cat")
    if 300 > resp.status_code >= 200:
        content = resp.json()
        content = content["fact"]
    else:
        content = f"Error {resp.status_code}."
        
    return content
def get_fox():
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/facts/fox")
    if 300 > resp.status_code >= 200:
        content = resp.json()
        content = content["fact"]
    else:
        content = f"Error {resp.status_code}."
        
    return content
def get_koala():
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/facts/koala")
    if 300 > resp.status_code >= 200:
        content = resp.json()
        content = content["fact"]
    else:
        content = f"Error {resp.status_code}."
        
    return content
def get_bird():
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/facts/birb")
    if 300 > resp.status_code >= 200:
        content = resp.json()
        content = content["fact"]
    else:
        content = f"Error {resp.status_code}."
        
    return content
def get_whale():
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/facts/whale")
    if 300 > resp.status_code >= 200:
        content = resp.json()
        content = content["fact"]
    else:
        content = f"Error {resp.status_code}."
        
    return content

# General Commands
@client.command()
async def inspire(ctx):
    quote = get_quote()
    await ctx.send(embed = discord.Embed(title = "A wise man once said...", description = quote, color = 0xf5f6fa))

@client.command()
async def fact(ctx):
    fact = randfacts.get_fact()
    await ctx.send(embed = discord.Embed(title = "Facts", description = fact, color = 0xf5f6fa))
    
@client.command()
async def weather(ctx, *, city: str):
    city_name = city.capitalize()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel
    
    if x["cod"] != "404":
        async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsius = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            
            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Weather in {city_name}",
                              timestamp=ctx.message.created_at,)
            embed.add_field(name="Description", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsius}°C**", inline=False)
            embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.pinimg.com/originals/77/0b/80/770b805d5c99c7931366c2e84e88f251.png")
            embed.set_footer(text=f"Weather command used by {ctx.author.name}")
            
            await ctx.reply(embed=embed)
    else:
        await ctx.reply("Huh, I couldn't find the city mentioned. Is it the right city?")
        
# Calculator

# buttons array
buttons = [
    [
        Button(style=ButtonStyle.grey, label='1'),
        Button(style=ButtonStyle.grey, label='2'),
        Button(style=ButtonStyle.grey, label='3'),
        Button(style=ButtonStyle.blue, label='×'),
        Button(style=ButtonStyle.red, label='Exit')
    ],
    [
        Button(style=ButtonStyle.grey, label='4'),
        Button(style=ButtonStyle.grey, label='5'),
        Button(style=ButtonStyle.grey, label='6'),
        Button(style=ButtonStyle.blue, label='÷'),
        Button(style=ButtonStyle.red, label='←')
    ],
    [
        Button(style=ButtonStyle.grey, label='7'),
        Button(style=ButtonStyle.grey, label='8'),
        Button(style=ButtonStyle.grey, label='9'),
        Button(style=ButtonStyle.blue, label='+'),
        Button(style=ButtonStyle.red, label='Clear')
    ],
    [
        Button(style=ButtonStyle.grey, label='00'),
        Button(style=ButtonStyle.grey, label='0'),
        Button(style=ButtonStyle.grey, label='.'),
        Button(style=ButtonStyle.blue, label='-'),
        Button(style=ButtonStyle.green, label='=')
    ],
]


# calculates answer
def calculate(exp):
    o = exp.replace('×', '*')
    o = o.replace('÷', '/')
    result = ''
    try:
        result = str(eval(o))
    except:
        result = 'Oh Crap! An error occurred!'
    return result


@client.command()
async def calc(ctx):
    m = await ctx.send(content=random.choice(splash_screen))
    expression = '⠀'
    delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    e = discord.Embed(title=f'{ctx.author.name}\'s calculator | {ctx.author.id}', description=expression,
                      timestamp=delta)
    await m.edit(components=buttons, embed=e)
    while m.created_at < delta:
        res = await client.wait_for('button_click')
        if res.author.id == int(res.message.embeds[0].title.split('|')[1]) and res.message.embeds[
            0].timestamp < delta:
            expression = res.message.embeds[0].description
            if expression == '⠀' or expression == 'Oh Crap! An error occurred!':
                expression = ''
            if res.component.label == 'Exit':
                await res.respond(content='Calculator Closed', type=7)
                break
            elif res.component.label == '←':
                expression = expression[:-1]
            elif res.component.label == 'Clear':
                expression = '⠀'
            elif res.component.label == '=':
                expression = calculate(expression)
            else:
                expression += res.component.label
            f = discord.Embed(title=f'{res.author.name}\'s calculator|{res.author.id}', description=expression,
                              timestamp=delta)
            await res.respond(content='', embed=f, components=buttons, type=7)


# Gamey Commands
@client.command()
async def sus(ctx):
    sussiness = random.randint(0,100)
    await ctx.send(embed = discord.Embed(title = "Sussometer", description = f'You are {sussiness}% sus.', color = 0xe84118))
    
@client.command()
async def joke(ctx):
    joke = pyjokes.get_joke()
    await ctx.send(embed = discord.Embed(title = "Jokes", description = joke, color = 0xf5f6fa))
    
@client.command()
async def trigger(ctx, member: discord.Member=None):
    if not member: # if no member is mentioned
        member = ctx.author # the user who ran the command will be the member
        
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg: # get users avatar as png with 1024 size
            imageData = io.BytesIO(await trigImg.read()) # read the image/bytes
            
            await trigSession.close() # closing the session and;
            
            await ctx.reply(file=discord.File(imageData, 'triggered.gif')) # sending the file
        

# Animal Facts
@client.command()
async def panda(ctx):
    fact = get_panda()
    e = discord.Embed(title = "Pandas", description = fact, color = 0xf5f6fa)
    e.set_thumbnail(url="https://www.rd.com/wp-content/uploads/2020/03/GettyImages-1060486568.jpg?fit=700,1024")
    await ctx.send(embed = e)
    
@client.command()
async def dog(ctx):
    fact = get_dog()
    e = discord.Embed(title = "Dogs", description = fact, color = 0xf5f6fa)
    e.set_thumbnail(url="https://spiritdogtraining.com/wp-content/uploads/2021/09/pomeranian-first-time.png")
    await ctx.send(embed = e)

@client.command()
async def cat(ctx):
    fact = get_cat()
    e = discord.Embed(title = "Cats", description = fact, color = 0xf5f6fa)
    e.set_thumbnail(url="https://images.unsplash.com/photo-1611267254323-4db7b39c732c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8Y3V0ZSUyMGNhdHxlbnwwfHwwfHw%3D&w=250&q=80")
    await ctx.send(embed = e)
    
@client.command()
async def fox(ctx):
    fact = get_fox()
    e = discord.Embed(title = "Foxes", description = fact, color = 0xf5f6fa)
    e.set_thumbnail(url="https://images.pexels.com/photos/6889088/pexels-photo-6889088.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=250")
    await ctx.send(embed = e)
    
@client.command()
async def koala(ctx):
    fact = koala()
    e = discord.Embed(title = "Koalas", description = fact, color = 0xf5f6fa)
    e.set_thumbnail(url="https://www.zdnet.com/a/img/resize/df9890010cef92b486219d56748adb8c21c7d858/2021/09/27/55a1d73f-88c7-4551-a156-b49d7f5d0fde/koala-gettyimages-1271836615.jpg?width=1200&fit=bounds&auto=webp")
    await ctx.send(embed = e)

@client.command()
async def bird(ctx):
    fact = get_bird()
    e = discord.Embed(title = "Birds", description = fact, color = 0xf5f6fa)
    e.set_thumbnail(url="https://media.newyorker.com/photos/5a95a5b13d9089123c9fdb7e/2:2/w_3289,h_3289,c_limit/Petrusich-Dont-Mess-with-the-Birds.jpg")
    await ctx.send(embed = e)
    
@client.command()
async def whale(ctx):
    fact = get_whale()
    e = discord.Embed(title = "Whales", description = fact, color = 0xf5f6fa)
    e.set_thumbnail(url="https://th-thumbnailer.cdn-si-edu.com/pZSfv7nFe29y6pHteB-Wve1IzNo=/1000x750/filters:no_upscale():focal(715x531:716x532)/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer_public/76/01/7601fb67-87bf-4527-a325-ce824496df42/a_humpback_whale_breaches_the_surface_of_the_ocean_on_a_sunny_day.jpg")
    await ctx.send(embed = e)
    
# Administration and Moderation

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(embed=discord.Embed(title=f"***{member} has been banned from the server.***"))
    
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name,user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(embed=discord.Embed(description=f"***Unbanned {user.mention}.***"))
            return
    
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(embed=discord.Embed(description=f"***{member} has been kicked from the server.***"))

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
       await ctx.send(embed=discord.Embed(description="You do not have the permissions to use this command."))
       
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
       await ctx.send(embed=discord.Embed(description="You do not have the permissions to use this command."))
       
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
       await ctx.send(embed=discord.Embed(description="You do not have the permissions to use this command."))
       
       
@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(embed=discord.Embed(description=f"***{member.mention} has been muted.***"))
    
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
           await ctx.send(embed=discord.Embed(description="You do not have the permissions to use this command."))

@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(embed=discord.Embed(description=f"***{member.mention} has been unmuted.***"))

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
           await ctx.send(embed=discord.Embed(description="You do not have the permissions to use this command."))

# About the Bot
@client.command()
async def help(ctx):
    # e = discord.Embed(title="Moon Knight Commands", description=help_list, color = 0xf5f6fa)
    # await ctx.send(embed = e)

    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] # skip to start, left, right, skip to end
    current = 0
    msg = await ctx.send(embed=client.help_pages[current])
    
    for button in buttons:
        await msg.add_reaction(button)
        
    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)

        except asyncio.TimeoutError:
            return print("test")

        else:
            previous_page = current
            if reaction.emoji == u"\u23EA":
                current = 0
                
            elif reaction.emoji == u"\u2B05":
                if current > 0:
                    current -= 1
                    
            elif reaction.emoji == u"\u27A1":
                if current < len(client.help_pages)-1:
                    current += 1

            elif reaction.emoji == u"\u23E9":
                current = len(client.help_pages)-1

            for button in buttons:
                await msg.remove_reaction(button, ctx.author)

            if current != previous_page:
                await msg.edit(embed=client.help_pages[current])


@client.command()
async def dev(ctx):
    await ctx.send(embed=discord.Embed(description='I was developed by **Magnus Chase#9444**, the dark lord and the most powerful hardcore programmer known to mankind.', color = 0xf5f6fa))
    
@client.command()
async def link(ctx):
    e = discord.Embed(title="Advaith Joshi | Official",
                      url="https://linktr.ee/Advaith7Joshi",
                      description="Advaith Joshi | A Programmer, Game Developer, and a VFX Artist.", color = 0xf5f6fa)
    await ctx.send(embed=e)
    
@client.command()
async def about(ctx):
    await ctx.send(embed=discord.Embed(title = "Moon Knight#5827", description='I became **Moon Knight** to battle evil wherever I could find it. And I never had to look farther than the darkness inside my own heart.\n\nI am Moon Knight, and I serve none other than the lord of darkness, **Magnus Artemis Chase.**', color = 0xf5f6fa))
    



    
client.run("OTM0MzU4NjA0MzAyMTM1MzE3.Yeu7Qg.zVp-e6-QiSdYKqsXXQK8GH8Yk-Q")
