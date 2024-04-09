# W_R_Excel.py

import openpyxl
from datetime import datetime

def add_rent_entry(tenant, entry_type, amount, description):
    file_path = 'finances.xlsx'
    wb = openpyxl.load_workbook(file_path)
    sheet = wb['Rent']

    # Добавляем новую запись в конец
    new_row = sheet.max_row + 1
    sheet[f'A{new_row}'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sheet[f'B{new_row}'] = tenant
    sheet[f'C{new_row}'] = entry_type
    sheet[f'D{new_row}'] = amount
    sheet[f'E{new_row}'] = description

    wb.save(file_path)
    wb.close()
