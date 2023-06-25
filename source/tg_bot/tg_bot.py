import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import requests


bot = Bot(token='6168375175:AAF0MNk_KNWgKSavyud0s256PLH4fUFCHyU')
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    response = requests.get('http://127.0.0.1:8000/api_v1/card/list/')
    if response.status_code == 200:
        cards = response.json()
        if cards:
            card = cards[-1]
            if message.from_user.username == card['username']:
                greeting = f"Привет, {card['name']} из города {card['city']}!"
                await message.answer(greeting)
            else:
                await message.answer("Привет!, зарегистрируй свою карточку приветствия")
        else:
            await message.answer("Привет!")
    else:
        await message.answer("Ошибка при получении карточки")


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)
