from aiogram import Router

from .admin import routers as admins
from .start import route as start

routers: list[Router] = [*admins, start]

__all__ = [
    "routers"
]
