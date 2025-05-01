from pytz import timezone
from datetime import datetime

from aiogram.types import Message
from aiogram import Router, F, Bot

from database.db import db
from keyboards.inline.user import get_main_menu

router = Router()


@router.message(F.text == "/start")
async def start_func(msg: Message, bot: Bot):
    user_id = msg.from_user.id
    username = msg.from_user.username or None
    first_name = msg.from_user.first_name
    now_date = datetime.now(timezone("Europe/Kyiv")).strftime("%Y.%m.%d")

    user_info = await db.get_user(user_id)
    if user_info is None:
        await db.create_user(
            user_id=user_id, first_name=first_name, username=username, reg_date=now_date
        )
        await db.add_user_levels(user_id)
    else:
        await db.updated_username(user_id, username)

    await bot.send_message(
        chat_id=msg.from_user.id,
        text=f"👋 Привет, <b>{msg.from_user.full_name}</b>",
        reply_markup=await get_main_menu(),
        parse_mode="html",
    )
