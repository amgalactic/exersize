from os import system, name
import pandas as pd
import tabulate


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def operate_excel(file_to_open):
    xl = pd.ExcelFile(file_to_open)
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
                    data_df = pd.read_excel(file_to_open, sheet_name=None)
                    print(data_df)
                elif int(sheet_choice) == len_of_sheet_list + 2:
                    break

                data_df = pd.read_excel(file_to_open, sheet_name=xl.sheet_names[int(sheet_choice)-1])
                print(data_df)

            except ValueError:
                print('Incorrect value! Try again')

            except IndexError:
                print('Option is out of range. Try again')

    else:
        data_df = pd.read_excel(file_to_open)
        print(data_df)


def main(path_to_file):
    extension = path_to_file.strip().split('.')[-1]

    if extension == 'json':
        
        try:
            data_df = pd.read_json(path_to_file.strip())
            print(data_df)

        except ValueError:
            print('Something wrong with this json file.')

    if extension == 'csv':
        pass

    if extension == 'xlsx' or extension == 'xls':
        operate_excel(path_to_file.strip())


user_filepath = input('''Enter the path to open file (csv, xlsx, json)
Path to file: ''')
main(user_filepath)
