############################## IMPORTING ##############################
from config import config
import asyncio
import logging
#import Video_inferno
from datetime import datetime
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, \
    BufferedInputFile, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
#from handlers import planting_h, support, throwing
from state import *
from keyboard import *

##########################################################################
# REGISTRATION AND INITIALIZATION BOT 

logging.basicConfig(level=logging.INFO) #  Setting the level of logs to INFO
bot = Bot(config["token"]) #  Creating bot instance with token
dp = Dispatcher() # Create dispatcher type
#dp.include_routers(planting_h.router, support.router, throwing.router) # Fix soon...

##########################################################################
# ADDITIONALY DEFINED FUNCTIONS
##########################################################################

# LOGS
def update_file(message):
    with open("information.txt", "r") as file:
        length = len(file.read())
        print(f"Длина Документа Логiв : {length}")

    with open("information.txt", "a") as file:
        file.write(f"Користувач написав : {message.text}\n")
        file.write(f"Повне Iм'я Користувача : {message.from_user.username}\n")
        file.write(f"Айди Користувача : {message.from_user.id}\n")
        file.write(f"Url Користувача : {message.from_user.url}\n")
        file.write(f"Час вiдправки : {datetime.now()}\n\n")


##########################################################################


### START COMMAND ###
@dp.message(Command("start"), StateFilter(None))
async def cmd_start(message: types.Message, state: FSMContext):
    update_file(message)
    await message.reply(f"<b>Привіт, <code>{message.from_user.full_name}!</code> 😉\nЦей бот має збірку фіч для гри CS2!</b>", parse_mode=ParseMode.HTML, reply_markup=start_InLineKeyBoard(message))

### START CALLBACK OF LINE WITH `THROWING` CALLABLE ###
@dp.callback_query(F.data == "throwing", StateFilter(None))
async def cmd_throwing(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Throwing.start_throwing)
    await callback.message.answer(f"<strong>Мапи:</strong>", parse_mode=ParseMode.HTML, reply_markup=throwing_InLineKeyBoard(message=callback.message))

@dp.callback_query(F.data == "back_throwing", StateFilter(Throwing.start_throwing))
async def cmd_support_toDevelop(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(None)
    await callback.message.reply(f"<b>Привіт, <code>{callback.message.from_user.full_name}!</code> 😉\nЦей бот має збірку фіч для гри CS2!</b>", parse_mode=ParseMode.HTML, reply_markup=start_InLineKeyBoard(callback.message))

### START CALLBACK OF LINE WITH `PLANTING` CALLABLE ###
@dp.callback_query(F.data == "planting", StateFilter(None))
async def cmd_throwing(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Planting.start_planting)
    await callback.message.answer(f"<strong>Мапи:</strong>", parse_mode=ParseMode.HTML, reply_markup=planting_InLineKeyBoard(message=callback.message))

@dp.callback_query(F.data == "back_planting", StateFilter(Planting.start_planting))
async def cmd_support_toDevelop(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(None)
    await callback.message.reply(f"<b>Привіт, <code>{callback.message.from_user.full_name}!</code> 😉\nЦей бот має збірку фіч для гри CS2!</b>", parse_mode=ParseMode.HTML, reply_markup=start_InLineKeyBoard(callback.message))

### START CALLBACK OF LINE WITH `SUPPORT` CALLABLE ###
@dp.callback_query(F.data == "support", StateFilter(None)) 
async def cmd_support(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Support.start_support)
    await callback.message.answer(f"<strong>Підтримка:</strong>", parse_mode=ParseMode.HTML, reply_markup=support_InLineKeyBoard(message=callback.message))

### ACCEPT THE  USER'S MESSAGE AND GO TO NEXT STATE ###
@dp.callback_query(F.data == "to_develop", StateFilter(Support.start_support))
async def cmd_support_toDevelop(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Support.communication)
    await callback.answer("Чекаю ваше повідомлення!")

@dp.message(F.text, StateFilter(Support.communication))
async def cmd_getText(message: types.Message,  state: FSMContext):
    await bot.send_message(config["admin_id"], f"""
{datetime.now()}
Нове повідомлення від {message.from_user.full_name};
Посилання на юзера: @{message.from_user.username}
Повідомлення: {message.text}
                           """)
    await message.answer("Повідомлення було відправлено! Протягом доби ви отримаєте відповідь.")
    await state.set_state(Support.start_support)

@dp.callback_query(F.data == "back_support", StateFilter(Support.start_support))
async def cmd_support_toDevelop(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(None)
    await callback.message.reply(f"<b>Привіт, <code>{callback.message.from_user.full_name}!</code> 😉\nЦей бот має збірку фіч для гри CS2!</b>", parse_mode=ParseMode.HTML, reply_markup=start_InLineKeyBoard(callback.message))

#########################################################################
@dp.message(F.text)
async def cmd_answer(message: types.Message):
    update_file(message)
    await message.answer("Привіт, я тебе не зрозумів 😢.\nВикористай /start!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


