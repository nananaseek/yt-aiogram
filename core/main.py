import logging

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode

from .settings.config import settings
from .settings.log import DEFAULT_LOGGING
from .database.init_db import startup_db, shutdown_db
from .handlers.comand import command_router
from .handlers.message import router as yt_down_router

dp = Dispatcher()
bot = Bot(settings.TOKEN, parse_mode=ParseMode.HTML)


async def configure_logging(log_settings: dict = None):
    log_settings = log_settings or DEFAULT_LOGGING
    logging.config.dictConfig(log_settings)
    logging.info('Logging settings is activate')


async def init_bot() -> None:

    dp.startup.register(configure_logging)
    dp.startup.register(startup_db)
    dp.shutdown.register(shutdown_db)
    dp.include_router(command_router)
    dp.include_router(yt_down_router)

    await dp.start_polling(bot)
