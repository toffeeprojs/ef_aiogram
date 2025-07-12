from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from src.states import Main
from src.callbacks.currency import (
    CurrencyCallback,
    CurrencyAction,
    currency_keyboard
)

router = Router()


@router.callback_query(
    CurrencyCallback.filter(
        F.action == CurrencyAction.get
    )
)
async def get_currency(callback_query: CallbackQuery, callback_data: CurrencyCallback, state: FSMContext):
    await state.set_state(Main.giveCurrency)
    await callback_query.message.answer(
        f"{callback_data.currency_name}",
        reply_markup=currency_keyboard(
            CurrencyAction.give
        )
    )

    await callback_query.answer()


__all__ = [
    "router"
]