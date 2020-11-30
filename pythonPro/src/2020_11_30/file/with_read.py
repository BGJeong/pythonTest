with open('../data/stockcode.txt', 'r', encoding='utf-8') as file:
    line = file.readline()

    num = 1
    while line != '':
        print('%d %s' %(num, line), end='')
        line = file.readline()
        num += 1