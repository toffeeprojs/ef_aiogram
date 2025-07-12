from aiogram import Router
from aiogram.filters import StateFilter

from src.states import Regis

from .location_setting import router as location_setting
from .any_message import router as any_message

router = Router()
router.message.filter(StateFilter(Regis.locationSetting))

router.include_routers(location_setting, any_message)

__all__ = [
    "router"
]
