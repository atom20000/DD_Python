
def sum_of_digits(num):
    if not num.isdigit():
        print('Вы ввели не число')
        return
    return sum(map(int, list(num)))


if __name__ == '__main__':
    num = input('Введите число\n')
    print(f'Сумма цифр чисал {num} равна', sum_of_digits(num))