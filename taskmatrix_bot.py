from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
import asyncio
import os
from dotenv import load_dotenv, find_dotenv

# Загрузка переменных окружения
load_dotenv(find_dotenv())

# Получение токена бота из переменных окружения
TELEGRAM_TOKEN = os.getenv("Token_tg")

async def start(message: Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.KeyboardButton(text="Открыть матрицу задач", web_app=types.WebAppInfo(url="https://taskmatrix.online/")))
    await message.answer("Матрица задач", reply_markup=markup)

async def main():
    # Инициализация бота
    bot = Bot(TELEGRAM_TOKEN)

    # Инициализация диспетчера
    dp = Dispatcher()

    # Регистрация обработчика команды /start
    dp.message.register(start, commands=['start'])

    # Запуск поллинга
    await dp.start_polling()

# Запуск асинхронного цикла
if __name__ == '__main__':
    asyncio.run(main())
