from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from enum import Enum


class CurrencyAction(Enum):
    give = "give"
    get = "get"

class CurrencyCallback(CallbackData, prefix="currency"):
    action: CurrencyAction
    currency_name: str


def currency_keyboard(action: CurrencyAction) -> InlineKeyboardMarkup:
    currency_name = "USD"

    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=currency_name,
                callback_data=CurrencyCallback(
                    action=action,
                    currency_name=currency_name
                ).pack()
            )
        ]
    ])


__all__ = [
    "CurrencyAction",
    "CurrencyCallback",
    "currency_keyboard"
]
