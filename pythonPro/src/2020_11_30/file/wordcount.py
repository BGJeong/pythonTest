def getTextFreq(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        tmp = text.split()

        fa={}
        for c in tmp:
            if c in fa:
                fa[c] += 1
            else:
                fa[c] = 1
    return fa

result = getTextFreq('../data/data.txt')
print(type(result))
print(result)

print(sorted(result.items()))
print(sorted(result.items(), key=lambda x: x[0]))
