import random


def generate():
    noun = []
    verb = []
    print('Стоп символ ";"')
    while (word := input('Существительные\n')) and word != ';': 
        noun.append(word)
    while (word := input('Глаголы\n')) and word != ';': 
        verb.append(word)
    count = input('Число фраз\n')
    if not count.isdigit():
        print('Error')
        return
    for i in range(int(count)):
        phrase = [
            random.choice(noun),
            random.choice(noun),
            random.choice(verb)
        ]
        random.shuffle(phrase)
        print(' '.join(phrase))


if __name__ == '__main__':
    generate()