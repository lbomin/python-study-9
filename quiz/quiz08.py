
# [파이썬 퀴즈8 - 리스트]


# 문제1)
# scores = [88, 92, 75, 64, 95, 81, 70]
# - 최고점, 최저점, 평균을 출력하세요.
# - 80점 이상인 점수만 모은 리스트를 만들어 출력하세요. (for 와 리스트 표현식 두 가지 방법)
# - 점수를 높은 순서로 정렬한 새 리스트를 출력하세요. (원본 유지)

'''
scores = [88, 92, 75, 64, 95, 81, 70]

smallest = scores[0]
largest = scores[0]
total = 0
for v in scores:
    if v <= smallest:
        smallest = v
    if v >= largest:
        largest = v
    total = total + v
print("최대", largest, "최소", smallest, "평균", (total/len(scores)))
print("최대", max(scores), "최소", min(scores), "평균", (sum(scores)/len(scores)))

over80 = []
for v in scores:
    if v >= 80:
        over80.append(v)
print(over80)
#print( [v for v in scores if v >= 80] )
over80_2 = [v for v in scores if v >= 80]
print(over80_2)
'''


# 문제2)
# 공백으로 구분된 단어들을 입력 받아서
# - 단어 개수
# - 가장 긴 단어
# - 길이가 5 이상인 단어만 대문자로 바꾼 리스트
# 를 출력하세요.

# inp = input("단어 띄어쓰기 구분해서 입력").split()
# print(inp)


inp = ['apple', 'note', 'book', 'morning', 'afternoon', 'abc123', 'q1234']
print("단어 개수:", len(inp) )

longest = inp[0]
for v in inp:
    if len(v) >= len(longest):
        longest = v
print("가장 긴단어:", longest)
#print("가장 긴단어:", max(inp))     #max(inp) note  min(inp) afternoon
print("가장 긴단어:", max(inp, key=len))

up5 = []
for v in inp:
    if len(v) >= 5:
        up5.append(v.upper())       
print(up5)

up5_2 = [ v.upper() for v in inp if len(v) >= 5]
print(up5_2)

num = [ 5, 10, -9, -15, 14]
print(max(num))
print(max(num, key=abs))     #abs 절대값 



# 문제3)
# 장바구니 프로그램
# cart = []
# 'add 상품명' 을 입력하면 추가, 'del 상품명' 을 입력하면 삭제, 'q' 입력시 종료
# 종료할 때 장바구니 목록을 번호와 함께 출력하세요.

# +옵션1) 이미 있는 상품을 add 하면 '이미 담긴 상품' 출력
# +옵션2) 없는 상품을 del 하면 '없는 상품' 출력

cart = []

while True:
    cmd = input("명령어 입력 (add/del/q) 상품명:").split()

    # q
    print(cmd)

    if cmd[0] == 'q':
        #장바구니목록 보여주고
        for idx, value in enumerate(cart):
            print( (idx+1) , value)
        break

    print(cmd[0], cmd[1])   #IndexError: list index out of range

    if cmd[0] == 'add':
        #이미있는지 체크
        if cmd[1] in cart:  #이미있다
            print("이미 있는 상품입니다")
        else:   #없다
            cart.append(cmd[1])
    elif cmd[0] == 'del':
        #리스트에 있는지 체크하고 지우기 
        if cmd[1] in cart: #있다
            cart.remove(cmd[1])
        else:   #없다
            print("없는 상품입니다")
    else:
        print("잘못입력하셨습니다.")


# 종료된거니까
# 장바구니 보여주기