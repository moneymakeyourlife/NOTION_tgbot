from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from keyboards.inline.user import get_daily_menu, get_main_menu

from database.db import db


router = Router()


@router.callback_query(F.data == "back_to_main")
async def back_to_main(call: CallbackQuery, bot: Bot):
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text=f"👋 Привет, <b>{call.from_user.full_name}</b>",
        reply_markup=await get_main_menu(),
        parse_mode="html",
    )


@router.callback_query(F.data == "back_to_daily")
async def back_to_daily(call: CallbackQuery, bot: Bot):
    user_id = call.from_user.id
    daily_user = await db.get_daily_tasks(user_id)

    answ_text = "📋 Вы перешли в меню ежедневных задач\n\n"

    if len(daily_user) == 0:
        answ_text += "❗️ У вас нет ежедневных задач"
    else:
        for task in daily_user:
            if task.is_done:
                answ_text += f"✅ {task.daily_task}\n"
            else:
                answ_text += f"📝 {task.daily_task}\n"

    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text=answ_text,
        reply_markup=await get_daily_menu(),
    )
