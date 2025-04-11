import asyncio
from aiogram import Bot, Dispatcher

from handlers import user_commands
from callbacks.user import open_profile, back_to_main
from utils.bot_commands import set_commands

from database.db import db
from config import TOKEN


async def main():
    await db.init_models()

    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        user_commands.router,
        open_profile.router,
        back_to_main.router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
