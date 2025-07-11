from aiogram.fsm.state import StatesGroup, State


class Regis(StatesGroup):
    locationSetting = State()

class Main(StatesGroup):
    getCurrency = State()
    giveCurrency = State()

class Post(StatesGroup):
    rateSetting = State()
    commentSettings = State()
