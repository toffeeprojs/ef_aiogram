from aiogram import Router
from aiogram.filters import StateFilter

from src.states import Main

from .get_currency import router as get_currency
from .give_currency import router as give_currency
from .any_message import router as any_message

router = Router()
router.message.filter(StateFilter(Main.getCurrency, Main.giveCurrency))

router.include_routers(get_currency, give_currency, any_message)

__all__ = [
    "router"
]
