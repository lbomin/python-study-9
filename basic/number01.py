
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

