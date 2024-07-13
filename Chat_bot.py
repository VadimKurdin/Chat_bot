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

@bot.command()
async def encryption(ctx, word: str):
    cipher=encrypt_word(word)
    await ctx.send(cipher)
    return cipher

@bot.command()
async def decryption(ctx, word: str):
    cipher=decrypt_word(word)
    await ctx.send(cipher)
    return cipher

def encrypt_word(word):
    if len(word) < 2:
        return word

    encrypted_word = word[-2] + word[1:-2] + word[0] + word[-1]
    return encrypted_word

def decrypt_word(word):
    if len(word) < 2:
        return word
    elements=word
    decrypted_word = elements[-2] + elements[1:-2] + elements[0] + elements[-1]
    return decrypted_word

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
