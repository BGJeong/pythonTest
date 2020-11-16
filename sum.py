list1 = [2, 2, 1, 3, 8, 5, 7, 6, 3, 6, 2, 3, 9, 4, 4]
list2 = list(range(1, 11))

result1 = sum(list1)
result2 = sum(list2)

print(result1)
print(result2)

result22 = len(list1)
print(result22)

listdata = []
for i in range(3):
    text = input("입력[%d/3]" % (i + 1))
    listdata.append(text)
    print(listdata)
