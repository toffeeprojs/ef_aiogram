from aiogram import BaseMiddleware
from aiogram.fsm.state import State
from aiogram.types import Update, Message
from typing import Callable, Awaitable, Any, Dict, Union

from .common_lib.postgres import PostgresManager


class DependencyMiddleware(BaseMiddleware):
    def __init__(self, postgres_manager: PostgresManager):
        self.postgres_manager = postgres_manager

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any]
    ) -> Any:
        data["postgres_manager"] = self.postgres_manager

        return await handler(event, data)


class NoMessageMiddleware(BaseMiddleware):
    def __init__(self, allowed_states: list[Union[State, str, None]]):
        self.allowed_states = allowed_states

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ):
        if data_state := data.get("state"):
            if state := await data_state.get_state():
                if state not in self.allowed_states:
                    return None

        return await handler(event, data)


__all__ = [
    "DependencyMiddleware",
    "NoMessageMiddleware",
]
