from sys import stdin


def distance(a, b): #Расстояние Левенштейна
    n, m = len(a), len(b)
    etal = b
    error_pos = []
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
                if j == i:
                    error_pos.append(j-1)
            min_act = min((add, 'add'), (delete, 'delete'), (change, 'change'))
            current_row[j] = min_act[0]
    return (current_row[n], error_pos, etal)

def check_grammar():
    print('каждое слово с новой строки. Остановите ввод нажатие ctr+D')
    true_word = list(map(lambda x : x.rstrip(), stdin.readlines()))
    sentence = (input('Введите проверяемое предложение\n')).split()
    for i in set(true_word).intersection(sentence): sentence.remove(i)
    for word in sentence:
        check = []
        for true_w in true_word:
            check.append(distance(word, true_w))
        min_dis = min(check)
        print(''.join([ f' {i} ' if j in min_dis[1] else i for i, j in zip(word, range(len(word)))]), f'\nЭталонное слова {min_dis[2]}')

if __name__ == '__main__':
    check_grammar()
    