
def save_file(input_, file_path = 'file.txt'):
    with open(file_path, 'a') as file:
        file.write(input_ + '\n')


if __name__ == '__main__':
    save_file(input('Введите строку\n'))