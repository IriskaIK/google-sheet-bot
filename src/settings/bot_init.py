from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import psycopg2


conn = psycopg2.connect(dbname='SheetBot', user='postgres', 
                        password='8339', host='localhost', port=5432)


BOT_TOKEN = '5931024328:AAF816RwpQ9u6bIRTF1A9Qiegyi3pV_I2kk'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())