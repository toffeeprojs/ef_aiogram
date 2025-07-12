from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from src.states import Main
from src.callbacks.currency import CurrencyCallback, CurrencyAction

router = Router()


@router.callback_query(
    CurrencyCallback.filter(
        F.action == CurrencyAction.give
    )
)
async def give_currency(callback_query: CallbackQuery, callback_data: CurrencyCallback, state: FSMContext):
    await state.set_state(Main.giveCurrency)
    await callback_query.message.answer(
        f"{callback_data.currency_name}"
    )

    await callback_query.answer()


__all__ = [
    "router"
]