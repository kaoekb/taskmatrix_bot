
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
# from aiogram import executor
from aiogram.types.web_app_info import WebAppInfo
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

bot = Bot(Token_tg)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.KeyboardButton(text="Открыть матрицу задач", web_app=WebAppInfo(url="https://taskmatrix.online/")))
    await message.answer("Матрица задач", reply_markup=markup)

executor.start_polling(dp)