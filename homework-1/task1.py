
def calculate():
    num1 = input('первое число\n')
    if not num1.isnumeric():
        print('Error')
        return
    if (oper := input('Оператор из списка: +, -, *, /, **, %, radical\n')) \
        and oper not in ('+', '-', '*', '/', '**', '%', 'radical'):
        print('Error')
    else:
        if (num2 := input('второе число\n')) and num2.isnumeric():
            if oper == 'radical' and int(num2) != 0:
                print(f'{num2}\u221A{num1} = {float(num1) ** (1 / float(num2))}')
            else:
                if oper == '/' and int(num2) == 0:
                    print('Error')
                    return
                expr = ' '.join((num1, oper, num2))
                print(f'{expr} = {eval(expr)}')
        else:
            print('Error')


if __name__ == '__main__':
    calculate()