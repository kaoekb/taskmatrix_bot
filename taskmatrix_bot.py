from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor
from aiogram import executor
from aiogram.types.web_app_info import WebAppInfo
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TELEGRAM_TOKEN = os.getenv("Token_tg")

# @taskmatrix_bot.:
bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.KeyboardButton(text="Открыть квадрат", web_app=WebAppInfo(url="https://taskmatrix.online/")))
    await message.answer("Квадрат", reply_markup=markup)

executor.start_polling(dp)