from config import TOKEN

from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    """Ловец (обработчик сообщений)"""
    await message.answer("Добро пожаловать в тестового эхо бота!")
    
executor.start_polling(dp,  skip_updates=True)