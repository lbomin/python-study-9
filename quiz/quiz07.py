# FizzBuzz 문제
# 1 ~ 100 까지 출력하면서
# 3의 배수는 Fizz, 5의 배수는 Buzz, 3과 5의 공배수는 FizzBuzz 출력
'''
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)    
'''
# [파이썬 퀴즈7 - 제어문 종합 : 업다운 숫자 맞추기 게임]

# 1 ~ 100 사이 랜덤 숫자를 하나 정하고
# 사용자가 숫자를 입력하면 'UP' / 'DOWN' 힌트를 주세요.
# 맞추면 몇 번 만에 맞췄는지 출력하고 종료합니다.

import random

rnum = random.randint(1, 100)
count = 0

while True:
    jesi = int(input("정답을 맞춰보세요! : "))

    if jesi <= 0 or jesi > 100:
        print('1~100 사이 숫자만 입력하세요.')
        continue

    count += 1

    if rnum == jesi:
        print(f'{rnum} 정답입니다!')
        print(f'{count}번 만에 맞췄습니다!')
        break
    
    elif count>=7:
        print(f'7회가 지나 정답 공개후 종료합니다.')
        print(f'정답은 {rnum} 입니다!')
        break

    elif rnum > jesi:
        print('UP')

    else:
        print('DOWN')