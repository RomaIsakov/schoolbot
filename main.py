from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
import config
import pandas
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

storage = MemoryStorage()
bot = Bot(token=config.BotToken)
dp = Dispatcher(bot, storage=storage)


class ClientStatesGroup(StatesGroup):
    requests = State()
    desc = State()
    vote = State()
    req = State()
    comp = State()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(
        "Я бот школы 334, который поможет узнать информацию о школе, оставить отзыв/предложение, узнать новости и принять участие в голосованиях")


@dp.message_handler(commands=['info'])
async def process_info_command(message: types.Message):
    await message.reply("Школа 334...")  # написать!


# Requests and complains
@dp.message_handler(commands=['requests'], state=None)
async def process_requests_command(message: types.Message):
    keyBoard = InlineKeyboardMarkup(row_width=2)
    req_button = InlineKeyboardButton(text="Предложение", callback_data="req")
    comp_button = InlineKeyboardButton(text="Жалоба", callback_data="comp")
    cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
    keyBoard.add(req_button, comp_button, cancel_button)

    await message.reply("Вы хотите оставить жалобу или предложение?", reply_markup=keyBoard)


@dp.callback_query_handler()
async def vote_callback(call_back: types.CallbackQuery, state: FSMContext):
    await bot.edit_message_reply_markup(
        chat_id=call_back.from_user.id,
        message_id=call_back.message.message_id,
        reply_markup=None)
    if call_back.data == 'req':
        await ClientStatesGroup.req.set()
        return await call_back.message.answer("Напишите своё предложение")
    if call_back.data == 'comp':
        await ClientStatesGroup.comp.set()
        return await call_back.message.answer("Напишите свою жалобу")
    if call_back.data == 'cancel':
        await state.finish()
        return await call_back.message.answer("Отменено")


@dp.message_handler(state=ClientStatesGroup.req)
async def process_req_command(message: types.Message, state: FSMContext):
    text = "Ваше предложение: \n" + message.text
    keyBoard = InlineKeyboardMarkup(row_width=3)
    ok_button = InlineKeyboardButton(text="Сохранить", callback_data="ok")
    notok_button = InlineKeyboardButton(text="Удалить", callback_data="notok")
    edit_button = InlineKeyboardButton(text="Изменить", callback_data="edit")
    keyBoard.add(ok_button, notok_button, edit_button)

    await message.answer(text, reply_markup=keyBoard)


@dp.callback_query_handler(state=ClientStatesGroup.req)
async def vote_callback(call_back: types.CallbackQuery, state: FSMContext):
    await bot.edit_message_reply_markup(
        chat_id=call_back.from_user.id,
        message_id=call_back.message.message_id,
        reply_markup=None)
    if call_back.data == 'ok':
        await state.finish()
        return await call_back.message.answer("Ваше предложение сохранено!")
    if call_back.data == 'notok':
        await state.finish()
        return await call_back.message.answer("Предложение удалено!")
    if call_back.data == 'edit':
        await state.finish()
        return await call_back.message.answer("")


@dp.message_handler(state=ClientStatesGroup.comp)
async def process_req_command(message: types.Message, state: FSMContext):
    text = "Ваша жалоба: \n" + message.text
    keyBoard = InlineKeyboardMarkup(row_width=3)
    ok_button = InlineKeyboardButton(text="Сохранить", callback_data="ok")
    notok_button = InlineKeyboardButton(text="Удалить", callback_data="notok")
    edit_button = InlineKeyboardButton(text="Изменить", callback_data="edit")
    keyBoard.add(ok_button, notok_button, edit_button)

    await message.answer(text, reply_markup=keyBoard)


@dp.callback_query_handler(state=ClientStatesGroup.comp)
async def vote_callback(call_back: types.CallbackQuery, state: FSMContext):
    await bot.edit_message_reply_markup(
        chat_id=call_back.from_user.id,
        message_id=call_back.message.message_id,
        reply_markup=None)
    if call_back.data == 'ok':
        await state.finish()
        text = call_back.message.text
        dataFrame=pandas.read_csv("complains.csv")
        dataFrame = dataFrame.append(pandas.Series([call_back.message.message_id, call_back.message.date, text[14:]], index=dataFrame.columns[:len([call_back.message.message_id, call_back.message.date, text[14:]])]), ignore_index=1)
        dataFrame.to_csv("complains.csv")
        return await call_back.message.answer("Ваша жалоба сохранена!")

    if call_back.data == 'notok':
        await state.finish()
        return await call_back.message.answer("Жалоба удалена!")
    if call_back.data == 'edit':    
        return await call_back.message.answer("Напишите изменённую жалобу:")


@dp.message_handler(commands=['voting'])
async def process_voting_command(message: types.Message):
    await message.reply("Выберите в какои голосовании вы хотите учавствовать или начните своё!")


@dp.message_handler(commands=['news'])
async def process_news_command(message: types.Message):
    await message.reply("Список актуальных новостей:")


if __name__ == '__main__':
    executor.start_polling(dp)

# РАСКИДАТЬ ПО ФАЙЛИКАМ!!
