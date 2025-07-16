from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


router = Router()

@router.message()
async def start(message: Message, state: FSMContext):
    await message.answer("Hello!")


__all__ = [
    "router"
]