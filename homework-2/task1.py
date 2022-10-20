from faker import Faker


faker = Faker('ru_RU')

class Republic():

    def __init__(self):
        self.name = faker.company()
        self.agricultural_industry = ('Сельское хозяйство', faker.random.randint(-1, 1))
        self.light_industry = ('Легкая промышленность', faker.random.randint(-1, 1))
        self.group_a_heavy_industry = ('Тяжелая промышленность группы А', faker.random.randint(-1, 1))
        self.group_b_heavy_industry = ('Тяжелая промышленность группы Б', faker.random.randint(-1, 1))
        self.military_industrial_complex = ('Военно промышленный комплекс', faker.random.randint(-1, 1))
        self.science = ('Наука', faker.random.randint(-1, 1))
        self.chemical_industry = ('Химическая промышленность', faker.random.randint(-1, 1))

    def find_industries(self, value):
        return [self.__getattribute__(i)[0] for i in self.__dir__()[1:8] if self.__getattribute__(i)[1] == value]

def generate_stat(count):
    republics = [Republic() for i in range(count)]
    find_lst = lambda v: [j for i in map(lambda x: x.find_industries(v), republics) for j in i]
    find_max = lambda lst: max([(i, lst.count(i)) for i in set(lst)], key= lambda x: x[1])
    laggards = find_lst(-1)
    the_most_laggards = find_max(laggards)
    print(f'Самая отстающая отрасль в союзных республиках "{the_most_laggards[0]}", она отстает на {the_most_laggards[1]}')
    advanced = find_lst(1)
    the_most_advanced = find_max(advanced)
    print(f'Самая развитая отрасль в союзных республиках "{the_most_advanced[0]}", она развита на {the_most_advanced[1]}')
    balanced = find_lst(0)
    the_most_balanced = find_max(balanced)
    print(f'Самая сбалансированная отрасль в союзных республиках "{the_most_balanced[0]}", она сбалансирована на {the_most_balanced[1]}')
    all_industries_lag_adv = laggards + advanced
    stat_all_industries_lag_adv = [(i, all_industries_lag_adv.count(i)) for i in set(all_industries_lag_adv)]
    for i in stat_all_industries_lag_adv:
        print(f'Статистика по отрасли "{i[0]}", значение {i[1]}')
if __name__ == '__main__':
    generate_stat(4)