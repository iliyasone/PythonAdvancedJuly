from __future__ import annotations

from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from keyboards_clicker import first_keyboard, second_keyboard


bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class States:
    CLICKER: str = 'CLICKER' 
    
async def edit_clicker_message(message: Message, state: FSMContext):
    clicks = (await state.get_data())['clicks']
    
    if clicks == 0:
        await message.edit_text('0\nСделай свой первый клик!',
                                reply_markup=first_keyboard)
        
    if clicks < 15:
        await message.edit_text(f'{clicks}',
                                reply_markup=first_keyboard)
    if clicks >= 15:
        await message.edit_text(f'{clicks}',
                                reply_markup=second_keyboard)

@dp.message_handler(commands=['start'])
async def process_start(message: Message, state: FSMContext):
    await message.answer("Добро пожаловать в кликер!")
    await state.set_state(States.CLICKER)
    await state.update_data(clicks=0)
    
    clicker_message = await message.answer('_')
    await edit_clicker_message(clicker_message, state)
    
    
@dp.callback_query_handler(lambda c: c.data == 'click', state=States.CLICKER)
async def process_click(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer('+1')
    clicks = (await state.get_data())['clicks']
    await state.update_data(clicks=clicks+1)
    await edit_clicker_message(message=callback_query.message, state=state)
    
    
@dp.callback_query_handler(lambda c: c.data == 'double-click', state=States.CLICKER)
async def process_double_click(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer('+2')
    clicks = (await state.get_data())['clicks']
    await state.update_data(clicks=clicks+2)
    await edit_clicker_message(message=callback_query.message, state=state)
    
    
    
@dp.callback_query_handler()
async def general_process(callback_query: types.CallbackQuery):
    await callback_query.answer('Что-то пошло не так')
    

@dp.message_handler()
async def general_process_messages(message: Message):
    await message.reply('Данный тип сообщений не поддерживается')

executor.start_polling(dp)