from aiogram import Router
from aiogram.filters import StateFilter

from src.states import Regis
from .location_setting import route as location_setting

route = Router()
route.message.filter(StateFilter(Regis.locationSetting))

route.include_router(location_setting)

__all__ = [
    "route"
]
