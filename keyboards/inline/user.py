from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def get_main_menu() -> InlineKeyboardMarkup:
    kb_btns = [
        [InlineKeyboardButton(text="👤 Профиль", callback_data="profile")],
        [InlineKeyboardButton(text="‼️ Ежедневки", callback_data="daily")],
    ]

    kb = InlineKeyboardMarkup(inline_keyboard=kb_btns, resize_keyboard=True)
    return kb


async def get_back_to_main_menu() -> InlineKeyboardMarkup:
    kb_btns = [
        [InlineKeyboardButton(text="🔙 Главное меню", callback_data="back_to_main")],
    ]

    kb = InlineKeyboardMarkup(inline_keyboard=kb_btns, resize_keyboard=True)
    return kb
