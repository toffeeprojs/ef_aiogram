from aiogram import Router

from .start import route as start

routes: list[Router] = [start]

__all__ = [
    "routes"
]
