#Imports
import discord
from discord.ext import commands
import random
import time

#Test discord token
#DiscordToken = 'ODAwODExNjI4Mjg2MTgxMzg3.YAXj8g.1mXxSA9iUI5_NDukWjEmRcJezKU'
#FU discord token
DiscordToken = 'ODAwNzA1OTc5ODY3ODU2OTE2.YAWBjQ.D2w0jkUp686bqlU_Jzi9BkEH_A8'

#Define bot client, prefix and remove help command
global bot
bot = commands.Bot(command_prefix="-", help_command=None)

#Test channel
#bot_channel = bot.get_channel(800728465502502972)
#FU channel
bot_channel = bot.get_channel(798289725391634443)

#Test channel name
#botchannelname = "bot-channel"
#FU channel name
botchannelname = "🤖bot-channel"

#Test error
#channelerrormessage = "Please use <#800728465502502972>"
#FU Error
channelerrormessage = 'Please use <#798289725391634443>'

#Define return when command is not recognized
@bot.event
async def on_command_error(erreur, error):
    if erreur.channel.name == botchannelname:
        if isinstance(error, commands.CommandNotFound):
            await erreur.send("```The command you entered was not recognized, try -help for the available commands```")
    else:
        await erreur.send(channelerrormessage)

#Define the new help command
@bot.command()
async def help(help):
    if help.channel.name == botchannelname:
        await help.send('```Shortcuts for cash stack item ideas:\n'
        '-10m   -50m    -100m   -200m   -500m\n\n'        
        'Shortcut for 8 random high volume overnight ideas:\n'
        '-overnights\n\n'
        'Shortcuts for items available:\n'
        '-tbow       -ely        -scy\n\n'
        'Shortcuts to combined lists available:\n'
        '-inq        -anc        -jus\n'
        '-orbs       -tob        -bond```')
    else:
        await help.send(channelerrormessage)

#Twisted bow
@bot.command()
async def tbow(tbow):
    if tbow.channel.name == botchannelname:
        await tbow.send('!graph tbow', delete_after=0)
        time.sleep(1)
        await tbow.send('!price tbow', delete_after=0)
    else:
        await tbow.send(channelerrormessage)

#Elysian
@bot.command()
async def ely(ely):
    if ely.channel.name == botchannelname:
        await ely.send('!graph ely', delete_after=0)
        time.sleep(1)
        await ely.send('!price ely', delete_after=0)
    else:
        await ely.send(channelerrormessage)

#Scythe
@bot.command()
async def scy(scy):
    if scy.channel.name == botchannelname:
        await scy.send('!graph scy', delete_after=0)
        time.sleep(1)
        await scy.send('!price scy', delete_after=0)
    else:
        await scy.send(channelerrormessage)

#Inquisitor
@bot.command()
async def inq(inq):
    if inq.channel.name == botchannelname:
        await inq.send('!graph inq great', delete_after=0)
        time.sleep(1)
        await inq.send('!price inq great', delete_after=0)
        time.sleep(1)
        await inq.send('!graph inq haub', delete_after=0)
        time.sleep(1)
        await inq.send('!price inq haub', delete_after=0)
        time.sleep(1)
        await inq.send('!graph inq plate', delete_after=0)
        time.sleep(2)
        await inq.send('!price inq plate', delete_after=0)
        time.sleep(2)
        await inq.send('!graph inq mace', delete_after=0)
        time.sleep(2)
        await inq.send('!price inq mace', delete_after=0)
    else:
        await inq.send(channelerrormessage)
#orbs
@bot.command()
async def orbs(orbs):
    if orbs.channel.name == botchannelname:
        await orbs.send('!graph eldritch', delete_after=0)
        time.sleep(1)
        await orbs.send('!price eldritch', delete_after=0)
        time.sleep(1)
        await orbs.send('!graph volatile', delete_after=0)
        time.sleep(1)
        await orbs.send('!price volatile', delete_after=0)
        time.sleep(1)
        await orbs.send('!graph harmonised', delete_after=0)
        time.sleep(2)
        await orbs.send('!price harmonised', delete_after=0)
    else:
        await orbs.send(channelerrormessage)

