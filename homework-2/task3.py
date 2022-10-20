
def sum_of_digits(num):
    print(f'Сумма цифр чисал {num} равна', sum(map(int, list(num))))


if __name__ == '__main__':
    sum_of_digits(input('Введите число\n'))