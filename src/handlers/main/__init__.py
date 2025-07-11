from aiogram import Router
from aiogram.filters import StateFilter

from src.states import Main

route = Router()
route.message.filter(StateFilter(Main.getCurrency, Main.giveCurrency))

__all__ = [
    "route"
]
