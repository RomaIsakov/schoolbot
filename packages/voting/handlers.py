from aiogram import types


async def process_voting_command(message: types.Message):
    await message.reply("Список опросов вы можете найти в информационном канале школы 334:\nhttps://t.me/+tdHLw5XZYI80M2Ni")