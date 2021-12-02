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
    print(tabulate(data, headers='keys', tablefmt='psql'))


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
            print(f'{len_of_sheet_list + 1} back')
            sheet_choice = input(f'\nWhich one do you want to see? \n')

            try:
                clear()

                if int(sheet_choice) == len_of_sheet_list + 1:
                    break

                data_df = pd.read_excel(excel_to_open, sheet_name=xl.sheet_names[int(sheet_choice) - 1])
                pretty_print(data_df)
                input('Press "Enter" to continiue')
                clear()

            except ValueError:
                print('Incorrect value! Try again')

            except IndexError:
                print('Option is out of range. Try again')

    else:
        data_df = pd.read_excel(excel_to_open)
        pretty_print(data_df)
        input('Press "Enter" to continiue')
        clear()


def operate_json(json_to_open):
    clear()
    data_df = pd.read_json(json_to_open)
    pretty_print(data_df)
    input('Press "Enter" to continiue')
    clear()


def operate_csv(csv_to_open):
    clear()
    with open(csv_to_open) as csv_file:
        columns = list(csv.reader(csv_file, delimiter=';'))
        pretty_print(columns)
    input('Press "Enter" to continiue')
    clear()
