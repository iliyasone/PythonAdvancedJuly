from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
                          InlineKeyboardButton, InlineKeyboardMarkup

click = InlineKeyboardButton("click 🧟", callback_data='click')
double_click = InlineKeyboardButton("double-click 🧟‍♀️", callback_data='double-click')

first_keyboard = InlineKeyboardMarkup().add(click)

second_keyboard = InlineKeyboardMarkup().add(click).add(double_click)