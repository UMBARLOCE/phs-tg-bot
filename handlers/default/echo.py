"""echo.py."""
import string
import json
import asyncio
from aiogram import types

from config_data.loader import bot


async def echo_(message: types.Message) -> None:
    """
    Пустой хендлер.

    Удаляет мат сразу.
    Удаляет предупреждения через 5 секунд.
    """
    # await bot.send_message(
    #     message.from_user.id,
    #     message.text,
    #     # reply_markup=kb_4_commands(),
    # )
    text_mes: str = "".join(
        [i for i in message.text.lower() if i.isalnum()]
    )
    for mat in json.load(fp=open(file="censor/cenz.json")):
        if mat in text_mes:
            await message.delete()
            try:
                warning_mes: types.Message = await bot.send_message(
                    chat_id=message.from_user.id,
                    text="Маты запрещены!",
                )
            except Exception as exc:
                warning_mes: types.Message = await message.answer(
                    text="Маты запрещены!",
                )
            await asyncio.sleep(delay=5)
            await warning_mes.delete()
            break
    else:
        await message.answer(text="неизвестная команда")
