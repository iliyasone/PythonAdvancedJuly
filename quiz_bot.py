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
                         reply_markup=keyboards.start_keyboard)
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
    
    answers_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                 one_time_keyboard=True)
    
    for answer in question.answers:
        button = types.KeyboardButton(answer)
        answers_keyboard.insert(button)
        
    
    await message.answer(question.text,
                         reply_markup=answers_keyboard)
    
    
@dp.message_handler(state=States.question)
async def handle_answer(message: Message, state: FSMContext):
    text = message.text
    
    data = await state.get_data()
    i = data['last_question']
    score = data['score']
    
    current_question = questions[i]
    
    if text == current_question.rigth_answer:
        score += 1
        await state.update_data(score=score)    
        await message.reply("OK!")
    else:
        await message.reply("NOT OK!")
        await message.answer(f'Правильный ответ {current_question.rigth_answer}')
        
        if current_question.explanation:
            await message.answer(current_question.explanation)
    
    await state.update_data(last_question=i+1)
    
    if i+1 >= len(questions):
        await state.set_state(States.final)
        await message.answer(f'{data["name"]}. вот ваш счет: {score} из {len(questions)}')
    else:
        await ask_question(message, i+1)

input("Press ENTER to start")
executor.start_polling(dp, skip_updates=False)