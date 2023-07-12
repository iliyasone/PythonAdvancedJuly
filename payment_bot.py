from __future__ import annotations

from config import TOKEN, PAYMENT_TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['buy'])
async def process_buy_command(message: types.Message):
    await bot.send_invoice(
        chat_id= message.from_user.id,
        title='Курс Python Advanced',
        description='Курс продвинутого программирования по Python Advanced',
        currency='rub',
        provider_token=PAYMENT_TOKEN,
        is_flexible=False,
        prices=[
            types.LabeledPrice(
                label='Курс по питон-телеграм ботам', 
                amount=30_000_00
                ),
            types.LabeledPrice(
                label='НДС', 
                amount=6_000_00
                ),
            
            ],
        start_parameter='python-advanced-example',
        payload='some-invoice-payload-for-our-internal-use',
        photo_url='https://files.realpython.com/media/Advance_Watermarked.7780b18d1990.jpg',
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=True,
        need_phone_number=True

    )
    
    
@dp.pre_checkout_query_handler(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
    print(pre_checkout_query.order_info)
    print("Check")

executor.start_polling(dp)