
# bool 자료형   boolean   참 거짓

print(True, False)
print(type(True))

# 비교연산자  -> 결과 True|False
print(10==10)
print(10!=10)
print(10>20)
print(10<20)
print(10>=10)
print(10<=4)
print('---------------------')

# 문자열 비교
print('Python'=='Python')
print('Python'=='python')
print('Python'!='python')
print('---------------------')

# 값 == 객체 비교 is
n1 = 1
n2 = 1.0
print(n1==n2)
print(type(n1)==type(n2))

# print(n1 is n2)
print(type(n1) is type(n2))

x = None
print(x==None)
print(x is None)    # None 비교시 is
print('---------------------')

# 논리 연산자   and or not
print(True and True)
print((1==1) and (2>1))
print(False or True)
print(not True)
print(not False)

age = 25
print(age>=20 and age<30)
print(20<=age<30)   # 파이썬은 비교 연산자를 연속으로 사용하는 것을 허용

print(age>10 or age<100)
print('---------------------')

# 정수, 실수 문자열 -> bool
print(bool(1), bool(0))         #1 -> True  1==1    1>0
print(bool(501), bool(-20))     #숫자형은 0을 False
print(bool(5.5), bool(0.0))     
print(bool('a'), bool(' '), bool('')) # 빈문자열을 False
print(bool([]), bool([1,2,3]))  # 빈리스트를 False
print('---------------------')

# && ||
print(False and 'abc')
print(True and 'abc')   ## { True && <요소>}
print(False or "def")
print('---------------------')

print()



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




# 숫자  정수형(int)  실수형(float)  연산자

# 사칙연산

print(1+1)
print(3-1)
print(2*9)
print(69/7) # 실수형
print(34/12) # 실수형

