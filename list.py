a = []
b = [10, 20, 30]
c = ['python', 'java', 'oracle', 'jsp', 'spring']
d = [30, 3.14, True, False, 'hi']
print(d)

list2 = list(range(10))

list3 = list(range(1, 11))
list4 = list(range(1, 11, 2))

print(list2)
print(list3)
print(list4)

listdata = [1, 2, 'a', 'b', 'c', [4, 5, 6]]
data1 = listdata[1]
data2 = listdata[3]
data3 = listdata[5]
data4 = listdata[5][1]
data5 = listdata[5][-1]
print(data1)
print(data5)

import numpy as np

s3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a1 = np.array(s3)
print(a1)
