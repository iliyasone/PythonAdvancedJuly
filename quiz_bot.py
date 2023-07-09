from __future__ import annotations

from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import keyboards

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class States:
    name = 'name'
    ready_to_start = 'ready_to_start'
    q1 = 'q1'
    q2 = 'q2'
    q3 = 'q3'


@dp.message_handler(commands=['start'],state='*')
async def start_handler(message: Message, state: FSMContext):
    await message.answer("Добро пожаловать в квиз! Как тебя зовут?")
    await state.set_state('name')
    

@dp.message_handler(state=States.name)
async def name_handler(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Готов начать?)",
                         reply_markup=keyboards.start_keyboard)
    await state.set_state(States.ready_to_start)
    
    
@dp.message_handler(state=States.ready_to_start)
async def start_button_handler(message: Message, state: FSMContext):
    await state.update_data(score=0)
    if message.text == keyboards.start_button.text:
        await message.answer("Отлично! Первый вопрос: сколько было найдено планет "
                             "за пределами Солнечной системы?",
                             reply_markup=keyboards.q1_answers)
        await state.set_state(States.q1)
    else:
        await message.reply("Напиши как будешь готов)")

@dp.message_handler(state=States.q1)
async def q1_handler(message: Message, state: FSMContext):
    if message.text == keyboards.q1_b.text:
        await message.reply("Правильно!")
        data = await state.get_data()
        await state.update_data(score=data['score']+1)
    else:
        await message.reply(f"Неправильно: правильный ответ {keyboards.q1_b.text}")
    await message.answer("Cколько лет Земле?",
                        reply_markup=keyboards.q2_answers)
    await state.set_state(States.q2)
    
@dp.message_handler(state=States.q2)
async def q1_handler(message: Message, state: FSMContext):
    if message.text == keyboards.q2_c.text:
        await message.reply("Правильно!")
        data = await state.get_data()
        await state.update_data(score=data['score']+1)
    else:
        await message.reply(f"Неправильно: правильный ответ {keyboards.q2_c.text}")
    await message.answer("Солнце является ...",
                        reply_markup=keyboards.q3_answers)
    await state.set_state(States.q3)
    

@dp.message_handler(state=States.q3)
async def q1_handler(message: Message, state: FSMContext):
    if message.text == keyboards.q3_b.text:
        await message.reply("Правильно!", 
                            reply_markup=types.ReplyKeyboardRemove())
        data = await state.get_data()
        await state.update_data(score=data['score']+1)
    else:
        await message.reply(f"Неправильно: правильный ответ {keyboards.q3_b.text}", 
                            reply_markup=types.ReplyKeyboardRemove())
        
        
    await message.answer(f"Вы закончили квиз. Ваш результат {(await state.get_data())['score']} и {3}")
    
    
executor.start_polling(dp, skip_updates=True)