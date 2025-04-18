from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import (
    CallbackQuery,
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from database.db import db
from keyboards.inline.user import get_accept_cancel_keyboard, get_back_to_daily_menu

router = Router()


@router.callback_query(F.data == "remove_daily_task")
async def open_remove_daily_task(call: CallbackQuery, bot: Bot, state: FSMContext):
    user_id = call.from_user.id

    daily_user = await db.get_daily_tasks(user_id)

    kb = []

    for task in daily_user:
        kb.append(
            [
                InlineKeyboardButton(
                    text=task.daily_task,
                    callback_data=f"del_daily_{task.id}",
                )
            ]
        )
    kb.append(
        [
            InlineKeyboardButton(
                text="⬅️ Назад",
                callback_data="back_to_daily",
            )
        ]
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    await bot.delete_message(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
    )

    await bot.send_message(
        chat_id=call.from_user.id,
        text="❗️ Выберите задачу, которую хотите удалить",
        reply_markup=keyboard,
    )
