while True:
    num1 = int(input('첫번째 정수를 입력'))
    if not num1:
        break
    num2 = int(input('두번째 정수를 입력'))
    if not num2:
        break
    num3 = int(input('세번째 정수를 입력'))
    if not num3:
        break

    max = num1 if num1 > num2 else num2

    max = num3 if num3 > max else max


    min = num1 if num1 < num2 else num2

    min = num3 if num3 < min else min

    print('최대값은 {0}입니다.'.format(max))
    print('최소값은 {0}입니다.'.format(min))