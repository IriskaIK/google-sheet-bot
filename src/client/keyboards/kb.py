from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

StartBtn = KeyboardButton('Розпочати✅')



continueBtn = KeyboardButton('Продовжити✅')
readyBtn = KeyboardButton('Готово✅')

saveBtn = KeyboardButton('Зберегти📝')
deleteBtn = KeyboardButton('Видалити🗑')
addBtn = KeyboardButton('Додати➕')

helpbtn = KeyboardButton('Допомога❔')
addColumn = KeyboardButton('Додати нову колонку🗂')
addValue = KeyboardButton('Внести нові дані📝')


openWorkSheet = KeyboardButton('Відкрити існуючий аркуш📂')
createWorkSheet = KeyboardButton('Створити новий аркуш📎')


backToActions = KeyboardButton('Повернутись⬅️')

continueColumnBtn = KeyboardButton('Додати нову колонку🗂')
endBtn = KeyboardButton('Закінчити📎')
endRowBtn = KeyboardButton('Закінчити внесення даних📎')


continue_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(continueBtn)
ready_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(readyBtn)


work_sheets_action_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(openWorkSheet, createWorkSheet)
create_workSheet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(createWorkSheet)

column_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(continueColumnBtn, endBtn)
row_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True).add(addValue, endRowBtn)

row_end_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True).add(endRowBtn)


actions_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(helpbtn)
actions_kb.row(addColumn, addValue)


start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(StartBtn)

back_to_actions = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(backToActions)