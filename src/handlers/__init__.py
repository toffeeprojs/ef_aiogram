from aiogram import Router, F
from aiogram.enums import ChatType

from .common import routes as commons
from .regist import route as regis

routes = Router()
routes.message.filter(F.chat.type == ChatType.PRIVATE)

routes.include_routers(*commons, regis)

__all__ = [
    "routes"
]