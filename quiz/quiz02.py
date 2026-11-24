# [파이썬 퀴즈2 - 시퀀스]


# 문제1)
url = 'https://www.python.org/downloads'
# 위 문자열에서 슬라이스를 사용해 아래 값을 꺼내 출력하세요.
# - 'https'
# - 'www.python.org'
# - 'downloads'
print('문제 1')

print(url[:5])
print(url[8:22])
print(url[23:])

print('-'*30)


# 문제2)
n = [-32, 5, 2, -10, 55, 7, 9, 0]
# - 홀수 번째 인덱스(1, 3, 5 ...)의 요소만 출력하세요.
# - 마지막 3개 요소를 출력하세요.
# - 리스트를 거꾸로 뒤집어서 출력하세요.
print('문제 2')

print(n[1::2])
print(n[-3::])
print(n[::-1])

print('-'*30)

# 문제3)
# 날짜 문자열 '20261102' 를 입력 받아서 2026년 11월 02일 로 출력하세요.
print('문제 3')

nal = input('8자리 연월일 입력 : ')
y = nal[0:4] 
m = nal[4:6]
d = nal[6:8]
print(f'{y}년 {m}월 {d}일')

print('-'*30)

# 문제4)
year = (2021, 2022, 2023, 2024, 2025, 2026)
population = (10249679, 10195318, 10143645, 9994195, 9886021, 9810000)
# 최근 3년간의 연도와 인구 수를 출력하세요. (음수 인덱스 사용)
print('문제 4')

print(year[-3],'-',population[-3])
print(year[-2],'-',population[-2])
print(year[-1],'-',population[-1])

print('-'*30)

print()