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