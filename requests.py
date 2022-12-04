from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
token = '5480170349:AAG_rSDagUJ53QFpBPveZIw5YR6GhsogdCg'
async def process_requests_command(message: types.Message):
    await message.reply("Бот школы 334, который поможет узнать информацию о школе, оставить отзыв/предложение, узнать новости и принять участие в голосованиях. Но пока я эхо-бот!")