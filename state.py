from aiogram.fsm.state import StatesGroup, State

class Throwing(StatesGroup):
    start_throwing = State()
    Mirage_throwing = State()
    Inferno_throwing = State()
    Dust2_throwing = State()

class Planting(StatesGroup):
    start_planting = State()
    Mirage_planting = State()
    Inferno_planting = State()
    Dust2_planting = State()

class Support(StatesGroup):
    start_support = State()
    communication = State()