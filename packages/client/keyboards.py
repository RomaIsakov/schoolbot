from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Function for creating the requests keyboard
def create_requests_keyboard():
    """
    Create an inline keyboard with options for submitting a request or complaint, or cancelling the operation.
    Returns:
    InlineKeyboardMarkup: The created inline keyboard.
    """
    kb = InlineKeyboardMarkup(row_width=2)
    req_button = InlineKeyboardButton(text="Предложение", callback_data="req")
    comp_button = InlineKeyboardButton(text="Жалоба", callback_data="comp")
    cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
    kb.add(req_button, comp_button, cancel_button)
    return kb


# Function for creating the process request keyboard
def create_process_req_keyboard():
    """
    Create an inline keyboard with options for approving, deleting, or editing a request or complaint.
    Returns:
        InlineKeyboardMarkup: The created inline keyboard.
    """
    kb = InlineKeyboardMarkup(row_width=3)
    ok_button = InlineKeyboardButton(text="Сохранить", callback_data="ok")
    notok_button = InlineKeyboardButton(text="Удалить", callback_data="notok")
    edit_button = InlineKeyboardButton(text="Изменить", callback_data="edit")
    kb.add(ok_button, notok_button, edit_button)
    return kb


# Function for creating the requests keyboard
def create_selection_keyboard():
    """
    Create an inline keyboard with options for submitting a request or complaint, or cancelling the operation.
    Returns:
    InlineKeyboardMarkup: The created inline keyboard.
    """
    kb = InlineKeyboardMarkup(row_width=2)
    req_button = InlineKeyboardButton(text="Оставить", callback_data="create")
    comp_button = InlineKeyboardButton(text="Посмотреть", callback_data="view")
    cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
    kb.add(req_button, comp_button, cancel_button)
    return kb
