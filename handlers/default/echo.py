from aiogram import types
from config_data.loader import bot


async def echo_(message: types.Message):
    # await message.answer(message.text)
    await bot.send_message(
        message.from_user.id,
        message.text,
        # reply_markup=kb_4_commands(),
    )
