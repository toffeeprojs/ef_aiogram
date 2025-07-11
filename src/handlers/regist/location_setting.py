from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
    Location,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from src.states import Main

route = Router()


@route.message(F.location.as_("location"))
async def location_setting(message: Message, state: FSMContext, location: Location):
    await state.set_state(Main.getCurrency)
    await message.answer(
        f"{location.latitude}, {location.longitude}",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="UST", callback_data="aaa")
                ]
            ]
        )
    )


__all__ = [
    "route"
]
