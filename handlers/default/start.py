from aiogram import types
from config_data.loader import bot


async def start_(message: types.Message):
    """Запустить бота"""
    await bot.send_message(
        message.from_user.id,
        f"Привет, {message.from_user.full_name}!",
        # reply_markup=kb_4_commands(),
    )
