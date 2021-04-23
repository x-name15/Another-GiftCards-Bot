#-------------Imports y Froms----------------
import discord, json
import random, string, os, colorama, sys
import time, datetime, asyncio, requests
from os import system, name
from discord import Embed, File
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands.cooldowns import BucketType
from console.utils import set_title
from colorama import Fore
from colorama import init
init()
#-------------Imports y Froms----------------
#-----------------Titulo y el Input osusaasdsadada------------------
version = "ULTIMATE"
set_title(f'GC Generator Bot {version} by Chirimoya | Enjoy the Tool')
input(f"Hey welcome to the tool\nThis tool is for{Fore.RED} educational purposes{Fore.RESET}\nI will not be responsible for the misuse of the program\n{Fore.RED}Most of the codes will not work because they are random and string functions{Fore.RESET}, so good luck with that :D\nWith that said, hit {Fore.YELLOW}ENTER{Fore.RESET} to continue")
print(Fore.BLUE + """
 _____  _____   _____                           _              ______       _   
|  __ \/  __ \ |  __ \                         | |             | ___ \     | |  
| |  \/| /  \/ | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __  | |_/ / ___ | |_ 
| | __ | |     | | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__| | ___ \/ _ \| __|
| |_\ \| \__/\ | |_\ \  __/ | | |  __/ | | (_| | || (_) | |    | |_/ / (_) | |_ 
 \____/ \____/  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|    \____/ \___/ \__|                                                                                                                                                                
""" + Fore.RESET)
#-----------------Titulo y el Input osusaasdsadada------------------
#-----Config Data----------------------------------------
with open('config.json') as f:
	config = json.load(f)
token = config.get('token')
prefix = config.get("prefix")
game = config.get("RPC")
rate = config.get("rate")
per = config.get("per")
t = BucketType.default
anouncement = requests.get('https://pastebin.com/raw/jeqPhRxu')
#-----Config Data----------------------------------------
client = commands.Bot(command_prefix=prefix)
client.remove_command('help')
print(f"{Fore.MAGENTA}Message of the day, by Chirimoya: {anouncement.text}{Fore.RESET}")
#-----------------------------------------Eventos de la GiftCards osiosi----------------------------------------------------------------------------
def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def NitroBox():
    code1 = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
    return f'https://discord.com/billing/promotions/xbox-game-pass/redeem/{code1}'

def Nike():
  code2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
  return f'Nike Code: {code2}'

def Netflix():
  code3 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
  return f'Netflix Code: {code3}'

def Spotify():
  code4 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=19))
  return f'Spotify Code: {code4}'

def Blizzard():
    code5 = ('').join(random.choices(string.ascii_uppercase + string.digits, k=20))
    return f'Blizzard Code: {code5}'

def Robux():
    code6 = ('').join(random.choices(string.digits, k=10))
    return f"Robux Code: {code6}"

def MCWin10():
    Mcode = ('').join(random.choices(string.ascii_uppercase + string.digits, k=25))
    return f"Minecraft Win 10 Key: {Mcode}"

def MCCode():
    randomnumber1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber3 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    generatedMinecraftcode = randomnumber1 + "-" + randomnumber2 + "-" + randomnumber3 
    return f"Minecraft Code: {generatedMinecraftcode}"

def Vbucks():
    randomnumber1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
    randomnumber2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
    randomnumber3 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
    randomnumber4 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
    generatedVbucks = randomnumber1 + "-" + randomnumber2 + "-" + randomnumber3 + "-" + randomnumber4
    return f"V-bucks Fornite Code: {generatedVbucks}"

def DiscordToken():
    firstGen = random.choice(string.ascii_letters).upper() + random.choice(string.ascii_letters).upper()+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+ random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    return f"Discord Token: {firstGen}"

def Uplay():
    randomnumber1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber3 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber4 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    generatedUplay = randomnumber1 + "-" + randomnumber2 + "-" + randomnumber3 + "-" + randomnumber4
    return f"Uplay Key: {generatedUplay}"

def MalwareBytes():
    randomnumber1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
    randomnumber2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber3 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber4 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber5 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    generatedMal = randomnumber1 + ":" + randomnumber2 + "-" + randomnumber3 + "-" + randomnumber4 + "-" + randomnumber5
    return f"MalwareBytes Key: {generatedMal}"

