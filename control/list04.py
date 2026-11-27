# 리스트 중첩
# 2차원 리스트

# 2차원 행, 열

a=[[10,20],[30,40],[50,60]]

print(a)

print(a[1][0])
print(a[2][0])
print(a[0][1])
a[0][1]=99

print(a)

b=[[10,20],[30,40],[50,60]]

# 반복문으로 2차원 리스트 출력

for i in range(len(b)): # 3 0 1 2
    for j in range(len(b[1])):
        print(b[i][j], end=' ')
    print()
print('-'*50)

for row in b:   #[10, 20]   [30, 40]    [50, 60]
    for v in row:
        print(v, end=' ')
    print()
print('-'*50)

for x, y in b:
    print(x, y)
print('-'*50)


# 2차원 리스트 생성
# [[],[],[]]

c = []
for i in range(3):
    temp = []
    for j in range(2):      # []
        temp.append(j)
    # temp=[0, 1]
    c.append(temp)
print(c)

d=[i for i in range(3)]
print(d)

e=[[j for j in range(2)]for i in range(3)]
print(e)

f=[[0]*2 for i in range(3)]
print(f)


students=[['김보석', '바보', 33],['이보석', '앰생', 24],['김유겸', '큼겸', 23]]
print(sorted(students))
print(sorted(students, reverse=True))
# 특정 위치의 열을 기준으로 정렬

print(sorted(students, key=lambda s: s[1])) # lambda 한줄로 간단하게 작성하는 함수
print(sorted(students, key=lambda s: s[2])) 

# 2차원 리스트 복사
a=[[10,20],[30,40]]
b=a

print(a,b)
a[0][0]=99
print(a,b)
print('-'*50)

a=[[10,20],[30,40]]
b=a.copy()

print(a,b)
a[0][0]=99
print(a,b)

print('-'*50)

import copy

a=[[10,20],[30,40]]
b=copy.deepcopy(a)

print(a,b)
a[0][0]=99
print(a,b)

print('-'*50)

