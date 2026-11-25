# [파이썬 퀴즈4 - 조건문]

# 문제1)
# 나이를 입력 받아서 요금을 출력하세요.
# - 8세 미만 : 무료
# - 8 ~ 13세 : 650원
# - 14 ~ 18세 : 1050원
# - 19 ~ 64세 : 1350원
# - 65세 이상 : 무료

age = int(input('나이 입력:'))

if age < 8:
    print('무료')
elif age <=13:
    print('650원')
elif age <=18:
    print('1050원')
elif age <=64:
    print('1350원')
else:
    print('무료')

# 문제2)
# 년도를 입력 받아서 윤년인지 출력하세요.2
# - 4로 나누어 떨어지고 100으로 나누어 떨어지지 않으면 윤년
# - 또는 400으로 나누어 떨어지면 윤년

year = int(input('연도 입력:'))
if (year%4) == 0 and (year%100) != 0:
    print('윤년')
elif (year%400) == 0:
    print('윤년')
else:
    print('윤년 아님')

# 문제3)
# 교통카드 잔액 9000원에서 나이에 따른 요금(문제1)을 차감하고
# 남은 잔액을 출력하세요.

cash = 9000
print(f'잔액은 {cash}원 입니다')
x = int(input('나이 입력:'))

if x < 8:
    pass
elif x <=13:
    cash-=650
elif x <=18:
    cash-=1050
elif x <=64:
    cash-=1350
else:
    pass

print(f'잔액은 {cash}원 입니다')

# 문제4)
# 세 정수를 공백으로 구분해 입력 받아서 가장 큰 수를 출력하세요. (max 함수 사용하지 않기)
a, b, c = map(int,input('새 정수를 공백으로 구분하여 입력:').split())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)



print()