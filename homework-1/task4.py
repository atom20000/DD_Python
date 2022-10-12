import time


def timer():
    timer_value = time.strptime(input('Введите время в формате HH:MM:SS\n'),'%H:%M:%S')
    timer_end = time.time() + 3600 * timer_value.tm_hour + 60 * timer_value.tm_min + timer_value.tm_sec
    while time.time() < timer_end:
        print(time.strftime('%H:%M:%S', time.gmtime(timer_end - time.time())))
        time.sleep(1)
    print('ВСЕ, КОНЕЦ!')


if __name__ == '__main__':
    timer()