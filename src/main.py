from os import environ
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.storage.memory import MemoryStorage
from redis.asyncio.client import Redis

from .middlewares import DependencyMiddleware
from .common_lib.postgres import PostgresManager, PostgresSettings
from .handlers import router


async def main() -> None:
    dp = Dispatcher(
        storage=RedisStorage(
            redis=Redis(
                host=environ["REDIS_HOST"]
            ),
            state_ttl=86_400
        )
    )

    postgres_manager = PostgresManager(
        PostgresSettings()
    )

    await postgres_manager.connect()

    try:
        dp.update.middleware(
            DependencyMiddleware(
                postgres_manager
            )
        )

        dp.include_router(router)

        await dp.start_polling(
            Bot(
                token=environ["TELEGRAM_BOT_TOKEN"],
                default=DefaultBotProperties(
                    parse_mode=ParseMode.HTML
                )
            )
        )
    finally:
        await postgres_manager.disconnect()
