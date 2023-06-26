from aiogram.utils import executor
from aiogram import Dispatcher
from config_data.loader import dp
from config_data.registrar import set_handlers, set_commands

# from database.sq_db import create_table


async def on_startup(_):
    """Выполняется один раз при включении."""
    # create_table()
    set_handlers(dp)
    await set_commands(dp)
    print("Бот он-лайн")


async def on_shutdown(dp: Dispatcher):
    """Запускается один раз при выключении."""
    await dp.storage.close()
    await dp.storage.wait_closed()
    print("Бот офф-лайн")


if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
    )
