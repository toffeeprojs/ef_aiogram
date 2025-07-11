from os import environ
import asyncio
from src.main import main


if __name__ == "__main__":
    asyncio.run(
        main(
            token=environ["TELEGRAM_BOT_TOKEN"],
            redis_host=environ["REDIS_HOST"],
        )
    )
