from __future__ import annotations

from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import keyboards
from questions import questions
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class States:
    name = 'name'
    ready_to_start = 'ready_to_start'
    question = 'question'
    final = 'final'

@dp.message_handler(commands=['start'],state='*')
async def start_handler(message: Message, state: FSMContext):
    await message.answer("Добро пожаловать в квиз! Как тебя зовут?")
    await state.set_state('name')
    

@dp.message_handler(state=States.name)
async def name_handler(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Готов начать?)",
                         reply_markup=)
    await state.set_state(States.ready_to_start)
    
    

@dp.message_handler(state=States.ready_to_start)
async def start_button_handler(message: Message, state: FSMContext):
    await state.update_data(score=0)
    if message.text == keyboards.start_button.text:
        await state.update_data(score=0,last_question=0)
        await message.answer("Отлично! Первый вопрос:")
        await state.set_state(States.question)
        await ask_question(message=message)
    else:
        await message.reply("Напиши как будешь готов)")


async def ask_question(message: Message, question_number: int = 0):
    question = questions[question_number]

    await bot.send_poll(
        chat_id=message.from_user.id,
        options=question.answers,
        is_anonymous=False,
        type = 'Quiz',
        correct_option_id=question.rigth_answer_index
    )
    
    
executor.start_polling(dp)