from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import asyncio
import os
from dotenv import load_dotenv, find_dotenv

# Загрузка переменных окружения
load_dotenv(find_dotenv())

# Получение токена бота из переменных окружения
TELEGRAM_TOKEN = os.getenv("Token_tg")

# Инициализация диспетчера
dp = Dispatcher()

# Добавление логирования (по желанию)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.KeyboardButton(text="Открыть матрицу задач", web_app=types.WebAppInfo(url="https://taskmatrix.online/")))
    await message.answer("Матрица задач", reply_markup=markup)

async def main():
    # Инициализация и регистрация бота в диспетчере
    async with Bot(TELEGRAM_TOKEN) as bot:
        dp.set_bot(bot)
        await dp.start_polling()

# Запуск асинхронного цикла
if __name__ == '__main__':
    asyncio.run(main())
