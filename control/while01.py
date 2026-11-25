
# 초기화 -> 조건식 -> 코드실행문 -> 증감식(변화식) -> 조건식 -> 코드실행문 -> .......

i=0

while i<5:
    print(i)
    i=i+1

i=10
while i>0:
    print(i, end=' ')
    i=i-1
print()


#count=int(input('숫자입력:'))
count=0

while count>0:
    print(count, end=' ')
    count=count-1


# 랜덤
import random

print(random.randint(1, 6)) # 1-6 사이의 랜덤값

dice=0
while dice !=3:
    dice=random.randint(1,6) # 주사위 굴리기
    print('dice:', dice)

# 입력값이 0이 입력될때따지, 입력된 모든 수의 합
# break
total=0
while True:
    num=int(input('숫자입력(0입력시 김보석):'))
    total=total+num
    if num==0:
        break
print('총 합계:', total)







print()