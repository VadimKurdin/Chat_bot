import discord
import random
from bot_logic import gen_pass

def tirlist(a1, a2, a3, a4, a5, a6):
    tirlist_={
    1: a1,
    2: a2,
    3: a3,
    4: a4,
    5: a5,
    6: a6
    }
    return tirlist_
tir_list_gold=tirlist('Харит', 'Клинт', 'Бруно', 'Беатрис', 'Броуди', 'Иксия')
tir_list_exp=tirlist('Чонг', 'Пакито', 'Арлот', 'Бенадетта', 'Теризла', 'Чу')
tir_list_mag=tirlist('Ксавьер', 'Харит', 'Новария', 'Валентина', 'Лилия', 'Фарамис')
tir_list_forest=tirlist('Нолан', 'Дариус', 'Мартис', 'Хелкарт', 'Пакито', 'Сабер')
tir_list_roum=tirlist('Матильда', 'Лолита', 'Минотавр', 'Хуфра', 'Тигран', 'Флорин')

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello') or message.content.startswith('$hi'):
        await message.channel.send("Ня! :)")
    elif message.content.startswith('$bye'):
        await message.channel.send("Ня... :(")
    elif message.content.startswith('$Что ты умеешь делать?') or message.content.startswith('$Что ты умеешь?'):
        await message.channel.send("Я умею писать Ня! И тир-листы по mlbb :3")
    elif message.content.startswith('Выведи тир лист по стрелкам') or message.content.startswith('Лист по стрелкам'):
        await message.channel.send(tir_list_gold)
    elif message.content.startswith('Выведи тир лист по бойцам') or message.content.startswith('Лист по бойцам'):
        await message.channel.send(tir_list_exp)
    elif message.content.startswith('Выведи тир лист по магам') or message.content.startswith('Лист по магам'):
        await message.channel.send(tir_list_mag)
    elif message.content.startswith('Выведи тир лист по лесникам') or message.content.startswith('Лист по лесникам'):
        await message.channel.send(tir_list_forest)
    elif message.content.startswith('Выведи тир лист по роумерам') or message.content.startswith('Лист по роумерам'):
        await message.channel.send(tir_list_roum)
    elif message.content.startswith('Ня') or message.content.startswith('Ня!') or message.content.startswith('ня') or message.content.startswith('ня!'):
        await message.channel.send('Ня! ;3')
    else:
        await message.channel.send("Ня?...")
