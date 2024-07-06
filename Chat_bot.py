import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='@', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def parol(ctx, left: int):
    elements = "+-/*!&$#?=@<>"
    password_ = ""
    for i in range(left):
        password_ += random.choice(elements)
    
    await ctx.send(password_)
    return password_
    