# 몫 나머지
print(7//2) # 나눗셈 몫 -> 3
print(7%2)  # 나머지    -> 1

print( divmod(7,2)) # (3, 1) (몫, 나머지)

# 거듭제곱
print(2**5) # 2의 5제곱

# 자료형 확인 : type()
print(type(10))     #<class 'int'>   정수
print(type(3.5))    #<class 'float'> 실수
print(type(4/2))    #<class 'float'> 실수
print(type(4//2))   #<class 'int'>   정수

# 정수 <-> 실수 변환
print(int(3.5)) # 정수형으로 변환하며, 소숫점은 버림
print(float(5)) # 실수형으로 변환
#print('100'+ 1 ) # js에선 1001, 파이썬에선 오류남
print(int('100')+ 1 ) # 문자를 숫자와 계산하고 싶다면 변환
print('100'+ str(1) ) # str은 숫자를 문자로 변환

# 실수 계산
print(0.1+0.2)
print((0,1+0.2)==0.3)
print(round(0.1+0.2, 2)) # round 반올림 함수

# 계산 우선순위 -> js와 동일

print(3+5*2)
print((3+5)*2)

# 숫자 표기, 큰 수 계산
print(1234567*1234567)
print(1000000)
print(1,000,000)
print(1_000_000)    # 가독성 위해 숫자에 _ 넣기 가능
print(10, 20, 30)



# 출력

# ,로 구분 출력 , 사이에 공백
print(1,2,3)
print('김보석', '바보')

# 값 사이에 넣을 문자를 지정 sep    기본값:' ' 공백

print(1,2,3, sep=', ')
print(2025, 12, 11, sep='-')
print('김','보석', sep='')
print(1920, 1280, sep='x')

# 줄바꿈 문자 \n
print('김\n보\n석')
print(1,2,3,4, sep='\n')

# print 출력 후 끝에 붙는 문자 : end (기본값 \n)
print('줄바꿈없음', end='')
print('다음줄 출력인가?')
print('김', end='')
print('보', end='')
print('석')

print('hi', 'hello', 'good', sep='~', end='!\n')

# 문자열 숫자
age = 20
print('나이 : ', age)
# print('나이 : ' + age) TypeError: can only concatenate str (not "int") to str
print('나이 : ' + str(age))

# f-string  문자열 내부에 변수 넣으면서 사용
name = '바보석'
print(name, '님 나이는 : ', age)
print(f'{name}님의 나이는 {age}세 입니다 ')
print(f'올해는 {age}세, 내년에는 {age+1}세 입니다')




# 큰따옴표 작은따옴표
hello = 'Hello, world'
hi = '안녕하세요'

print(hello)
print(hi)
print(type(hi))

s1 = "my name's ..."
s2 = 'hi"hello'
s3 = '큰"따옴표 작은\' \"따옴표'    # \' \" 이스케이프 문자
print(s1)
print(s2)
print(s3)

# 여러줄 문자열
s4 = '''
    여러줄
    문자열
    띄울때
    사용 가능

'''
print(s4)

'''
이거 사용을 
여러줄 주석처럼
사용도 가능
'''

s5 = """
    큰따옴표도
    가능
"""

print(s5)

# 이스케이프 문자
print('줄바꿈\n문자')
print('탭 띄어쓰기\t문자')
print('역슬래시 \\ \\ 문자')

# 문자열 연산
a = 'hello'
b = 'world'
print(a+b)
print(a,b,sep=' ')
print(a*3)  # 반복의미
print('-' * 30) # 구분선 역할

# 문자함수
print(len(a))
print(len('12345678'))
print('ll' in a)
print('ll' in b)
print('ll' not in b)

num = '123'
print(int(num)+123)
print(str(123)+'456')


print()



# 변수


# 변수명 = 값

x = 10
y = 3.14
name = '김보석'
is_ok = True    # 파이썬은 변수명에 $ $ $ $ 이거 못 씀

print(x)
print(y)
print(name)
print(is_ok)
print(type(x), type(y), type(name), type(is_ok))

# 변수명
# 영문, 숫자, _ 한정 특문 가능, 숫자 시작 불가
# 대소문자 구분
# 키워드 사용불가 (if, for, class 등)

# 변수명 짓는 스타일
# 자바, JS --->  카멜케이스 -> userName
# 파이썬 ---> 스네이크 케이스 -> user_name



# 숫자형 n ---> n = 10   n = 20   n = '문자'

# 변수에 값을 다시 저장하고 사용시 자료형 변경 가능
x = 20
print(x)
x = '김보석'
print(x, type(x))

# 여러 변수 동시에 저장
a, b, c = 10, 20, 30
print(a, b, c)
d = e = f = 9
print(d, e, f)

# 두 변수의 값 바꾸기
print(a, b)
a, b = b, a
print(a, b)

Tlqkf = '씨발'

# 변수 삭제
del d
#print(d)    # 오류발생

# 빈 변수 : None bi.....
z = None
print(z)

# 변수 계산
a= 10
b = 20
c = a + b
print(c)
c = a + a + b + b
print(c)

# 복합대입연산자
a = a + 5
a += 5
a -= 3
a *= 2
a //= 5
print(a)    # 34
a //= 5
print(a)    # 6.8 -> 6

x = -10
print(-x)



# 딕셔너리  key : value 세트로 저장
# {키:값}

lux = { 'health':490, 'mana':334, 'melee':550, 'armor':18.72}
print(lux)
print(type(lux))    # <class 'dict'>

# 리스트 값 찾기 리스트[인덱스]
# 딕셔너리 값 찾기 딕셔너리[키값]

person = {'name':'홍길동', 'age':25, 'hobby':['독서', '운동']}
print(person['name'])
print(person['age'])
print(person['hobby'])
print(person['hobby'][1])

# 키 값 중복시 마지막 값만 남음
d = {'a':1, 'a':2}
print(d)

# 딕셔너리의 키값 : 문자열, 숫자형, 튜플 가능 (리스트는 불가)

x = {1:'김보석', 2:'바보 김보석', False:0, 3.5:[1.2], (1,2):'튜플의 밸류'}
print(x)
print(x[1])
print(x[False])
print(x[3.5])
print(x[(1,2)])

# 빈 딕셔너리 만들기
a = {}
b = dict()
print(a, b)

# dict() 형태로 만들기
c = dict(health=340, mana=120)
d = dict( [('health', 340), ('mana', 120)] )
e = dict( zip(['health', 'mana'], [340, 120]) )

print(c)
print(d)
print(e)

# 값 변경 | 추가

# lux = { 'health':490, 'mana':334, 'melee':550, 'armor':18.72}
lux['health'] = 2490
lux['mana_regen'] = 3.28
print(lux)

print(lux['mana'])      
print(lux.get('mana'))

#print(lux[mijonjae])       # NameError: name 'mijonjae' is not defined
print(lux.get('mijonjae'))  # 존재하지 않으면 None
print(lux.get('mijonjae', 50))
lux['mijonjae'] = 81
print(lux.get('mijonjae', 50))

badaiyagi = 'dobak'

# 키가 있는지 확인 in
print('health' in lux)
print('mijonjae' in lux)
print('jonjae' in lux)

print(lux)
print(len(lux)) # 갯수

# 삭제
del lux['mijonjae']
print(lux)

print()




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





# sequence 시퀀스

# 각 자료형에 사용되는 기능

l = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
t = (11,22,33,44)
r = range(0, 10, 2) # 0 2 4 6 8
s = '김보석'

# in, not in  내부에 포함? 미포함?
print(30 in l)
print(100 in l)
print(44 in t)
print(12 in r)
print(2 in r)
print('보' in s)
print('성' in s)
print('성' not in s)

# + 연결하기
print(l + [100, 110])
print(l)
print(t + (55, 66))
print(s + " 바보")
#print(r + range(10,16,2)) # range + <-- 불가
print(list(r)+list(range(10,16,2)))

#   * 연산 반복하기
print( [ 1, 2 ] * 3 )
print(('a', 'b') * 3)
print("-" * 50)

print(len(l))
print(len(t))
print(len(r))
print(len(s))

# 인덱스 : 0 ~
print(l[2])
print(t[1])
print(r[3])
print(s[1]) # 문자열에서 인덱스는 해당위치의 문자 하나

# 음수(-) 인덱스    : -1 -2 -3 ... 뒤에서부터
print(l[-1])
print(s[-1])

# print(l[200])   IndexError: list index out of range

# 리스트만 가능한 기능
l[2] = '보석'
print(l)

del l[2]
print(l)

# s[3] = '천재'
print(s) # 문자열 안됨

print()





# 슬라이스

# [시작인덱스:끝인덱스:증가폭]
#           exclusive



l = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

print( l[0:4] ) # 인덱스 0 1 2 3   < 4
print( l[2:7])
print( l )
print( l[0:len(l)] )        # l[1:10]   10개 index ~9

print( l[0:len(l):2] )  # 0 2 4 6 8
print( l[0:10:3] )  # 0 3 6 9

print( l[-7:-2])
print( l[0:-2])

# 인덱스 생략
print( l[:7] ) # 처음부터 - 6까지 (<7)
print( l[3:] ) # 3 인덱스부터 끝까지
print( l[:] )  # 전체   (복사)
l2 = l      # 얕은복사
l2 = l[:]   # 깊은복사

print(l[::2]) # 처음부터 끝까지 2씩 증가
print(l[::-1])  # 정렬을 거꾸로 뒤집는 용도로 사용

# 튜플, range, str 슬라이스
t = (1,2,3,4,5)
print( t[0:3] )
print(range(10)[3:7])
print (list(range(10)[3:7]))

s = 'hello, world!'
print(s[0:5])
print(s[5:])
print(s[::-1]) # 문자열 뒤집기

jumin = '991201-1234567'
print(jumin[:6]) # 앞자리
print(jumin[7:]) # 뒷자리
print(jumin[-7:]) # 뒷자리
print(jumin[7])  # 성별

# 슬라이스 활용 값 바꾸기

a = [10, 20, 30, 40, 50]
a[1:3] = ['a', 'b']
print(a)

a[1:3] = ['x']
print(a)

a = a + [60, 70, 80]
print(a)
a.append(90)
print(a)

del a[0]
print(a)
del a[1:4]
print(a)



print()