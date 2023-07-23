from aiogram import Dispatcher
from client import client, state


def register_handlers_client(dp: Dispatcher):
      #basic handlers
      dp.register_message_handler(client.start, commands='start')
      dp.register_message_handler(client.addSheet, state=client.Form.wait_for_continue, text ='Продовжити✅')
      dp.register_message_handler(client.addSheetURL, state=client.Form.wait_for_ready, text = 'Готово✅')
      dp.register_message_handler(client.checkSheetConn, state=client.Form.wait_for_sheet_url)
      
      dp.register_message_handler(client.openWorkSheet, state=client.Form.openWorkSheet, text = 'Відкрити існуючий аркуш📂')
      dp.register_message_handler(client.addWorkSheet, state=client.Form.openWorkSheet, text = 'Створити новий аркуш📎')
      
      dp.register_message_handler(client.checkWorkSheet, state=client.Form.waiting_for_worksheet)
      dp.register_message_handler(client.createWorkSheet, state=client.Form.waiting_for_creating_worksheet)
      
      dp.register_message_handler(client.getHelp, state=client.Form.default, text = 'Допомога❔')
      dp.register_message_handler(client.actionMenu, state=client.Form.wait_for_back)
      
      dp.register_message_handler(client.addColumn, state=client.Form.default, text = 'Додати нову колонку🗂')
      dp.register_message_handler(client.processColumn, state=client.Form.waiting_for_column)
      dp.register_message_handler(client.checkColumns, state=client.Form.default, text = 'Закінчити📎')
      
      dp.register_message_handler(client.addRow, state=client.Form.default, text = 'Внести нові дані📝')
      dp.register_message_handler(client.processRowElement, state=client.Form.waiting_for_row)
      dp.register_message_handler(client.checkRows, state=client.Form.default, text = 'Закінчити внесення даних📎')


      