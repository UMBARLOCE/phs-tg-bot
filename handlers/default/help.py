from aiogram import types
from config_data.loader import bot


async def help_(message: types.Message) -> None:
    """Вызвать справку"""
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Бот для поиска оптимальных отелей.\n"
        "Команды с описанием указаны в МЕНЮ.",
        # reply_markup=kb_4_commands(),
    )