def Avast():
    randomnumber1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6))
    randomnumber2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6))
    randomnumber3 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6))
    generatedAvast = randomnumber1 + "-" + randomnumber2 + "-" + randomnumber3
    return f"Avast Key: {generatedAvast}"

def ExpressVPN():
    EVPNCode = ''.join(random.choices(string.ascii_uppercase + string.digits, k=23))
    return f"Express VPN Code: {EVPNCode}"

def HMA():
    randomnumber1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6))
    randomnumber2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6))
    randomnumber3 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6))
    generatedHMA = randomnumber1 + "-" + randomnumber2 + "-" + randomnumber3
    return f"HMA Key: {generatedHMA}"

def ZALTV():
    ZALCode = ''.join(random.choices(string.digits, k=10))
    return f"ZalTV Code: {ZALCode}"

def Paysafecard():
    randomnumber1 = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    randomnumber2 = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    randomnumber3 = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    randomnumber4 = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    generatedcodePaysafe = randomnumber1 + '-' + randomnumber2 + '-' + randomnumber3 + '-' + randomnumber4
    return f"Paysafe Code: {generatedcodePaysafe}"

def Steam():
    randomnumber1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
    randomnumber2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
    randomnumber3 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
    generatedcodeSteam = randomnumber1 + '-' + randomnumber2 + '-' + randomnumber3
    return f"Steam Key: {generatedcodeSteam}"

def Amazon():
    randomnumber1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6))
    randomnumber3 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    generatedcodeAmazon = randomnumber1 + '-' + randomnumber2 + '-' + randomnumber3
    return f"Amazon Code: {generatedcodeAmazon}"

def Xbox():
    randomnumber1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
    randomnumber2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
    randomnumber3 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
    randomnumber4 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
    randomnumber5 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
    generatedcodeXbox = randomnumber1 + '-' + randomnumber2 + '-' + randomnumber3 + '-' + randomnumber4 + '-' + randomnumber5
    return f"Xbox Code: {generatedcodeXbox}"

def Itunes():
    randomnumber1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(16))
    generatedcodeItunes = randomnumber1
    return f"Itunes Code: {generatedcodeItunes}"

def Playstore():
    randomnumber1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber3 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber4 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber5 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    generatedcodePlaystore = randomnumber1 + '-' + randomnumber2 + '-' + randomnumber3 + '-' + randomnumber4 + '-' + randomnumber5
    return f"Playstore Code: {generatedcodePlaystore}"

def Playstation():
    randomnumber1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber3 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    generatedcodePSN = randomnumber1 + '-' + randomnumber2 + '-' + randomnumber3
    return f"PSN Code: {generatedcodePSN}"

def Paypal():
    randomnumber1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber3 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    generatedcodePaypal = randomnumber1 + "-" + randomnumber2 + "-" + randomnumber3
    return f"Paypal Code: {generatedcodePaypal}"

def Nintendo():
    randomnumber1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber3 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber4 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    generatedcodeNintendo = randomnumber1 + "-" + randomnumber2 + "-" + randomnumber3 + "-" + randomnumber4
    return f"Nintendo E-Shop Code: {generatedcodeNintendo}"

def ProxyScrape():
    randomnumber1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
    randomnumber2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
    randomnumber3 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
    randomnumber4 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
    generatedcodeProxyScrape = randomnumber1 + "-" + randomnumber2 + "-" + randomnumber3 + "-" + randomnumber4
    return f"ProxyScrape Key: {generatedcodeProxyScrape}"

def Webkinz():
    WCode = ('').join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return f"WebKinz Code: {WCode}"

def IMVU():
    IMCode = ('').join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return f"IMVU Code: {IMCode}"

def PokemonTGC():
    randomnumber1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(3))
    randomnumber2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
    randomnumber3 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(3))
    randomnumber4 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(3))
    generatedcodePokemon = randomnumber1 + "-" + randomnumber2 + "-" + randomnumber3 + "-" + randomnumber4
    return f"Pokemon TGC Code: {generatedcodePokemon}"
#-----------------------------------------Fin de Eventos de la GiftCards osiosi-------------------------------------------------------------------
#-----------Inicio------------
@client.event
async def on_ready():
    print(f"{Fore.GREEN}The bot is online!{Fore.RESET}")
    print("------------------------------")
    print(f"Logued in: {Fore.RED}{client.user.name}{Fore.RESET}")
    print(f'ID of the Bot: {Fore.RED}{client.user.id}{Fore.RESET}')
    print(f"Version of {Fore.BLUE}Discord{Fore.RESET}: {discord.__version__}")
    print(f"Version of the Bot: {Fore.LIGHTMAGENTA_EX}{version}{Fore.RESET}")
    print("-------------------------------")
    print(f"{Fore.MAGENTA}--Commands Loggers--{Fore.RESET}")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(game))
