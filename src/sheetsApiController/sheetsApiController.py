import gspread



class sheetsApiController():
    def __init__(self, sheetFileUrl) -> None:  
        self.gc = gspread.service_account(filename="src\sheetsApiController\credential.json")
        self.sh = self.gc.open_by_url(sheetFileUrl)
        self.wks = None
        self.sheet_url = sheetFileUrl
        self.wks_name = None



    def getAllSheets(self):
        return self.gc.list_spreadsheet_files()


    def getSheetName(self) -> str:
        return self.sh.title
    
    

    def openWorkSheet(self, workSheetName):
        self.wks_name = workSheetName
        self.wks = self.sh.worksheet(workSheetName)

    def CreateNewWorkSheet(self, name):
        self.wks_name = name
        self.sh.add_worksheet(title=name, rows=1000, cols=26)
        self.wks = self.sh.worksheet(name)

    def getAllWorkSheets(self):
        try:
            return self.sh.worksheets()
        except:
            print('something went wrong, try again')



    def changeWorkSheet(self, name):
        try:
            self.sh.worksheet(name)
        except:
            print('something went wrong, try again')

    def getAllRecordsInSheet(self):
        try:
            return self.wks.get_all_records()
        except:
            print('something went wrong, try again')


    def getFirstRow(self):
        values_list = self.wks.row_values(1)
        return values_list
        
        
    def addDataToSheet(self, data:list):
        self.wks.append_row(data)
        return

    

    def getDataFromCells(self, cell_range):
        try:
            return self.wks.get(cell_range)
        except:
            print('something went wrong, try again')


    def putDataInCells(self, row, column , value):
        try:
            self.wks.update_cell(row, column, value)
        except:
            print('something went wrong, try again')







# some = sheetsApiController('https://docs.google.com/spreadsheets/d/1WYDQ-G0HkbMsViZfYLJ6eABxPUGAI15Rfo-mIKDgTv8/edit#gid=0')
# some.openWorkSheet('Аркуш1')

 