#Theater of blood
@bot.command()
async def tob(tob):
    if tob.channel.name == botchannelname:
        await tob.send('!graph rapier', delete_after=0)
        time.sleep(1)
        await tob.send('!price rapier', delete_after=0)
        time.sleep(1)
        await tob.send('!graph sang', delete_after=0)
        time.sleep(1)
        await tob.send('!price sang', delete_after=0)
        time.sleep(1)
        await tob.send('!graph avernic', delete_after=0)
        time.sleep(2)
        await tob.send('!price avernic', delete_after=0)
    else:
        await tob.send(channelerrormessage)

#Ancestral
@bot.command()
async def anc(anc):
    if anc.channel.name == botchannelname:
        await anc.send('!graph ancestral hat', delete_after=0)
        time.sleep(1)
        await anc.send('!price ancestral hat', delete_after=0)
        time.sleep(1)
        await anc.send('!graph ancestral top', delete_after=0)
        time.sleep(1)
        await anc.send('!price ancestral top', delete_after=0)
        time.sleep(1)
        await anc.send('!graph ancestral bottom', delete_after=0)
        time.sleep(2)
        await anc.send('!price ancestral bottom', delete_after=0)
    else:
        await anc.send(channelerrormessage)

#Justiciar
@bot.command()
async def jus(jus):
    if jus.channel.name == botchannelname:
        await jus.send('!graph justiciar faceguard', delete_after=0)
        time.sleep(1)
        await jus.send('!price justiciar faceguard', delete_after=0)
        time.sleep(1)
        await jus.send('!graph justiciar chestguard', delete_after=0)
        time.sleep(1)
        await jus.send('!price justiciar chestguard', delete_after=0)
        time.sleep(1)
        await jus.send('!graph justiciar legguards', delete_after=0)
        time.sleep(2)
        await jus.send('!price justiciar legguards', delete_after=0)
    else:
        await jus.send(channelerrormessage)

#Bond
@bot.command()
async def bond(bond):
    if bond.channel.name == botchannelname:
        await bond.send('!graph old school bond', delete_after=0)
        time.sleep(1)
        await bond.send('!price old school bond', delete_after=0)
    else:
        await bond.send(channelerrormessage)

#Grab 8 random overnights
@bot.command()
async def overnights(overnights):
    if overnights.channel.name == botchannelname:
        randomfile = open("randoms.txt", "rt")
        randomlist = random.sample(randomfile.readlines(), 8)
        randomlistclean = ''.join(randomlist)
        print (randomlistclean)
        await overnights.send('```' + randomlistclean + '```')
        randomfile.close()
    else:
        await overnights.send(channelerrormessage)

#-10m
tenfile = open("ten.txt", "rt")
tenlist = tenfile.readlines()
tenlistclean = ''.join(tenlist)

#-50m
fiftyfile = open("fifty.txt", "rt")
fiftylist = fiftyfile.readlines()
fiftylistclean = ''.join(fiftylist)

#-100m
onehundredfile = open("onehundred.txt", "rt")
onehundredlist = onehundredfile.readlines()
onehundredlistclean = ''.join(onehundredlist)

#-200m
twohundredfile = open("twohundred.txt", "rt")
twohundredlist = twohundredfile.readlines()
twohundredlistclean = ''.join(twohundredlist)

#-500m
fivehundredfile = open("fivehundred.txt", "rt")
fivehundredlist = fivehundredfile.readlines()
fivehundredlistclean = ''.join(fivehundredlist)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="#bot-channel | -help"))

@bot.event
async def on_message(message):
    if message.content == '-10m':
        await message.channel.send(tenlistclean)
    elif message.content == '-50m':
        await message.channel.send(fiftylistclean)
    elif message.content == '-100m':
        await message.channel.send(onehundredlistclean)
    elif message.content == '-200m':
        await message.channel.send(twohundredlistclean)
    elif message.content == '-500m':
        await message.channel.send(fivehundredlistclean)
    else:
        await bot.process_commands(message)
    

bot.run(DiscordToken)