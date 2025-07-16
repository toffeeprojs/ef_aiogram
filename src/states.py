from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    location = State()


class Main(StatesGroup):
    menu = State()


class ExchangesList(StatesGroup):
    get = State()
    give = State()


class ExchangesCreate(StatesGroup):
    rate = State()
    comment = State()


class Settings(StatesGroup):
    view = State()
    display_name = State()


__all__ = [
    "Registration",
    "Main",
    "ExchangesList",
    "ExchangesCreate",
    "Settings",
]
