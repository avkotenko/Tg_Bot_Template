from aiogram import types, Router
from aiogram.filters.command import Command


from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Users


router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message, session: AsyncSession):
    """
    Хэндлер команды /start
    Отправляем сообщение пользователю и сохранияем его данные в БД
    """
    await session.merge(Users(user_id=message.from_user.id))
    await session.commit()
    await message.reply("Commands start")

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    """
    Хэндлер команды /help
    Отправляем сообщение пользователю
    """
    await message.reply("Commands help")


