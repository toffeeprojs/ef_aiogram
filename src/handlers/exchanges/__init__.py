from aiogram import Router

from .create import router as create
from .list import router as list


router = Router()

router.include_routers(create, list)


__all__ = [
    "router"
]