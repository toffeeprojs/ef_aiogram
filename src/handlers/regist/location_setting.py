from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
    Location,
    ReplyKeyboardRemove
)

from src.states import Main
from src.callbacks.currency import CurrencyAction, currency_keyboard

router = Router()


@router.message(F.location.as_("location"))
async def location_setting(message: Message, state: FSMContext, location: Location):
    await state.set_state(Main.getCurrency)
    await message.answer("Отлично! Регистрация пройдена", reply_markup=ReplyKeyboardRemove())

    await message.answer(
        f"{location.latitude}\n"
        f"{location.longitude}",
        reply_markup=currency_keyboard(
            CurrencyAction.get
        )
    )


__all__ = [
    "router"
]
