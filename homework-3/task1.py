import random


def task():
    try:
        print('ОК', 10 / random.randint(0,1))
    except:
        print('деление на 0')


if __name__ == '__main__':
    task()