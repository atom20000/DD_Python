import random


lst_goods = ['Молоко', 'Сливки', 'Мороженое', 'Специи', 'Мясо', 'Сыр', 
    'Консервы', 'Яйца', 'Масло', 'Хлеб', 'Батон', 'Конфеты', 'Печенье',
    'Мука', 'Крупа', 'Макаронны', 'Чай', 'Уксус', 'Свежие овощи', 'Свежие фрукты',
    'Орехи', 'Грибы', 'Ткани', 'Обувь', 'Косметические товары', 'Мыло', 'Бумага']

def difference_sets():
    set_1 = set(random.choice(lst_goods) for i in range(random.randint(1, len(lst_goods))))
    set_2 = set(random.choice(lst_goods) for i in range(random.randint(1, len(lst_goods))))
    set_diff = set_1.symmetric_difference(set_2)
    print(f'Первое множество\n{set_1}\nВторое множество\n{set_2}\nРазница множеств\n{set_diff}')


if __name__ == '__main__':
    difference_sets()