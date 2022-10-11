
def calculate():
    num1 = input('первое число\n')
    if not num1.isdigit():
        print('Error')
        return
    if (oper := input('Оператор из списка: +, -, *, /, **, %, radical\n')) \
        and oper not in ('+', '-', '*', '/', '**', '%', 'radical'):
        print('Error')
    else:
        if (num2 := input('второе число\n')) and num2.isdigit() and int(num2) != 0:
            if oper == 'radical':
                print(f'{num2}\u221A{num1} = {int(num1) ** (1 / int(num2))}')
            else:
                expr = ' '.join((num1, oper, num2))
                print(f'{expr} = {eval(expr)}')
        else:
            print('Error')


if __name__ == '__main__':
    calculate()