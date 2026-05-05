import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random

import webserver

load_dotenv()

token = os.environ['DISCORD_TOKEN']

##test
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as Bot, {bot.user.name}')


@bot.event
async def on_member_join(member):
    await member.send(f"Welcome {member.name}!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "helia" in message.content.lower():
        await message.channel.send(f"{message.author.mention} !!!!!")
    await bot.process_commands(message)



#@bot.command()
#async def fdd_create_list(ctx,msg):
#    f = open(f"{msg}.json", "x")


@bot.command()
async def fdd_add(ctx,msg):
    with open(f"fdd.txt", "a") as f:
        x = f"{msg}\n"
        f.write(x)
        await ctx.send(f"{msg} ajouté")


@bot.command()
async def fdd_help(ctx):
    await ctx.send(
        f"Pour les roll ! :\n1er roll:\n25 ou moins = fruit du démon\n2ème roll :\n95 ou plus = Logia\n70 ou plus = Zoan\nen dessous de 70 = Paramecia")

@bot.command()
async def fdd_random(ctx):


    randomFDD = random.randint(1,100)
    if randomFDD <= 25:
        await ctx.send(f"tu as un fruit du démon !!!!! :0 (roll : {randomFDD})")

        randomFDD = random.randint(1,100)
        if randomFDD >= 95:
            await ctx.send(f"tu as un Logia !!!!!!!!! :0 :0 :0 GG (roll : {randomFDD})")
        elif randomFDD >= 70 :
            await ctx.send(f"tu as un Zoan !!!! (roll : {randomFDD})")
        elif randomFDD < 70  :
            await ctx.send(f"tu as un Paramecia ({randomFDD})")
            with open("fdd.txt", "r") as y:
                contents = y.readlines()
                chosen = random.randint(0 , len(contents))



            await ctx.send(f"tu as eu{contents[chosen]}")

            with open("fdd.txt", "w") as i:
                del contents[chosen]
                i.write("")
            with open("fdd.txt", "a") as i:
                for line in contents:
                    i.write(line)
        else:
            await ctx.send(f"t'as rien... dommage....({randomFDD})")




@bot.command()
async def fdd_paramecia_test(ctx):
    await ctx.send(f"tu as un Paramecia")
    with open("fdd.txt", "r") as y:
        contents = y.readlines()
        chosen = random.randint(0, len(contents))

        await ctx.send(f"tu as eu {contents[chosen]}")

    with open("fdd.txt", "w") as i:
        del contents[chosen]
        i.write("")
    with open("fdd.txt", "a") as i:
        for line in contents:
            i.write(line)

@bot.command()
async def fdd_list(ctx):
    with open("fdd.txt", "r") as y:
        for line in y.readlines():
            await ctx.send(f"{line}")


# fdd 25% de chance d'avoir
# fdd si oui -> quel genre de fruit
# soit zoan 25%, logia 5%, Paramecia 70%
# zoan -> classique 60%, préhistorique 35%, mythique 5%
# Paramecia aléatoire dans la liste -> enlever automatiquement


webserver.keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)