from aiogram import Router, types
from aiogram.filters import CommandStart

command_router = Router()


@command_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f'Привіт {message.from_user.username}. \n'
                         f'Надішли мені посилання на ютуб і я тобі відправю відео з ютубу')
