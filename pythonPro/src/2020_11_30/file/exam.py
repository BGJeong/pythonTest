a = [17, 92, 18, 33, 58, 7, 33, 42]
maximum = a[0]

for index, value in enumerate(a):
    if value > maximum:
        ind = index
        maximum = value
print('최대값은 %d, 인덱스는 a[%d]' % (maximum, ind))
