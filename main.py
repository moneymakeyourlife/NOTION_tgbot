import asyncio
from pytz import timezone
from datetime import datetime

from aiogram import Bot, Dispatcher
from aiogram.types.input_file import FSInputFile
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from handlers import user_commands
from callbacks.user import (
    open_profile,
    back_to_main,
    set_done_daily,
    add_daily_task,
    open_daily_tasks,
    remove_daily_task,
    daily_ok,
)

from database.db import db
from config import TOKEN, ADMIN_ID
from utils.bot_commands import set_commands
from utils.remainders import shchedule_daily_remainders


async def scheduled_task(bot: Bot):
    await db.cleanup_daily_tasks()
    file = FSInputFile("database/database.db")

    now_time_and_date = datetime.now(timezone("Europe/Kyiv")).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    await bot.send_document(
        chat_id=ADMIN_ID,
        document=file,
        caption=f"🗂️ Бекап от {now_time_and_date}",
    )


async def main():
    await db.init_models()

    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        user_commands.router,
        open_profile.router,
        back_to_main.router,
        open_daily_tasks.router,
        add_daily_task.router,
        remove_daily_task.router,
        set_done_daily.router,
        daily_ok.router,
    )

    scheduler = AsyncIOScheduler(timezone=timezone("Europe/Kyiv"))
    scheduler.add_job(scheduled_task, CronTrigger(hour=0, minute=0), args=[bot])
    scheduler.add_job(db.back_daily_to_history, CronTrigger(hour=23, minute=59))
    scheduler.add_job(
        shchedule_daily_remainders, CronTrigger(hour="12,17,22", minute=0), args=[bot]
    )
    scheduler.start()

    await bot.delete_webhook(drop_pending_updates=True)
    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
