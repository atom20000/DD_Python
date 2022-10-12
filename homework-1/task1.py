
def check_num(num):
    try:
        float(num)
        return True
    except:
        return False

def calculate():
    num1 = input('первое число\n')
    if not check_num(num1):
        print('Error')
        return
    if (oper := input('Оператор из списка: +, -, *, /, **, %, radical\n')) \
        and oper not in ('+', '-', '*', '/', '**', '%', 'radical'):
        print('Error')
    else:
        if (num2 := input('второе число\n')) and check_num(num2):
            if oper == 'radical' and int(num2) != 0:
                print(f'{num2}\u221A{num1} = {float(num1) ** (1 / float(num2))}')
            else:
                print('Error')
                return
            if oper == '/' and int(num2) == 0:
                print('Error')
                return
            expr = ' '.join((num1, oper, num2))
            print(f'{expr} = {eval(expr)}')
        else:
            print('Error')


if __name__ == '__main__':
    calculate()