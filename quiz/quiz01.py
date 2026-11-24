# [파이썬 퀴즈1 - 입출력]

# 문제1)
# 사각형의 가로, 세로 길이를 한 줄에 공백으로 구분해서 입력 받고
# 넓이와 둘레를 아래처럼 출력하세요.
# 입력 예) 10 5
# 출력 예)
# 넓이 : 50
# 둘레 : 30
a, b = 10, 5
print('문제 1')
print('넓이 : ',a)
print('둘레 : ',b)
print()

# 문제2)
# 국어, 영어, 수학 점수를 콤마로 구분해서 입력 받고
# 총점과 평균(소수점 둘째 자리까지)을 출력하세요.
# 입력 예) 90,85,77
# 출력 예) 총점 252, 평균 84.0
print('문제 2')
c, d, e = map(int, input('숫자 세개 ,로 나줘서 입력 : ').split(','))
total = c+d+e
avg = total / 3
print(f'총점 {total}, 평균 {avg}')
print('총점 :', total, end=", ")
print('평균 ', round(avg, 2))
print(f'총점 {total}, 평균 {avg:.2f}')


# 문제3)
# 초(second)를 입력 받아서 '몇 시간 몇 분 몇 초' 로 출력하세요.
# 입력 예) 3725
# 출력 예) 1시간 2분 5초
print('문제 3')
second = int(input('초 입력 : '))

h = second // 3600
m = (second % 3600) // 60
s = second % 60

print(f'{h}시간 {m}분 {s}초')
print()

# 문제4)
# 년, 월, 일을 입력 받아서 sep 을 사용해 2026/11/02 형태로 출력하세요.

print('문제 4')
year = input('년 입력 : ')
month = input('월 입력 : ')
day = input('일 입력 : ')

print(year, month, day, sep='/')
print()