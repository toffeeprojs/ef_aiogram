from aiogram import Router, html
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton
)

from src.states import Regis

route = Router()


@route.message(CommandStart())
async def start(message: Message, state: FSMContext) -> None:
    await state.set_state(Regis.locationSetting)
    await message.answer(
        f"{html.bold('Отправь геометку')}\n"
        "Это необходимо что бы я мог подобрать ближайших людей для обмена валют",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Отправить геометку", request_location=True)]
            ],
            resize_keyboard=True,
            is_persistent=True,
            one_time_keyboard=True
        ),
    )

__all__ = [
    "route"
]
