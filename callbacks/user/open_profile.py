from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery
from aiogram.types.input_file import FSInputFile

from database.db import db
from keyboards.inline.user import get_back_to_main_menu

router = Router()


@router.callback_query(F.data == "profile")
async def open_profile(call: CallbackQuery, bot: Bot):
    user_id = call.from_user.id
    user_info = await db.get_user(user_id)

    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text=f"👤 Профиль\n\n"
        f"Имя: {user_info.first_name}\n"
        f"Юзернейм: {user_info.username}\n",
        reply_markup=await get_back_to_main_menu(),
    )
