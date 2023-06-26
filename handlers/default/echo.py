from loader import bot
from aiogram import types


async def echo_(message: types.Message):
    # await message.answer(message.text)
    await bot.send_message(
        message.from_user.id,
        message.text,
        # reply_markup=kb_4_commands(),
    )
