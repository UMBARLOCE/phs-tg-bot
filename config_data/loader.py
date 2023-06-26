from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config_data.config import TG_BOT_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
bot = Bot(TG_BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
