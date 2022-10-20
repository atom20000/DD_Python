
def kinematic_equation(t, v, x0=0, a=10):
    return x0 + int(v) * int(t) + (a * int(t) ** 2) / 2


if __name__ == '__main__':
    t = input('Введите время t\n')
    v = input('Введите время v\n')
    if (t.isdigit() and v.isdigit()):
        print(kinematic_equation(t= t, v= v))
    else:
        print('Один из введенных параметров не является числом')
