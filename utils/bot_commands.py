from aiogram import Bot
from aiogram.types import BotCommand
from aiogram.types import BotCommandScopeDefault

commands = [
    BotCommand(command="start", description="Начало работы"),
    BotCommand(command="help", description="Помощь"),
]


async def set_commands(bot: Bot):
    await bot.set_my_commands(commands, BotCommandScopeDefault())