#-----------Inicio------------
#----------------Eventos-------------------------------
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(title='Cooldown',description=f'{error}'))
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"{ctx.message.author.mention} Are u sure do u type correctly the command?")

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def nitro(ctx):
  print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.BLUE}Nitro Code{Fore.RESET} in time {datetime.datetime.now()}!")
  await ctx.author.send(Nitro())
  embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x0b81da)
  embed.set_thumbnail(url="https://i.imgur.com/RY5oA8m.gif")
  embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=True)
  embed.set_footer(text="GC Generator Bot Tool")
  await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def nitrobox(ctx):
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.CYAN}Xbox Nitro Code{Fore.RESET} in time {datetime.datetime.now()}!")
    await ctx.author.send(NitroBox())
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x0b81da)
    embed.set_thumbnail(url="https://bot.to/wp-content/uploads/2020/09/animated-emojis_5f702f96b0333.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=True)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def nike(ctx):
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.WHITE}Nike Code{Fore.RESET} in time {datetime.datetime.now()}!")
    await ctx.author.send(Nike())
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x545a63)
    embed.set_thumbnail(url="https://prod.media.libero.pe/1200x660/libero/imagen/2018/11/06/noticia-1541520430-nike-logo-clasico.jpg")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=True)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def netflix(ctx):
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.RED}Netflix Code{Fore.RESET} in time {datetime.datetime.now()}!")
    await ctx.author.send(Netflix())
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0xb90404)
    embed.set_thumbnail(url="https://i.imgur.com/3qKDpcJ.gif")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def spotify(ctx):
    await ctx.author.send(Spotify())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.GREEN}Spotify Code{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x08e20f)
    embed.set_thumbnail(url="https://i.imgur.com/RL8Y2R8.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def blizzard(ctx):
    await ctx.author.send(Blizzard())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.CYAN}Blizzard Code{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x0c08e2)
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_image(url="https://i.imgur.com/lJ91mya.png")
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def robux(ctx):
    await ctx.author.send(Robux())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.GREEN}Roblox Robux Code{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x07f262)
    embed.set_thumbnail(url="https://i.imgur.com/pGl4Zgl.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def mcwin10(ctx):
    await ctx.author.send(MCWin10())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.GREEN}MC Win 10 Key {Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x07f262)
    embed.set_thumbnail(url="https://cdn.icon-icons.com/icons2/2699/PNG/512/minecraft_logo_icon_168974.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command(name="mckey")
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def mckey(ctx):
    await ctx.author.send(MCCode())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.GREEN}Minecraft Code {Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x07f262)
    embed.set_thumbnail(url="https://cdn.icon-icons.com/icons2/2699/PNG/512/minecraft_logo_icon_168974.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def dstoken(ctx):
    await ctx.author.send(DiscordToken())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.BLUE}Discord Token{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur token in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x2d47c8)
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Font_Awesome_5_brands_discord_color.svg/1200px-Font_Awesome_5_brands_discord_color.svg.png")
    embed.add_field(name="I send u the token in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def vbucks(ctx):
    await ctx.author.send(Vbucks())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.MAGENTA}V-Bucks Fortnite Code{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x2dc894)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/774657503538446357/778515244661997598/5bd9f4860591f23a4b521857.jpg")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def uplay(ctx):
    await ctx.author.send(Uplay())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.CYAN}Uplay Key{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x3378a3)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/589565983467765820/827937520708222986/Uplay_logo-bw.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def malwarebytes(ctx):
    await ctx.author.send(MalwareBytes())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.CYAN}MalwareBytes Key{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x3378a3)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/589565983467765820/827939544527536229/descarga_1.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def avast(ctx):
    await ctx.author.send(Avast())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.YELLOW}Avast AntiVirus Key{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0xf0e800)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/589565983467765820/827940910791655434/descarga_2.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def exvpn(ctx):
    await ctx.author.send(ExpressVPN())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.RED}Express VPN Code{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0xf02400)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/782292942067990569/827942693103468555/ExpressVPN-logo.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def hma(ctx):
    await ctx.author.send(HMA())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.CYAN}Hide My Ass Key{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x218cb0)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/782292942067990569/827943564423987220/HideMyAss_Logo.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def zaltv(ctx):
    await ctx.author.send(ZALTV())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.MAGENTA}ZalTV Code{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x000000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/782292942067990569/827945727833538580/descarga.jpg")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def paysafe(ctx):
    await ctx.author.send(Paysafecard())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.CYAN}PaySafe Code{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x3f87d5)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/782292942067990569/827946982634422282/descarga_3.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def steamkey(ctx):
    await ctx.author.send(Steam())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.MAGENTA}Steam Key{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x666061)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/782292942067990569/827948563689635870/descarga_4.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def amazon(ctx):
    await ctx.author.send(Amazon())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.GREEN}Amazon GiftCard Code{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x685a5f)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/782292942067990569/827957897643294720/descarga_5.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def xbox(ctx):
    await ctx.author.send(Xbox())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.GREEN}Xbox GiftCard Code{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x0de76c)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/782292942067990569/827958329841025036/1200px-Xbox_one_logo.svg.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def itunes(ctx):
    await ctx.author.send(Itunes())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.RED}Itunes GiftCard Code{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0xcd55dd)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/782292942067990569/827959207248527441/descarga_1.jpg")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def playstore(ctx):
    await ctx.author.send(Playstore())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.GREEN}PlayStore GiftCard Code{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x4abaa4)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/782292942067990569/827960195850043503/cc49e0969fbc128b3c055440483f83a4.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def psn(ctx):
    await ctx.author.send(Playstation())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.BLUE}PSN GiftCard Code{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x0040ff)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/782292942067990569/827960729587679283/Psn-logo.jpg")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def paypal(ctx):
    await ctx.author.send(Paypal())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.BLUE}PayPal GiftCard Code{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x5777d6)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/782292942067990569/827961287308345414/descarga_6.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def nintendo(ctx):
    await ctx.author.send(Nintendo())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.RED}Nintendo GiftCard Code{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0xd91717)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/774657503538446357/778515402497982484/240px-Nintendo_switch_logo.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def proxyscrape(ctx):
    await ctx.author.send(ProxyScrape())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.BLUE}ProxyScrape Premiun Key{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0x1751d9)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/782292942067990569/827962526704468048/descarga_7.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def webkinz(ctx):
    await ctx.author.send(Webkinz())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.MAGENTA}Webkinz Code{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0xc03092)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/782292942067990569/828282417676419092/webkinz-logo.jpg")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def imvu(ctx):
    await ctx.author.send(IMVU())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.YELLOW}IMVU Code{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0xe43aae)
    embed.set_thumbnail(url="https://www.mmaglobal.com/files/logos/social_network_imvu_and_artcenter-c39990a5985e7d402119e01c2bcf828b.jpg")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def pkmtcg(ctx):
    await ctx.author.send(PokemonTGC())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.RED}Pokemon TCG Code{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey ur code in the DMs!", url="https://cracked.to/Chirimoya", description="Thank for using the bot", color=0xd0013f)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/589565983467765820/828292502683516968/descarga_1.png")
    embed.add_field(name="I send u the code in DM", value="Pls go to check it!", inline=False)
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def cleancmd(ctx):
    os.system('cls')
    print(f"{Fore.RED}I cleaned all the cmd{Fore.RESET}")
    await ctx.send("Successfully")

@client.command()
@commands.is_owner()
async def gcdrop(ctx):
    await ctx.message.delete()
    print(f"A {Fore.RED}drop of GiftCards{Fore.RESET} is being executed :D")
    await ctx.send(Nitro())
    print(f"> Nitro Code Sended")
    await ctx.send(NitroBox())
    print(f"> Xbox Nitro Code Sended")
    await ctx.send(Steam())
    print(f"> Steam Key Sended")
    await ctx.send(Playstation())
    print(f"> PSN Code Sended")
    await ctx.send(Xbox())
    print(f"> Xbox Code Sended")
    await ctx.send(Nintendo())
    print(f"> Nintendo E-Shop Code Sended")
    await ctx.send(ProxyScrape())
    print(f"> ProxyScrape Premiun Key Sended")
    await ctx.send(Playstore())
    print(f"> Playstore Code Sended")
    await ctx.send(Itunes())
    print(f"> Itunes Code Sended")
    await ctx.send(Amazon())
    print(f"> Amazon Code Sended")
    await ctx.send(Paysafecard())
    print(f"> Paysafe Card Code Sended")
    await ctx.send(Blizzard())
    print(f"> Blizzard Code Sended")
    await ctx.send(Spotify())
    print(f"> Spotify Code Sended")
    await ctx.send(Netflix())
    print(f"> Netflix Code Sended")
    await ctx.send(Nike())
    print(f"> Nike Code Sended")
    await ctx.send(Robux())
    print(f"> Robux Code Sended")
    await ctx.send(MCWin10())
    print(f"> Minecraft Win 10 Key Code Sended")
    await ctx.send(MCCode())
    print(f"> Minecraft Code Sended")
    await ctx.send(DiscordToken())
    print(f"> Discord Token Code Sended")
    await ctx.send(Uplay())
    print(f"> Uplay Key Sended")
    await ctx.send(MalwareBytes())
    print(f"> MalwareBytes Key Sended")
    await ctx.send(Avast())
    print(f"> Avast Code Sended")
    await ctx.send(ExpressVPN())
    print(f"> Express VPN Code Sended")
    await ctx.send(HMA())
    print(f"> Hide My Ass Code Sended")
    await ctx.send(ZALTV())
    print(f"> ZalTV Code Sended")
    await ctx.send(Paypal())
    print(f"> Paypal Code Sended")
    await ctx.send(Webkinz())
    print(f"> Webkinz Code Sended")
    await ctx.send(IMVU())
    print(f"> IMVU Code Sended")
    await ctx.send(PokemonTGC())
    print(f"> Pokemon TCG Code Sended")
    print(f"-{Fore.RED}ALL THE GIFTCARDS HAS BEEN SENDED TO THE GUILD IN TIME: {datetime.datetime.now()}{Fore.RESET}-")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, reason=None):
    if reason == None:
        await ctx.send(f"Woah {ctx.author.mention}, Make sure you provide a reason!")
    else:
        messageok = f"You have been banned from {ctx.guild.name} for {reason}"
        await member.send(messageok)
        await member.ban(reason=reason)

