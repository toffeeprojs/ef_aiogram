from aiogram import Router
from aiogram.filters import StateFilter

from src.states import Post

from .rate_setting import router as rate_setting
from .comment_setting import router as comment_setting
from .any_message import router as any_message

router = Router()
router.message.filter(StateFilter(Post.rateSetting, Post.commentSettings))

router.include_routers(rate_setting, comment_setting, any_message)

__all__ = [
    "router"
]