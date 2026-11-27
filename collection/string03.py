# 문자열 포멧

name='김보석'
age=33
height=167.3355

# 1. 포맷 서식 % 표기
print('이름: %s' % name)
print('나이: %d세' % age)
print('키: %fcm' % height)
print('키: %.2fcm' % height)
print('이름: %s 나이: %d 키 %.2fcm' % (name, age, height))

print('이름: %10s' % name)      # 우측정렬 10칸 확보
print('이름: %-10s' % name)     # 좌측정렬 10칸 확보

# 2. format 메소드
print('이름: {} 나이: {} 키 {}cm'.format(name, age, height))
print('이름: {0} 나이: {1} 키 {2}cm {0}'.format(name, age, height))

print('이름: {name} 나이: {age} 키 {height}cm'.format(name=name, age=age, height=height))
print('키: {:.2f}cm'.format(height))

# 3. f-string   f'{name}'
print(f'이름:{name} 나이:{age}')
print(f'이름:{name.strip()} 나이:{age+1}')

print(f'{height:.2f}')
print(f'{height:.1f}')
print(f'{height:10.2f}cm')  # 10칸 차지하는데 소수점은 2번째 자리까지
print(f'{height:<10.2f}cm') # 좌측 정렬
print(f'{height:>10.2f}cm') # 우측 정렬
print(f'{height:^10.2f}cm') # 중앙 정렬
print(f'{height:*^10.2f}cm')
print(f'{height:->10.2f}cm')

print(f'{age:05d}')
print(f"{4:02d}월 {9:02d}일")

# 돈은 세자리마다 , 찍음
price=15771577567
print(f'{price:,}원')
print('{:,}'.format(price))

# 퍼센트
rate = 0.8765
print(f'{rate:.1%}')
print(f'{rate*100:.2f}%')


products = [['노트북', 1250000, 2], ['마우스', 25000, 5], ['키보드', 89000, 3]]


print('-'*50)
for title, price, qty in products:
    print(f'{title:<8}{price:10}{qty:>5}{price*qty:>18}')