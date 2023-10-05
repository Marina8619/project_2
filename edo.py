import os
from docx import Document
import openpyxl

str1 = 'Продажа, Приемка_товара, Перемещение, Списание_товара'


def generation_Word(type_oper, bd_index):
    document = Document()
    if os.path.exists(f'documents\{type_oper}'):
        print("Указанный файл существует")
        document.save(f'documents\{type_oper}\{type_oper}_{bd_index}.docx')
        os.startfile(f'documents\{type_oper}\{type_oper}_{bd_index}.docx', 'open')
    else:
        print("Файл не существует")
        os.mkdir(f'documents\{type_oper}')
        document.save(f'documents\{type_oper}\{type_oper}_{bd_index}.docx')
        os.startfile(f'documents\{type_oper}\{type_oper}_{bd_index}.docx', 'open')


# generation_Word('Приемка_товара', 5)

def generation_Excel(type_oper, bd_index):
    wb = openpyxl.Workbook()
    if os.path.exists(f'documents\{type_oper}'):
        wb.create_sheet(title=f'{type_oper}', index=0)
        wb.remove(wb['Sheet'])
        # sheet = wb[f'{type_oper}']
        print("Указанный файл существует")
        wb.save(f'documents\{type_oper}\{type_oper}_{bd_index}.xlsx')
        os.startfile(f'documents\{type_oper}\{type_oper}_{bd_index}.xlsx', 'open')
    else:
        print("Файл не существует")
        os.mkdir(f'documents\{type_oper}')
        wb.create_sheet(title=f'{type_oper}', index=0)
        wb.remove(wb['Sheet'])
        wb.save(f'documents\{type_oper}\{type_oper}_{bd_index}.docx')
        os.startfile(f'documents\{type_oper}\{type_oper}_{bd_index}.docx', 'open')


generation_Excel('Приемка_товара', 4)