@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.command(pass_context=True)
async def clean(ctx):
    if ctx.author.guild_permissions.administrator:
            llimit = ctx.message.content[10:].strip()
            await ctx.channel.purge(limit=int(llimit))
            await ctx.send('Cleared by <@{.author.id}>'.format(ctx))
            await ctx.message.delete()
    else:
        await ctx.send("You cant do that!")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has kicked.')

@client.command()
@commands.has_permissions(administrator = True)
async def nuke(ctx, channel: discord.TextChannel = None):
    if channel == None: 
        await ctx.send("You did not mention a channel!")
        return
    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)
    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="Has been Nuked!")
        await nuke_channel.delete()
        await new_channel.send("THIS CHANNEL HAS BEEN NUKED!")
        await ctx.send("Nuked the Channel sucessfully!\nhttps://tenor.com/view/saussi%C3%A7on-explode-boom-gif-16089684")
    else:
        await ctx.send(f"No channel named {channel.name} was found!")

@client.command()
async def info(ctx):
    embed=discord.Embed(title="Info", url="https://cracked.to/Chirimoya", description="Thank for using the bot\nTotally free tool in c.to for the discord community", color=0xa18c8c)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/782292942067990569/828297174961225728/gift-card.png")
    embed.set_image(url="https://cdn.discordapp.com/attachments/782292942067990569/828297834674782228/397ce7ff2fc83a09a8ec26e2a9fd0c3b.jpg")
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    await ctx.send("Help")
    await ctx.send(file=File("Commands.txt"))

@client.command()
async def http(ctx):
    f = open("Proxies/http-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&amp;protocol=http&amp;timeout=10000&amp')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Proxies/http-proxies.txt"))
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has scrapped some {Fore.CYAN}HTTP Proxies{Fore.RESET} in time {datetime.datetime.now()}!")

@client.command()
async def socks4(ctx):
    f = open("Proxies/socks4-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&amp;protocol=socks4&amp;timeout=10000&amp')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Proxies/socks4-proxies.txt"))
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has scraped some {Fore.GREEN}Socks4 Proxies{Fore.RESET} in time {datetime.datetime.now()}!")

@client.command()
async def socks5(ctx):
    f = open("Proxies/socks5-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&amp;protocol=socks5&amp;timeout=10000&amp')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Proxies/socks5-proxies.txt"))
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has scraped some {Fore.YELLOW}Socks5 Proxies{Fore.RESET} in time {datetime.datetime.now()}!")

client.run(token)