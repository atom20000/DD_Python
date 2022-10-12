from sys import stdin


def distance(a, b): #Расстояние Левенштейна
    n, m = len(a), len(b)
    etal = b
    if n > m:
        a, b = b, a
        n, m = m, n
    current_row = range(n + 1) 
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
            print(current_row)
    return (current_row[n], etal)

def check_grammar():
    print('каждое слово с новой строки. Остановите ввод нажатие ctr+D')
    true_word = list(map(lambda x : x.rstrip(), stdin.readlines()))
    sentence = (input('Введите проверяемое предложение\n')).split()
    #import pdb; pdb.set_trace()
    for i in set(true_word).intersection(sentence): sentence.remove(i)
    for word in sentence:
        #for true_w in list(filter(lambda x: abs(len(x)-len(word)) < 3, true_word)):
        for true_w in true_word:
            
            pass


if __name__ == '__main__':
    #check_grammar()
    print(distance('мапа','мама'))
    