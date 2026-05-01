import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.core.handlers import router
from app.data.models import init_models

load_dotenv()

TG_TOKEN = os.getenv("TG_TOKEN")


async def main() -> None:
    """Основная асинхронная функция запуска бота.

    Также запускает функцию init_models.
    """
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TG_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await init_models()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
