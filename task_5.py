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
    return len(list(set(otdel_list)))

print('Kolichestvo otdelov: {}'.format(get_kolichestvo_otdelov(sheet_to_work, 'Otdel')))

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

print('Max salary is: {}'.format(max_column(sheet_to_work, 'Salary')))

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
    otdel_dict = OrderedDict.fromkeys(otdel_list)


    for k in otdel_dict:
        i = 2
        max_sal = 0
        while True:
            temp_sal = sheet_to_work['{}{}'.format(chr(row + 1), i)].value
            if temp_sal == None:
                break
            key = sheet_to_work['{}{}'.format(chr(row), i)].value
            if temp_sal > max_sal and key == k:
                otdel_dict[k] = temp_sal
                max_sal = temp_sal
            i += 1
    return otdel_dict

print(max_sal_v_each_otdele(sheet_to_work, 'Otdel'))

def otdel_maxsal_surname_vfile(sheet_to_work, column):
    max_salary = max_column(sheet_to_work, column)
    for i in range(ord('A'), ord('Z') + 1):
        if sheet_to_work['{}1'.format(chr(i))].value == column:
            row = i
    i = 2
    while True:
        temp_sal = sheet_to_work['{}{}'.format(chr(row), i)].value
        if temp_sal == max_salary:
            otdel = sheet_to_work['{}{}'.format(chr(row-1), i)].value
            surname = sheet_to_work['{}{}'.format(chr(row-3), i)].value
            with open('otdel_maxsal_surname.txt', 'w') as output_file:
                output_file.write('Result: {}, {}, {}'.format(otdel, temp_sal, surname))
                print(' Info was written successfully')
                break
        i += 1

otdel_maxsal_surname_vfile(sheet_to_work, 'Salary')


