from config import TOKEN

from aiogram import Bot, Dispatcher, executor, types

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: types.Message, state: FSMContext):
    """Ловец start сообщения"""
    await message.answer("Добро пожаловать в групповой анонимный чат. Напиши своё имя")
    await state.set_state("name")


@dp.message_handler(state='name')
async def name_asking(message: types.Message, state: FSMContext):
    name = message.text
    state.update_data({"name" : name})
    await message.reply(f"Приятно познакомиться, {name}. Ты теперь в чате!")
    await state.set_state("g_chatting")


@dp.message_handler(state='g_chatting')
async def echo_handler(message: types.Message):
    """Эхо-ловец"""
    await message.answer(message.text)

executor.start_polling(dp,  skip_updates=True)