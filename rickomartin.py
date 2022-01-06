import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from pprint import pprint as pp

tg_bot_token = '5025665681:AAHWOwdkuTRVNYrorzm8pK9vJcaTvjHHW9U'

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


r = requests.get('https://rickandmortyapi.com/api/character')
data = r.json()
characters_raw = data['results']
characters = dict()

for values in characters_raw:
    characters[values['name']] = values


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("hello! enter character name")


@dp.message_handler()
async def get_info_about_character(message: types.Message):
    character = characters.get(message.text)
    if character is None:
        await message.reply("sorry not find")
    else:
        await message.reply(f"""
        name: {character['name']},
        species: {character['species']},
        gender: {character['gender']}
        """)

executor.start_polling(dp)