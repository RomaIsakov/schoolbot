from aiogram import types
from aiogram.dispatcher import FSMContext
import pandas as pd
from bot import bot
from packages.client.states import ClientStatesGroup
from config import complaints_dir, requests_dir
from packages.client import keyboards


async def process_requests_command(message: types.Message):
    """
    This function is called when the user sends the "/requests" command.
    It creates a keyboard with options to leave a complaint or suggestion.
    """
    kb = keyboards.create_requests_keyboard()
    await message.reply("Вы хотите оставить жалобу или предложение?", reply_markup=kb)


async def vote_callback(call_back: types.CallbackQuery, state: FSMContext):
    """
    This function is called when the user selects an option on the requests keyboard.
    It handles the user's selection by setting the appropriate state and sending a message
    prompting the user to enter their complaint or suggestion.
    """
    await bot.edit_message_reply_markup(
        chat_id=call_back.from_user.id,
        message_id=call_back.message.message_id,
        reply_markup=None)
    if call_back.data == 'req':
        # Set the state to "req" to handle the user's suggestion
        await ClientStatesGroup.req.set()
        return await call_back.message.answer("Напишите своё предложение")
    if call_back.data == 'comp':
        # Set the state to "comp" to handle the user's complaint
        await ClientStatesGroup.comp.set()
        return await call_back.message.answer("Напишите свою жалобу")
    if call_back.data == 'cancel':
        # Cancel the user's input and finish the state
        await state.finish()
        return await call_back.message.answer("Отменено")


async def process_req_command(message: types.Message):
    """
    This function is called when the user enters a suggestion.
    It displays the user's suggestion and provides a keyboard with options to approve or edit it.
    """
    text = "Ваше предложение: \n" + message.text
    kb = keyboards.create_process_req_keyboard()
    await message.answer(text, reply_markup=kb)


async def request_callback(call_back: types.CallbackQuery, state: FSMContext):
    """
    This function is called when the user selects an option on the suggestion keyboard.
    It handles the user's selection by saving or discarding the suggestion and sending a
    confirmation message to the user.
    """
    await bot.edit_message_reply_markup(
        chat_id=call_back.from_user.id,
        message_id=call_back.message.message_id,
        reply_markup=None)
    if call_back.data == 'ok':
        # Save the suggestion
        await state.finish()
        text = call_back.message.text

        df = pd.read_csv(requests_dir, index_col=0)
        df.loc[len(df.index)] = [call_back.message.message_id, call_back.from_user.id, call_back.message.date,
                                 text[19:]]
        df.to_csv(requests_dir)
        return await call_back.message.answer("Ваше предложение сохранено!")
    if call_back.data == 'notok':
        # Discard the suggestion
        await state.finish()
        return await call_back.message.answer("Предложение удалено!")
    if call_back.data == 'edit':
        # Prompt the user to edit their suggestion
        return await call_back.message.answer("Напишите изменённое предложение:")


async def process_com_command(message: types.Message):
    """
    This function is called when the user enters a complaint.
    It displays the user's complaint and provides a keyboard with options to approve or edit it.
    """
    text = "Ваша жалоба: \n" + message.text
    kb = keyboards.create_process_req_keyboard()
    await message.answer(text, reply_markup=kb)


async def complaint_callback(call_back: types.CallbackQuery, state: FSMContext):
    """
    This function is called when the user selects an option on the complaint keyboard.
    It handles the user's selection by saving or discarding the complaint and sending a
    confirmation message to the user.
    """
    await bot.edit_message_reply_markup(
        chat_id=call_back.from_user.id,
        message_id=call_back.message.message_id,
        reply_markup=None)
    if call_back.data == 'ok':
        # Save the complaint
        await state.finish()
        text = call_back.message.text

        df = pd.read_csv(complaints_dir, index_col=0)
        df.loc[len(df.index)] = [call_back.message.message_id, call_back.from_user.id, call_back.message.date,
                                 text[14:], "Жалоба принята, ждёт рассмотрения"]
        df.to_csv(complaints_dir)
        return await call_back.message.answer("Ваша жалоба сохранена!")

    if call_back.data == 'notok':
        # Discard the complaint
        await state.finish()
        return await call_back.message.answer("Жалоба удалена!")
    if call_back.data == 'edit':
        # Prompt the user to edit their complaint
        return await call_back.message.answer("Напишите изменённую жалобу:")

async def process_com_command(message: types.Message):
    """
    This function is called when the user enters a complaint.
    It displays the user's complaint and provides a keyboard with options to approve or edit it.
    """
    text = "Ваша жалоба: \n" + message.text
    kb = keyboards.create_process_req_keyboard()
    await message.answer(text, reply_markup=kb)