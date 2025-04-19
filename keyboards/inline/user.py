from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def get_main_menu() -> InlineKeyboardMarkup:
    kb_btns = [
        [InlineKeyboardButton(text="👤 Профиль", callback_data="profile")],
        [InlineKeyboardButton(text="‼️ Ежедневки", callback_data="daily_tasks")],
    ]

    kb = InlineKeyboardMarkup(inline_keyboard=kb_btns, resize_keyboard=True)
    return kb


async def get_back_to_main_menu() -> InlineKeyboardMarkup:
    kb_btns = [
        [InlineKeyboardButton(text="🔙 Главное меню", callback_data="back_to_main")],
    ]

    kb = InlineKeyboardMarkup(inline_keyboard=kb_btns, resize_keyboard=True)
    return kb


async def get_back_to_daily_menu() -> InlineKeyboardMarkup:
    kb_btns = [
        [InlineKeyboardButton(text="🔙 Ежедневки", callback_data="back_to_daily")],
    ]

    kb = InlineKeyboardMarkup(inline_keyboard=kb_btns, resize_keyboard=True)
    return kb


async def get_daily_menu() -> InlineKeyboardMarkup:
    kb_btns = [
        [
            InlineKeyboardButton(text="➕ Добавить", callback_data="add_daily_task"),
            InlineKeyboardButton(text="➖ Удалить", callback_data="remove_daily_task"),
        ],
        [
            InlineKeyboardButton(
                text="✅ Отметить выполненые", callback_data="done_daily_task"
            ),
        ],
        [InlineKeyboardButton(text="📊 Статистика", callback_data="daily_statistic")],
        [InlineKeyboardButton(text="🔙 Главное меню", callback_data="back_to_main")],
    ]

    kb = InlineKeyboardMarkup(inline_keyboard=kb_btns, resize_keyboard=True)
    return kb


async def get_accept_cancel_keyboard() -> InlineKeyboardMarkup:
    kb_btns = [
        [
            InlineKeyboardButton(text="✅ Да", callback_data="accept"),
            InlineKeyboardButton(text="❌ Нет", callback_data="cancel"),
        ]
    ]

    kb = InlineKeyboardMarkup(inline_keyboard=kb_btns, resize_keyboard=True)
    return kb
