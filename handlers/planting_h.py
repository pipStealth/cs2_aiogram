from config import config
import asyncio
import logging
from aiogram import Router, F, types, Bot
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, \
    BufferedInputFile, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from datetime import datetime
from aiogram.enums import ParseMode
from state import *
from keyboard import *

router = Router()
bot = Bot(config["token"]) #  Creating bot instance with token

### START CALLBACK OF LINE WITH `SUPPORT` CALLABLE ###
@router.callback_query(F.data == "support", StateFilter(None)) 
async def cmd_support(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Support.start_support)
    await callback.message.answer(f"<strong>Підтримка:</strong>", parse_mode=ParseMode.HTML, reply_markup=support_InLineKeyBoard(message=callback.message))

### ACCEPT THE  USER'S MESSAGE AND GO TO NEXT STATE ###
@router.callback_query(F.data == "to_develop", StateFilter(Support.start_support))
async def cmd_support_toDevelop(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Support.communication)
    await callback.answer("Чекаю ваше повідомлення!")

@router.message(F.text, StateFilter(Support.communication))
async def cmd_getText(message: types.Message,  state: FSMContext):
    await bot.send_message(config["admin_id"], f"""
{datetime.now()}
Нове повідомлення від {message.from_user.full_name};
Посилання на юзера: @{message.from_user.username}
Повідомлення: {message.text}
                           """)
    await message.answer("Повідомлення було відправлено! Протягом доби ви отримаєте відповідь.")
    await state.set_state(Support.start_support)

@router.callback_query(F.data == "back_support", StateFilter(Support.start_support))
async def cmd_support_toDevelop(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(None)
    await callback.message.reply(f"<b>Привіт, <code>{callback.message.from_user.full_name}!</code> 😉\nЦей бот має збірку фіч для гри CS2!</b>", parse_mode=ParseMode.HTML, reply_markup=start_InLineKeyBoard(callback.message))