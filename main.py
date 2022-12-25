from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
import config

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


@dp.message_handler(commands=['requests'], state=None)
async def process_requests_command(message: types.Message):
    await message.reply("Вы хотите оставить жалобу или предложение?")
    await message.answer("/req - чтобы оставить предложение \n/comp - чтобы оставить жалобу")
    await ClientStatesGroup.requests.set()


@dp.message_handler(commands=['req'], state=ClientStatesGroup.requests)
async def process_req_command(message: types.Message):
    await message.answer("Напишите своё предложение")
    await ClientStatesGroup.req.set()


@dp.message_handler(commands=['comp'], state=ClientStatesGroup.requests)
async def process_comp_command(message: types.Message):
    await message.answer("Напишите свою жалобу")
    await ClientStatesGroup.comp.set()


@dp.message_handler(state=ClientStatesGroup.req)
async def process_req_command(message: types.Message, state: FSMContext):
    await message.answer("Предложение сохранено!")
    await state.finish()


@dp.message_handler(state=ClientStatesGroup.comp)
async def process_req_command(message: types.Message, state: FSMContext):
    await message.answer("Жалоба сохранена!")
    await state.finish()


@dp.message_handler(commands=['voting'])
async def process_voting_command(message: types.Message):
    await message.reply("Выберите в какои голосовании вы хотите учавствовать или начните своё!")


@dp.message_handler(commands=['news'])
async def process_news_command(message: types.Message):
    await message.reply("Список актуальных новостей:")


@dp.message_handler(commands=['cancel'])
async def cancel_state(message: types.Message, state: FSMContext):
    cur_state = state.get_state()
    await message.answer("otmena")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp)

# РАСКИДАТЬ ПО ФАЙЛИКАМ!!
