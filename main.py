# Import the necessary handlers and the dispatcher
from aiogram.utils import executor
from packages.requests import handlers as req_handlers
from packages.client import handlers as client_handlers
from packages.news import handlers as news_handlers
from packages.voting import handlers as voting_handlers
from bot import dp
from packages.client.states import ClientStatesGroup

# Register message handlers for the requests and complaints commands
dp.register_message_handler(req_handlers.process_requests_command, commands=["requests"])
dp.register_callback_query_handler(req_handlers.vote_callback)
dp.register_message_handler(req_handlers.process_req_command, state=ClientStatesGroup.req)
dp.register_callback_query_handler(req_handlers.request_callback, state=ClientStatesGroup.req)
dp.register_message_handler(req_handlers.process_com_command, state=ClientStatesGroup.comp)
dp.register_callback_query_handler(req_handlers.complaint_callback, state=ClientStatesGroup.comp)

# Register message handlers for the start and info commands
dp.register_message_handler(client_handlers.process_start_command, commands=["start"])
dp.register_message_handler(client_handlers.process_info_command, commands=["info"])

# Register message handlers for the news and voting commands
dp.register_message_handler(news_handlers.process_news_command, commands=["news"])
dp.register_message_handler(voting_handlers.process_voting_command, commands=["voting"])

# Start the bots polling loop
if __name__ == '__main__':
    executor.start_polling(dp)
