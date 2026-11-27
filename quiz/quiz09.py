# [파이썬 퀴즈9 - 2차원 리스트]


scores = [
    ['김철수', 90, 85, 77],
    ['이영희', 72, 95, 88],
    ['박민수', 65, 70, 92],
    ['최지우', 98, 89, 94],
]
# (이름, 국어, 영어, 수학)


# 문제1)
# 학생별 총점과 평균을 출력하세요.
# 출력 예) 김철수 총점 252 평균 84.0

total = scores[0]

for i in range(len(scores)):
    temp = scores[i][1:]
    total = temp[0]+temp[1]+temp[2]
    sum1 = round(total / len(temp), 1)
    print(f'{scores[i][0]} 총점 {total} 평균 {sum1}')
print('-'*50)



# 문제2)
# 과목별(국어, 영어, 수학) 평균을 출력하세요.

subjects = ['국어', '영어', '수학']

for j in range(1, 4):
    total = 0

    for i in range(len(scores)):
        total += scores[i][j]

    avg = round(total / len(scores), 1)
    print(subjects[j-1], '평균', avg)
print('-'*50)

# 문제3)
# 총점이 가장 높은 학생의 이름을 출력하세요.
max_total = 0
max_name = ''

for i in range(len(scores)):
    temp = scores[i][1:]
    total = temp[0] + temp[1] + temp[2]

    if total > max_total:
        max_total = total
        max_name = scores[i][0]

print(max_name)
print('-'*50)


# 문제4)
# 3행 4열 2차원 리스트를 만들고 아래처럼 1부터 순서대로 채워서 출력하세요.
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

table = []
num = 1

for i in range(3):
    row = []
    for j in range(4):
        row.append(num)
        num+=1
    table.append(row)
print(table)

table = []

for i in range(3):
    row = []
    for j in range(4):
        row.append(i*4+(j+1))
    table.append(row)
print(table)

table2 = [[i*4+(j+1)for j in range(4)] for i in range(3)]
print(table2)