from aiogram import Router, F
from aiogram.enums import ChatType

from .common import routers as commons
from .main import router as main
from .post import router as post
from .regist import router as regist

router = Router()
router.message.filter(F.chat.type == ChatType.PRIVATE)
router.callback_query.filter(F.message)

router.include_routers(*commons, main, post, regist)

__all__ = [
    "router"
]