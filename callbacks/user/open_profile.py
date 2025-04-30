from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from database.db import db
from utils.draw_utils import draw_human
from keyboards.inline.user import get_back_to_main_menu

router = Router()


@router.callback_query(F.data == "profile")
async def open_profile(call: CallbackQuery, bot: Bot):
    user_id = call.from_user.id
    user_info = await db.get_user(user_id)
    user_levels = await db.get_user_levels(user_id)

    human_drow = await draw_human(
        head_level=user_levels.head_level,
        body_level=user_levels.body_level,
        legs_level=user_levels.legs_level,
        arms_level=user_levels.arms_level,
    )

    answ_text = (
        f"👤 Профиль\n\n"
        f"{human_drow}\n\n"
        f"Имя: {user_info.first_name}\n"
        f"Юзернейм: {user_info.username}\n"
    )

    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text=answ_text,
        reply_markup=await get_back_to_main_menu(),
    )
