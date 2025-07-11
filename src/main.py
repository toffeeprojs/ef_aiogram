from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis

from .handlers import routes


async def main(token: str, redis_host: str) -> None:
    dp = Dispatcher(storage=RedisStorage(redis=Redis(host=redis_host), state_ttl=172_800))
    dp.include_routers(routes)

    await dp.start_polling(
        Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    )
