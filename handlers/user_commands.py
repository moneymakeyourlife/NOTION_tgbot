from aiogram.types import Message
from aiogram import Router, F, Bot
from aiogram.types.input_file import FSInputFile

from database.db import db
from keyboards.inline.user import get_main_menu

from config import MAIN_IMAGE


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

    photo = FSInputFile("images/mainMenu.jpg")

    await bot.send_photo(
        chat_id=msg.from_user.id,
        photo=photo,
        caption=f"👋 Привет, <b>{msg.from_user.full_name}</b>",
        reply_markup=await get_main_menu(),
        parse_mode="html",
    )


@router.message(F.photo)
async def handle_photo(msg: Message):
    await msg.answer(
        f"file_id: <code>{msg.photo[-1].file_id}</code>", parse_mode="html"
    )
