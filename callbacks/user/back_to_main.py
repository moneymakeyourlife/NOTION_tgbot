from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from keyboards.inline.user import get_main_menu

router = Router()


@router.callback_query(F.data == "back_to_main")
async def back_to_main(call: CallbackQuery, bot: Bot):
    await bot.delete_message(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
    )

    await bot.send_message(
        chat_id=call.from_user.id,
        text=f"👋 Привет, <b>{call.from_user.full_name}</b>",
        reply_markup=await get_main_menu(),
        parse_mode="html",
    )
