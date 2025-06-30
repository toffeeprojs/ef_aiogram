import asyncio
from os import getenv

from src.main import main

if __name__ == "__main__":
    TOKEN = getenv("TELEGRAM_BOT_TOKEN")

    if TOKEN:
        asyncio.run(main(TOKEN))
    else:
        print(TOKEN)
        raise EnvironmentError