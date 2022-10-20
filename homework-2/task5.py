from faker import Faker


def generation():
    faker = Faker('ru_RU')
    return { faker.name() : {
        'возраст' : faker.random.randint(14, 100),
        'должность' : faker.job(),
        'номер рабочего места' : faker.unique.random_int(),
        'наличие доступа к тайне' : faker.random.choice(['да', 'нет'])
    }
        for i in range(faker.random.randint(1, 10))
    }


if __name__ == '__main__':
    print(generation())