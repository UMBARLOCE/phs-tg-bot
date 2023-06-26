from aiogram.dispatcher import Dispatcher
from aiogram.types import BotCommand
from handlers.default import start, help, echo


def set_handlers(dp: Dispatcher):
    """Регистрация хендлеров."""
    dp.register_message_handler(start.start_, commands=["start"])
    dp.register_message_handler(help.help_, commands=["help"])

    dp.register_message_handler(echo.echo_)  # эхо последнее


async def set_commands(dp: Dispatcher):
    """Регистрация команд."""
    all_commands = [
        start.start_,
        help.help_,
    ]

    await dp.bot.set_my_commands(
        [
            BotCommand(
                command=f"/{func.__name__[:-1]}",
                description=func.__doc__,
            )
            for func in all_commands
        ]
    )
