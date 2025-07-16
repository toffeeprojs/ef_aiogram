from aiogram import Router

from src.middlewares import NoMessageMiddleware
from src.states import ExchangesList, ExchangesCreate
from .admin import router as admin
from .common import router as common
from .exchanges import router as exchanges
from .main import router as main
from .registration import router as registration
from .settings import router as settings


router = Router()
router.message.middleware(
    NoMessageMiddleware([
        ExchangesList.get,
        ExchangesList.give,
        ExchangesCreate.rate,
        ExchangesCreate.comment
    ])
)

router.include_routers(
    admin,
    common,
    exchanges,
    main,
    registration,
    settings
)


__all__ = [
    "router"
]
