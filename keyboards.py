from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
                          InlineKeyboardButton, InlineKeyboardMarkup


start_button = KeyboardButton("START")

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False).add(start_button)

q1_a = KeyboardButton("< 1k")
q1_b = KeyboardButton("1k - 10k")
q1_c = KeyboardButton("10k - 1kk")
q1_d = KeyboardButton("> 1kk")

q1_answers = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
    ).insert(q1_a).insert(q1_b).add(q1_c).insert(q1_d)


q2_a = KeyboardButton("2023")
q2_b = KeyboardButton("8000")
q2_c = KeyboardButton("6.5ккк")
q2_d = KeyboardButton("Земли не существует")

q2_answers = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
    ).insert(q2_a).insert(q2_b).add(q2_c).insert(q2_d)



q3_a = KeyboardButton("Белым карликом")
q3_b = KeyboardButton("Желтым карликом")
q3_c = KeyboardButton("Солнца не сущесвует")
q3_d = KeyboardButton("Красным гигантом")

q3_answers = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
    ).insert(q3_a).insert(q3_b).add(q3_c).insert(q3_d)

