from aiogram.utils import executor
from handlers import handlers
from settings.bot_init import dp



handlers.register_handlers_client(dp)
executor.start_polling(dp, skip_updates = True)
