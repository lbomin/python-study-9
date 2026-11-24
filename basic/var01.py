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

