from aiogram import Bot, Dispatcher, types
import asyncio
import os
from dotenv import load_dotenv, find_dotenv

# Загрузка переменных окружения
load_dotenv(find_dotenv())

# Получение токена бота из переменных окружения
TELEGRAM_TOKEN = os.getenv("Token_tg")

# Инициализация бота и диспетчера
bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.KeyboardButton(text="Открыть матрицу задач", web_app=types.WebAppInfo(url="https://taskmatrix.online/")))
    await message.answer("Матрица задач", reply_markup=markup)

async def main():
    # Запуск процесса поллинга (опроса серверов Telegram)
    await dp.start_polling()

# Запуск асинхронного цикла
if __name__ == '__main__':
    asyncio.run(main())
