solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성', '지구']
planet = '지구'

pos = solarsys.index(planet, 5)
print('%s 는 태양계 %d 번째 위치'%(planet, pos))

a = [1, 2, 3]
a.insert(0, 4)
print(a)