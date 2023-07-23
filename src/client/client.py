from aiogram import types
from aiogram.dispatcher import filters

from settings.bot_init import bot
from .keyboards import kb


from aiogram.dispatcher import FSMContext
from .state import *
from .MessageGenerators.generateResponse import generate_response


from sheetsApiController.sheetsApiController import sheetsApiController
from dbController.pgdb import *



async def start(message: types.Message, state: FSMContext):
    
    
    user = get_user(message.from_user.id)
    if user:
        try:
            sc = sheetsApiController(user[0][3])
            await state.update_data(current_table_url = user[0][3])
            await state.update_data(current_sc = sc)


        except:
            await bot.send_message(message.from_user.id, 'Неможливо приєднатись до сервера. Перевірте правильність URL і спробуйте ввести його пізніше')
            return
        
        
        await state.set_state(Form.wait_for_sheet_url)
        
        await bot.send_message(message.from_user.id, 'Почнімо?', reply_markup=kb.start_kb)

        
    else:
        await bot.send_message(message.from_user.id, 'Привіт, я бот, який допоможе вам працювати з google таблицями, не відкриваючи їх.\n Для початку треба буде додати мене до вашої google таблиці.\n\n Якщо готові почати, тисніть "Продовжити✅"', reply_markup=kb.continue_kb)
        await state.set_state(Form.wait_for_continue)
    
    


