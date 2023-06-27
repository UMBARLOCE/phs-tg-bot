"""registar.py"""
from aiogram.dispatcher import Dispatcher
from aiogram.types import BotCommand
from handlers import default


COMMANDS = [
    default.start.start_,
    default.help.help_,
]

HANDLERS = [

]


def set_handlers(dp: Dispatcher) -> None:
    """Регистрация хендлеров."""
    [
        dp.register_message_handler(
            callback=func,
            commands=func.__name__[:-1],
        )
        for func in COMMANDS  # .extend(HANDLERS)
    ]

    # dp.register_message_handler(start.start_, commands=['start'])
    # dp.register_message_handler(help.help_, commands=['help'])
    dp.register_message_handler(callback=default.echo.echo_)  # эхо последнее


async def set_commands(dp: Dispatcher) -> None:
    """Регистрация команд."""
    await dp.bot.set_my_commands(
        [
            BotCommand(
                command=f"/{func.__name__[:-1]}",
                description=func.__doc__,
            )
            for func in COMMANDS
        ]
    )
