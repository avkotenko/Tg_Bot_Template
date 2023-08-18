from aiogram import Bot, Dispatcher
import asyncio
from dotenv import load_dotenv
import os
from handlers import commands, differents_type
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.middlewares import DbSessionMiddleware

load_dotenv()

token=os.getenv("TOKEN")
dp = Dispatcher()
bot = Bot(token=token)


async def main():
    engine = create_async_engine(url=os.getenv("URL_BD"), echo=True)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

    dp.update.middleware(DbSessionMiddleware(session_pool=sessionmaker))


    await bot.send_message(os.getenv("OWNER"), 'Start bot')

    dp.include_routers(commands.router, differents_type.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())