file = open('../data/test.txt', 'r', encoding='utf-8')
str = file.read()
print(str)
file.close()