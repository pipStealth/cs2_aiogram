from aiogram import types

# KEYBOARDS FOR /START
def start_InLineKeyBoard(message):
    kb = [
        [types.InlineKeyboardButton(text="Раскидки😎", callback_data="throwing"),
        types.InlineKeyboardButton(text="Подсадки😊", callback_data="planting")],
        [types.InlineKeyboardButton(text="Підтримка👌", callback_data="support")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard

# KEYBOARDS FOR CALLBACK THROWING
def throwing_InLineKeyBoard(message):
    kb = [
        [types.InlineKeyboardButton(text="Mirage 😎", callback_data="mirage_throwing"),
        types.InlineKeyboardButton(text="Inferno 😊", callback_data="inferno_throwing")],
        [types.InlineKeyboardButton(text="Dust2 👌", callback_data="dust2_throwing")],
        [types.InlineKeyboardButton(text="Назад ⏪", callback_data="back_throwing")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard

# KEYBOARDS FOR CALLBACK PLANTING
def planting_InLineKeyBoard(message):
    kb = [
        [types.InlineKeyboardButton(text="Mirage 😎", callback_data="mirage_planting"),
        types.InlineKeyboardButton(text="Inferno 😊", callback_data="inferno_planting")],
        [types.InlineKeyboardButton(text="Dust2 👌", callback_data="dust2_planting")],
        [types.InlineKeyboardButton(text="Назад ⏪", callback_data="back_planting")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard

# KEYBOARDS FOR CALLBACK SUPPORT
def support_InLineKeyBoard(message):
    kb = [
        [types.InlineKeyboardButton(text="Написати девелоперу 📩", callback_data="to_develop")],
        [types.InlineKeyboardButton(text="Ліцензія 📃", url="https://docs.google.com/document/d/12ngYWMpfR2kSg1GLg591W87V90TqNeiIXOhl1IeCLD8/edit?usp=sharing", callback_data="license")],
        [types.InlineKeyboardButton(text="Назад ⏪", callback_data="back_support")]
    ]

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard