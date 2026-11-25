# [파이썬 퀴즈5 - 반복문]


# 문제1)
# 단을 입력 받아서 구구단을 출력하세요. (for 사용)
# 입력 예) 7
# 출력 예) 7 * 1 = 7 ... 7 * 9 = 63
print('문제 1')
x=int(input('단수 입력:'))
for i in range(1, 10):
    print(f'{x} x {i} = {x*i}')
print()

# 문제2)
# 1 부터 입력한 수까지의 짝수 합과 홀수 합을 각각 출력하세요.
print('문제 2')
y = int(input('숫자 입력: '))

even_sum = 0
odd_sum = 0

for i in range(1, y + 1):
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i

print('짝수 합:', even_sum)
print('홀수 합:', odd_sum)
print()

# 문제3)
x = [49, -17, 25, 102, 8, 62, 21]
# 리스트의 각 요소에 10을 곱한 값을 한 줄에 출력하세요.
print('문제 3')
for i in x:
    print(i * 10, end=' ')
print()
print()


# 문제4)
# 잔액 13000원 교통카드에서 1350원씩 차감하면서 잔액이 1350원 미만이 될 때까지
# '남은 잔액' 을 출력하세요. (while 사용)
print('문제 4')
money = 13000

while money >= 1350:
    money = money - 1350
    print('남은 잔액:', money)
print()