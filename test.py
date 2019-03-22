import openpyxl
from collections import OrderedDict


excel_doc = openpyxl.load_workbook('table.xlsx')
sheet_to_work = excel_doc.get_sheet_by_name('Sheet1')

def get_kolichestvo_otdelov(sheet_to_work, column):
    for i in range(ord('A'), ord('Z')+1):
        if sheet_to_work['{}1'.format(chr(i))].value == column:
            row = chr(i)
    otdel_list = []
    i = 2
    while True:
        otdel_list.append(sheet_to_work['{}{}'.format(row, i)].value)
        i+= 1
        if sheet_to_work['{}{}'.format(row, i)].value == None:
            break
    return len(otdel_list)

print(get_kolichestvo_otdelov(sheet_to_work, 'Otdel'))

def max_column(sheet_to_work, column):
    '''Определяет макс в колонке, в какой передаем аргументом. У нас salary'''
    for i in range(ord('A'), ord('Z')+1):
        if sheet_to_work['{}1'.format(chr(i))].value == column:
            row = chr(i)
    column_list = []
    i = 2
    while True:
        column_list.append(sheet_to_work['{}{}'.format(row, i)].value)
        i+= 1
        if sheet_to_work['{}{}'.format(row, i)].value == None:
            break
    return max(column_list)

print(max_column(sheet_to_work, 'Salary'))

def max_sal_otdel(sheet_to_work, estim_column, ref_column):
    '''В каком отделе макс зарплата, сделал по ошибке:('''
    max_sal = max_column(sheet_to_work, estim_column)
    for i in range(ord('A'), ord('Z')+1):
        if sheet_to_work['{}1'.format(chr(i))].value == ref_column:
            row = i
    i = 2
    while True:
        otdel = sheet_to_work['{}{}'.format(chr(row), i)].value
        if sheet_to_work['{}{}'.format(chr(row+1), i)].value == max_sal:
            return otdel
            break
        elif otdel == None:
            return f'No {ref_column} with max {estim_column} was found'
            break
        else:
            i+= 1

print(max_sal_otdel(sheet_to_work, 'Salary', 'Otdel'))

def max_sal_v_each_otdele(sheet_to_work, column):
    '''Определeние максимальную зарплату в каждом отделе'''
    for i in range(ord('A'), ord('Z') + 1):
        if sheet_to_work['{}1'.format(chr(i))].value == column:
            row = i
    otdel_list = []
    i = 2
    while True:
        otdel_list.append(sheet_to_work['{}{}'.format(chr(row), i)].value)
        i += 1
        if sheet_to_work['{}{}'.format(chr(row), i)].value == None:
            break
    n = 2
    otdel_dict = OrderedDict.fromkeys(otdel_list)

    for i in otdel_dict:
        if otdel_dict[i]== None:
            otdel_dict[i] = sheet_to_work['{}{}'.format(chr(row + 1), n)].value
        elif otdel_dict[i] != None:
            if otdel_dict[i] >= sheet_to_work['{}{}'.format(chr(row + 1), n)].value:
                continue
            else:
                otdel_dict[i] = sheet_to_work['{}{}'.format(chr(row + 1), n)].value
        n+= 1
    return otdel_dict

print(max_sal_v_each_otdele(sheet_to_work, 'Otdel'))
