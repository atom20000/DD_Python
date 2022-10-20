import os


def load_file(file_path = 'file.txt'):
    if not os.path.exists(file_path):
        print('Файла нет')
        return
    with open(file_path, 'r') as file:
        print(file.read())


if __name__ == '__main__':
    load_file()