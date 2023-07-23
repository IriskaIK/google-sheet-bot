from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import psycopg2


conn = psycopg2.connect(dbname='', user='', 
                        password='', host='', port=)


BOT_TOKEN = ''

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
