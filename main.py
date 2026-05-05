import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import json
import os
import webbrowser

import webserver

load_dotenv()

token = os.getenv("DISCORD_TOKEN")

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



@bot.command()
async def fdd_create_list(ctx,msg):
    f = open(f"{msg}.json", "x")


@bot.command()
async def fdd_add_list(ctx,msg):
    with open(f"fdd.json", "w") as f:
        x = [f"{msg}"]
        json.dump({"FDD" : x}, f)

@bot.command()
async def fdd_random(ctx):
    y = json.loads(open(f"fdd.json", "r").read())
    await ctx.send(y)






# fdd 25% de chance d'avoir
# fdd si oui -> quel genre de fruit
# soit zoan 25%, logia 5%, Paramecia 70%
# zoan -> classique 60%, préhistorique 35%, mythique 5%
# aléatoire dans la liste -> enlever automatiquement


webserver.keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)