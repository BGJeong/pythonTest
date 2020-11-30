file = open('../data/movie_quotes.txt', 'r')

line = file.readline()
print(line)

while line != '':
    print(line, end='')
    line = file.readline()

file.close()