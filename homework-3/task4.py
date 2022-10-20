import os


def copy_file(file_path = 'file.txt', file_cp_path = 'file_cp.txt'):
    if not os.path.exists(file_path):
        print('Файла нет')
        return
    with open(file_path, 'r') as file:
        with open(file_cp_path, 'w') as file_cp:
            file_cp.write(file.read())
    os.remove(file_path)


if __name__ == '__main__':
    copy_file()