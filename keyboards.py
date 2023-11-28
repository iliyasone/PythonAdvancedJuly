from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
                          InlineKeyboardButton, InlineKeyboardMarkup


start_button = KeyboardButton("START")

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False).add(start_button)


button_108 = InlineKeyboardButton("108", callback_data='bus108')
button_106 = InlineKeyboardButton("106", callback_data='bus106')

busses_keyboard = InlineKeyboardMarkup().insert(button_106).insert(button_108)

button_back = InlineKeyboardButton("Вернуться назад", callback_data='back')
back_keyboard = InlineKeyboardMarkup().add(button_back)