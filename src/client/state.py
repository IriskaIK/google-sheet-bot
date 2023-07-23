from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup



class Form(StatesGroup):
    wait_for_continue = State()
    wait_for_ready = State()
    wait_for_sheet_url = State()


    openWorkSheet = State()
    waiting_for_worksheet = State()
    waiting_for_creating_worksheet = State()
    ready_for_action = State()
    default = State()  
    wait_for_back = State()
    
    
    waiting_for_row = State()
    wait_for_row_checking = State()
    
    waiting_for_column = State()
    columns_processing = State()
    columns = []

    row = []
    current_column_data = 0
        
    current_table_url = None
    current_work_sheet_name = None
    current_sc = None




