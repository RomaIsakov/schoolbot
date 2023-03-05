from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BotToken
from aiogram.dispatcher import Dispatcher

storage = MemoryStorage()
bot = Bot(BotToken)
dp = Dispatcher(bot, storage=storage)
