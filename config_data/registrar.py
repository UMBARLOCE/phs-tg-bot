from aiogram.dispatcher import Dispatcher
from aiogram.types import BotCommand
from handlers import default


COMMANDS = [
    default.start.start_,
    default.help.help_,
]


def set_handlers(dp: Dispatcher):
    """Регистрация хендлеров."""
    [
        dp.register_message_handler(
            func,
            commands=func.__name__[:-1],
        )
        for func in COMMANDS
    ]

    dp.register_message_handler(default.echo.echo_)  # эхо последнее


async def set_commands(dp: Dispatcher):
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
