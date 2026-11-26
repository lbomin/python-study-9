
# 리스트 조작

a = [10,20,30]
a.append(40)

print(a)

# 함수 메소드
# 특정 객체에 속한 함수 : 메소드

a.append([100,200])
print(a)
print(a[4])
print(a[4][0])
print(a[4][1])

print(len(a)) # 리스트의 길이

b=[1,2,3]
#b.append(4,5)
b=[1,2,3]+[4,5]
print(b)

# 리스트를 연결해서 확장
b.extend([6,7,8])
print(b)

# 특정위치에 추가  insert
c=[10,20,30]
c.insert(1,500)
print(c)

c.insert(0,100)
c.insert(len(c),900)
print(c)

# 리스트 요소 삭제
d=[10,20,30]
print(d)
print(d.pop())  # 제일 뒤에 요소를 삭제하면서 변환
print(d)
print(d.pop(0)) # pop(index) 제일 앞 요소 삭제하면서 반환
print(d)

# 값으로 요소 삭제
e=[10,20,30,40,20]

e.remove(30)
print(e)
#e.remove(50) ValueError: list.remove(x): x not in list
e.remove(20)    # 처음 나오는 값 한개만 삭제
print(e)

# 검색

e=[10,20,30,40,20]  
print(e.index(30))  # 해당 값이 위치한 인덱스를 반환
#print(e.index(50))  ValueError: list.index(x): x not in list
print(e.count(20))  # 해당 값의 개수

# 뒤집기 
e.reverse()
print(e)

# 정렬
e.sort()    # 리스트를 오름차순으로 정렬
print(e)
e=[1,4,3,5,3,6]
e.sort(reverse=True)   # 리스트를 내림차순으로 정렬
print(e)

# sorted() vs sort()
q=[5,7,3,5,8,9]
# q.sort()    리스트를 그대로 정렬
w=sorted(q) # 정렬해서 정렬된 리스트를 반환
print(q)
print(w)
e=sorted(q, reverse=True)
q.sort()    # 원본 반영
print(q)

print(sorted(q, reverse=True))
print(e.sort()) #None   e.sort() 내부적으로 정렬을 할 뿐, 반환이 없음
print(e)

# 모든 요소 삭제
e.clear()
print(e)    # [] 빈 리스트


# 리스트 복사
a=[1,2,3,4]     # 참조타입 변수 주소 ...
b=a             # 실제 복사가 일어난건 아님

print(a==b)     # [1,2,3,4] 값은 동일 True
print(a is b)   # 같은 객체인가?

a[0] = 99   # a, b 둘 다 바뀐것으로 보임
print(a)
print(b)

a=[1,2,3,4]
b=a.copy()
c=a[:]
d=a[::-1]





a[0]=99

print(a,b,c,d)
