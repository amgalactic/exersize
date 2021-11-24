import csv
from os import system, name
import pandas as pd
from tabulate import tabulate


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def pretty_print(data):
    print(tabulate(data, headers='key', tablefmt='psql'))


def operate_excel(excel_to_open):
    xl = pd.ExcelFile(excel_to_open)
    number_of_sheets = len(xl.sheet_names)

    if number_of_sheets > 1:
        clear()

        while True:
            print(f'There is {number_of_sheets} sheets:')

            for i, sheet in enumerate(xl.sheet_names, start=1):
                print(f'{i} {sheet}')

            len_of_sheet_list = len(xl.sheet_names)
            print(f'{len_of_sheet_list + 1} all sheets')
            print(f'{len_of_sheet_list + 2} back')
            sheet_choice = input(f'\nWhich one do you want to see? \n')

            try:
                clear()

                if int(sheet_choice) == len_of_sheet_list + 1:
                    data_df = pd.read_excel(excel_to_open, sheet_name=None)
                    pretty_print(data_df)

                elif int(sheet_choice) == len_of_sheet_list + 2:
                    break

                data_df = pd.read_excel(excel_to_open, sheet_name=xl.sheet_names[int(sheet_choice) - 1])
                pretty_print(data_df)

            except ValueError:
                print('Incorrect value! Try again')

            except IndexError:
                print('Option is out of range. Try again')

    else:
        data_df = pd.read_excel(excel_to_open)
        pretty_print(data_df)


def operate_json(json_to_open):
    clear()
    data_df = pd.read_json(json_to_open)
    pretty_print(data_df)


def operate_csv(csv_to_open):
    clear()
    with open(csv_to_open) as csv_file:
        columns = list(csv.reader(csv_file, delimiter=';'))
        pretty_print(columns)


def main(path_to_file):
    clear()
    extension = path_to_file.strip().split('.')[-1]

    if extension == 'json':
        operate_json(path_to_file.strip())

    if extension == 'csv':
        operate_csv(path_to_file.strip())

    if extension == 'xlsx' or extension == 'xls':
        operate_excel(path_to_file.strip())


while True:
    clear()
    user_filepath = input('''Enter the path to open file (csv, xlsx, json)
For exit, type 'exit'
Path to file: ''')

    if user_filepath.strip().lower() == 'exit':
        break

    main(user_filepath)