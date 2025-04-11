from aiogram import Router, F, Bot
from aiogram.types import Message

from database.db import db
from keyboards.inline.user import get_main_menu

router = Router()


@router.message(F.text == "/start")
async def start_func(msg: Message, bot: Bot):
    user_id = msg.from_user.id
    username = msg.from_user.username or None
    first_name = msg.from_user.first_name

    user_info = await db.get_user(user_id)
    if user_info is None:
        await db.create_user(user_id, first_name, username)
    else:
        await db.updated_username(user_id, username)

    await msg.answer(
        text=f"👋 Привет, <b>{msg.from_user.full_name}</b>",
        reply_markup=await get_main_menu(),
        parse_mode="html",
    )
