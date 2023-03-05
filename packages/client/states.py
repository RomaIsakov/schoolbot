"""
This module defines the ClientStatesGroup states group using the StatesGroup class

ClientStatesGroup defines the following states:

requests: A state for managing requests'
desc: A state for managing bot description
vote: A state for managing voting
news: A state for managing school news
req: A state for managing requests
comp: A state for managing complaints
"""
from aiogram.dispatcher.filters.state import StatesGroup, State


class ClientStatesGroup(StatesGroup):
    requests = State()
    desc = State()
    vote = State()
    news = State()
    req = State()
    comp = State()
