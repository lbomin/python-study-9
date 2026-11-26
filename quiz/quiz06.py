print(' 문 제 1')

for i in range(5):
    for j in range(5):
        if j < (5-i):
            print('*', end="")
    print()

for i in range(5):
    for j in range(5-i):
        print('*', end="")
    print()

for i in range(5, 0, -1):
    for j in range(i): 
        print('*', end='')
    print()

for i in range(5, 0 -1):
    print('*' * 1)



print(' 문 제 2')

# for i in range(5):

for i in range(5):        
    for j in range(5):     # 0 1 2 3 4     0 1 2 3 4   0 1 2 3 4    0 1 2 3 4  0 1 2 3 4
        if j < 4 - i :     # j < 4 - 0     j < 3       j < 4 - 2
            print(" ", end="")
        else :
            print("*", end="")

    for k in range(i):
        print('*', end='')
    print()

for i in range(5):
    for j in range(4-i):
        print(' ', end='')
    for k in range(2*i + 1):
        print('*', end='')
    print()
print()

for i in range(4, -1, -1):
    for j in range(i):
        print(' ', end='')
    for k in range(9 - 2*i):
        print('*', end='')
    print()
print()

for i in range(5):
    print(' '*(4-i)+'*'*(2*i+1)) 


'''
n = int(input('숫자입력:'))

for i in range(n):
    for j in range(n-i):
        print('*', end="")
    print()

for i in range(n):
    print(' '*((n-1)-i)+'*'*(2*i+1)) 
'''



print(' 문 제 3, 4')

# range(시작값, 종료값, 증감값)

for i in range(4, -1, -1):        
    for j in range(5):     # 0 1 2 3 4     0 1 2 3 4   0 1 2 3 4    0 1 2 3 4  0 1 2 3 4
        if j < 4 - i :     # j < 4 - 0     j < 3       j < 4 - 2
            print(" ", end="")
        else :
            print("*", end="")

    for k in range(i):
        print('*', end='')
    print()


print()


for i in range(5):        
    for j in range(5):     # 0 1 2 3 4     0 1 2 3 4   0 1 2 3 4    0 1 2 3 4  0 1 2 3 4
        if j < 4 - i :     # j < 4 - 0     j < 3       j < 4 - 2
            print(" ", end="")
        else :
            print("*", end="")

    for k in range(i):
        print('*', end='')
    print()

for i in range(3, -1, -1):        
    for j in range(5):     # 0 1 2 3 4     0 1 2 3 4   0 1 2 3 4    0 1 2 3 4  0 1 2 3 4
        if j < 4 - i :     # j < 4 - 0     j < 3       j < 4 - 2
            print(" ", end="")
        else :
            print("*", end="")

    for k in range(i):
        print('*', end='')
    print()


