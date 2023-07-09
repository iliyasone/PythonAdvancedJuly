from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
                          InlineKeyboardButton, InlineKeyboardMarkup


b1 = KeyboardButton("чат 1 на 1")
b2 = KeyboardButton("групповой чат")

choose_chat_type_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True).insert(b1).insert(b2)