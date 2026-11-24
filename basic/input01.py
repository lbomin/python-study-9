# input

print('input01.py')

# input() 사용자가 입력한 값을 문자열로 돌려주는 기능

x = input('김보석을 입력하세요 : ')
print('바보석 -->', x)

a = input('첫 숫자 : ')
b = input('둘쨰 숫자 : ')
print(a+b)
print(type(a))

# a = int(input('첫 숫자 : '))
print(int(a)+int(b))

# 입력 값을 변수 두개에 나눠서 저장 : split()
print(('10 20 30').split)
print(('10/20/30').split('/'))

c, d = input('숫자 두개 공백으로 띄워서 입력 : ').split()
print(c, d)
print(type(c))
print(int(c)+int(d))
c = int(c)
d = int(b)

# map(함수, 대상)   뒤 대상에게 한번씩 함수를 적용
e, f = map(int, input('숫자 두개 공백으로 띄워서 입력 : ').split())  # '10', '20'
print(e+f)
print(type(e))

g, h, i = map(int, input('숫자 세개 ,로 나줘서 입력 : ').split(','))
print(g+h+i)