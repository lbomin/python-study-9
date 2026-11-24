
# 리스트와 튜플

# 리스트(list) : 대괄호 [] 여러값 묶어서 저장

a = [12,34,56,78]
print(a)
print(type(a))  # <class 'list'>

# 자료형 상관없이 함께 저장 가능
person = ['홍길동', 25, 175.5, True]
print(person)

# 빈 리스트
b = []
c = list()
print(b, c)

# range() 활용 리스트 만들기
print(list(range(10)))          # 0 - 9
print(list(range(5, 12)))       # 5 - 11
print(list(range(0, 20, 2)))    # 0 - 18 2씩 증가
print(list(range(10, 0 , -1)))  # 10 - 1 1씩 감소

# 튜플 : 소괄호 () 묶어서 값을 저장, 생성 후 값 변경 불가
t = (11,22,33,44)
print(t)
print(type(t))  # <class 'tuple'>

t2 = 11, 22, 33 # 튜플로 저장됨
print(t2)

t3 = (38)   # 그냥 정수
print(t3)
t4 = (38,)  # 튜플로 인식
print(t4)

# 리스트는 값 변경 가능, 튜플은 불가능
print(a[1])
print(t[2])
a[1] = 99
print(a[1])
# t[2] = 88   TypeError: 'tuple' object does not support item assignment

# a:list t:tuple
# list tuple 변환
print(tuple(a))
print(list(t))

print(list('김보석'))

x, y, z = [10, 20, 30]
q, w = (40, 50)

print(x, y, z, q, w)





print()