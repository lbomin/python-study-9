

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