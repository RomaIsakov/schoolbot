from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import info, news, requests, vote

token = '5480170349:AAG_rSDagUJ53QFpBPveZIw5YR6GhsogdCg'

bot = Bot(token=token)
dp = Dispatcher(bot)

"""@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Бот школы 334, который поможет узнать информацию о школе, оставить отзыв/предложение, узнать новости и принять участие в голосованиях. Но пока я эхо-бот!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
"""
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Я бот школы 334, который поможет узнать информацию о школе, оставить отзыв/предложение, узнать новости и принять участие в голосованиях")
@dp.message_handler(commands=['info'])
async def process_info_command(message: types.Message):
    await message.reply("Школа 334...") #написать!
@dp.message_handler(commands=['requests'])
async def process_requests_command(message: types.Message):
    await message.reply("Вы хотите оставить жалобу или предложение?")
    await message.answer("req - чтобы оставить предложение \ncomp - чтобы оставить жалобу")
    @dp.message_handler(commands=['req'])
    async def process_req_command(message: types.Message):
        await message.answer("Напишите своё предложение")
    @dp.message_handler(commands=['comp'])
    async def process_comp_command(message: types.Message):
        await message.answer("Напишите свою жалобу")
        await message.answer("Вы хотите оставить жалобу или предложение?")
@dp.message_handler(commands=['voting'])
async def process_voting_command(message: types.Message):
    await message.reply("Выберите в какои голосовании вы хотите учавствовать или начните своё!")
@dp.message_handler(commands=['news'])
async def process_news_command(message: types.Message):
    await message.reply("Список актуальных новостей:")
if __name__ == '__main__':
    executor.start_polling(dp)


# функционал / ssh ключ