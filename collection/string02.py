
s = 'hello, world!'

# 문자 바꾸기 (대체하기) replace(대상, 바꿀값)

print(s.replace('world', '김보석')) # 원본은 유지
print(s)

s=s.replace('world', '김보석')
print(s)

# 분리 / 합치기     split / join
words = 'apple kiwi banana melon'.split()
print(words)

print('apple,kiwi,banana,melon'.split(','))

# 구분자.join(리스트)
print('-'.join(words))
print('/'.join(words))
print(''.join(words))

# 대소문자
print('hello'.upper())
print('GREAT'.lower())
print('hello great'.title())
print('hello great'.capitalize())

# 공백제거 (입력값 정리)
text = '   김 보 석   '
print('[', text, ']')
print('[', text.strip(), ']')
print('[', text.lstrip(), ']')
print('[', text.rstrip(), ']')
print('[', '. 김보석 바보!!'.strip('.!'), ']')

# 문자열 폭 정렬
print('[','바보석'.ljust(10),']')
print('[','바보석'.rjust(10),']')
print('[','바보석'.center(10),']')
print('[','바보석'.zfill(10),']')
print('2'.zfill(2))

print('[','바보석'.ljust(10, '*'),']')

# 문자 찾기
s = '이보석 반짝반짝'
print(s.find('보석'))   # 앞에서부터 찾아서 가장먼저 찾은 위치
print(s.rfind('보석'))  # 오른쪽에서 부터 찾기
print(s.find('보민'))   # 없으면 -1     if 찾은 결과 == -1:  없구나
print(s.index('보석'))  # 찾은 인덱스
# print(s.index('보민'))  ValueError: substring not found
print(s.count('보석'))  # 갯수세기

# 시작 끝 확인
file_name = '김유겸.xlsx'
print(file_name.startswith('김유겸'))
print(file_name.endswith('.xlsx'))
print(file_name.endswith('.pptx')) # 거짓

# 문자 타입 종류 판단
print('1234'.isdigit())
print(int('1234'))
print('12q34'.isdigit())    # False 숫자 형태 아님
# print(int('12q34')) ValueError: invalid literal for int() with base 10: '12q34'
print('1234'.isalpha())
print('abcd'.isalpha())

print('abcd'.isalnum())
print('1234abcd!@'.isalnum())  # 숫자영문

# 메소드 체이닝 (이어붙여서 수행)
raw = '  Hello, Python   '

raw = raw.strip()
raw = raw.lower()
raw = raw = raw.replace('python', 'world')

print(raw)

raw2 = ' hello, python  '
raw2 = raw2.strip().lower().replace('python', 'world2')
print(raw2)

email = input('이메일: ').strip().lower()   # 공백제거, 소문자로
print(email)
user_id, domain = email.split('@')
print(user_id, domain)