async def addSheet(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Щоб використовувати мене, потрібно створити нову google таблицю. Натиснути "Поділитися файлом" та ввести туди мою пошту: google-sheet-bot@academic-emblem-393016.iam.gserviceaccount.com\n\nПісля того, як виконаєте це, натисніть "Готово✅"', reply_markup=kb.ready_kb)
    await state.set_state(Form.wait_for_ready)


async def addSheetURL(message: types.Message, state : FSMContext):
    await bot.send_message(message.from_user.id, 'Чудово! Давайте перевіримо, чи бачу я вашу таблицю. \nВведіть URL вашої таблиці:')
    await state.set_state(Form.wait_for_sheet_url)
    

async def checkSheetConn(message:types.Message, state : FSMContext):
    user_info= create_user(message.from_user.username, message.from_user.id, message.text)
    
    if user_info == True:           
        try:
            sc = sheetsApiController(message.text)
        except:
            await bot.send_message(message.from_user.id, 'Неможливо приєднатись до сервера. Перевірте правильність URL і спробуйте ввести його пізніше')
            return
        
        await state.update_data(current_sc = sc)
        await state.update_data(current_table_url = message.text)
        
    else:
        sc = sheetsApiController(user_info[0][3])

    await state.set_state(Form.openWorkSheet)
    await bot.send_message(message.from_user.id, f'Ваша таблиця ({sc.getSheetName()}) успішно відкрита. Ви можете почати працювати з нею використовуючи кнопки знизу.', reply_markup=kb.work_sheets_action_kb)
    
    


async def openWorkSheet(message:types.Message, state:FSMContext):
    
    await state.set_state(Form.waiting_for_worksheet)
    await bot.send_message(message.from_user.id, 'Введіть назву аркуша: ')

async def addWorkSheet(message:types.Message, state:FSMContext):
    await state.set_state(Form.waiting_for_creating_worksheet)
    await bot.send_message(message.from_user.id, 'Введіть назву нового аркуша: ')


async def createWorkSheet(message:types.Message, state: FSMContext):
    data = await state.get_data('current_table_url')
    url = data.get('current_table_url')
    
    try:
        sc = sheetsApiController(url)
        sc.CreateNewWorkSheet(message.text)
        sc.wks.client.session.close()
    except:
        await state.set_state(Form.openWorkSheet)
        await bot.send_message(message.from_user.id, 'Щось пішло не так. Спробуйте пізніше', reply_markup=kb.work_sheets_action_kb)
        return
        
    await state.set_state(Form.default)
    
    await state.update_data(current_work_sheet_name = message.text)
    await state.update_data(current_sc = sc)
    
    await bot.send_message(message.from_user.id, f'Відкрито аркуш:{message.text}', reply_markup=kb.actions_kb)

        
async def checkWorkSheet(message:types.Message, state:FSMContext):
    data = await state.get_data('current_table_url')
    url = data.get('current_table_url')
    
    
    try:
        sc = sheetsApiController(url)
        sc.openWorkSheet(message.text)
        first_row = sc.getFirstRow()
        await state.update_data(columns=first_row) 
        sc.wks.client.session.close()
    except:
        await state.set_state(Form.openWorkSheet)
        await bot.send_message(message.from_user.id, 'Аркуш не знайдено. Спробуйте ще раз', reply_markup=kb.work_sheets_action_kb)
        return
    
    await state.set_state(Form.default)
    
    await state.update_data(current_work_sheet_name = message.text)
    await state.update_data(current_sc = sc)

    await bot.send_message(message.from_user.id, f'Відкрито аркуш:{message.text}', reply_markup=kb.actions_kb)
    


    
async def actionMenu(message:types.Message, state:FSMContext):
    await state.set_state(Form.default)
    url = await state.get_data('current_table_url')
    worksheet = await state.get_data('current_work_sheet_name')
      
    try:
        sc = sheetsApiController(url.get('current_table_url'))
        sc.openWorkSheet(worksheet.get('current_work_sheet_name'))
        first_row = sc.getFirstRow()
        await state.update_data(columns=first_row) 
        #get values from first row and set in into state.columns
        sc.wks.client.session.close()
    except:
        await bot.send_message(message.from_user.id, f'Їбать все накрилось')

    
    
    await bot.send_message(message.from_user.id, f'Активна таблиця: {sc.getSheetName()}\n\nURL таблиці: {sc.sheet_url}\n\nАркуш: {sc.wks_name}', reply_markup=kb.actions_kb)
    
async def getHelp(message:types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id ,'some help info', reply_markup=kb.back_to_actions)
    await state.set_state(Form.wait_for_back)




async def addColumn(message:types.Message, state:FSMContext):
    await state.set_state(Form.waiting_for_column)
    await bot.send_message(message.from_user.id, 'Введіть назву нової колонки:')
    
async def processColumn(message:types.Message, state:FSMContext):
    await state.set_state(Form.default)
    data = await state.get_data('columns')
    col_arr = data.get('columns')
    
    
    if col_arr == None:
        await state.update_data(columns= [message.text])

    else:       
        col_arr.append(message.text)
        await state.update_data(columns= col_arr)
        

    print(col_arr)
    
    
    
    
    await bot.send_message(message.from_user.id, f'{message.text} збережено, продовжити створення колонок?', reply_markup=kb.column_kb)

async def checkColumns(message:types.Message, state:FSMContext):
    await state.set_state(Form.wait_for_back)
    data = await state.get_data('columns')
    col_arr = data.get('columns')
    
    url = await state.get_data('current_table_url')
    worksheet = await state.get_data('current_work_sheet_name') 
     
    sc = sheetsApiController(url.get('current_table_url'))
    sc.openWorkSheet(worksheet.get('current_work_sheet_name'))
    
    for i in range(len(col_arr)):
        sc.putDataInCells(1, i+1, col_arr[i])
    
    
    sc.wks.client.session.close()
    await bot.send_message(message.from_user.id, f'{col_arr} - додані колонки. Щоб повернутись до головного меню, натисніть на "Повернутись⬅️"', reply_markup=kb.back_to_actions)



async def addRow(message:types.Message, state:FSMContext):
    columns_data = await state.get_data('current_column_data')
    cur_column= columns_data.get('current_column_data')
    
    data = await state.get_data('columns')
    columns = data.get('columns')
    await state.set_state(Form.waiting_for_row)
    
    if cur_column == None:
        cur_column = 0
        await state.update_data(current_column_data = cur_column)
    
    
    
    
    await state.update_data(current_column_data = cur_column+1)
    if not columns:
        await bot.send_message(message.from_user.id, f'Колонки ще не створені.', reply_markup=kb.back_to_actions)   
        await state.set_state(Form.wait_for_back)
        return

    if len(columns) == cur_column:
        await bot.send_message(message.from_user.id, f'Ви ввели усі дані. Натисніть закінчити', reply_markup=kb.row_end_kb)
        await state.set_state(Form.default)
        return

    
    await bot.send_message(message.from_user.id, f'Введіть {columns[cur_column]}:')
    
async def processRowElement(message:types.Message, state:FSMContext):
    await state.set_state(Form.default)
    data = await state.get_data('row')
    row_arr = data.get('row')
    
    print(row_arr)
    if row_arr == None:
        await state.update_data(row= [message.text])

    else:       
        row_arr.append(message.text)
        await state.update_data(row= row_arr)
        
    await bot.send_message(message.from_user.id, f'{message.text} додано, продовжити додавання елементів?', reply_markup=kb.row_kb)

    print(row_arr)



async def checkRows(message:types.Message, state:FSMContext):
    await state.set_state(Form.wait_for_back)

    data = await state.get_data('row')
    row_arr = data.get('row')
    
    if not row_arr:
        await bot.send_message(message.from_user.id, 'nihya')
        return
    
    url = await state.get_data('current_table_url')
    worksheet = await state.get_data('current_work_sheet_name') 
    
    sc = sheetsApiController(url.get('current_table_url'))
    
    sc.openWorkSheet(worksheet.get('current_work_sheet_name'))
    
    sc.addDataToSheet(row_arr)
    
    await state.update_data(row = [])
    await state.update_data(current_column_data = 0)

    
    await bot.send_message(message.from_user.id, f'{row_arr} - ці дані успішно додано до таблиці. Щоб повернутись до головного меню, натисніть на "Повернутись⬅️"', reply_markup=kb.back_to_actions)
    sc.wks.client.session.close()