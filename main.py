import inputs


def main(path_to_file):
    inputs.clear()
    extension = path_to_file.strip().split('.')[-1]

    if extension == 'json':
        inputs.operate_json(path_to_file.strip())

    if extension == 'csv':
        inputs.operate_csv(path_to_file.strip())

    if extension == 'xlsx' or extension == 'xls':
        inputs.operate_excel(path_to_file.strip())


while True:
    inputs.clear()
    user_filepath = input('''Enter the path to open file (csv, xlsx, json)
For exit, type 'exit'
Path to file: ''')

    if user_filepath.strip().lower() == 'exit':
        break

    main(user_filepath)
