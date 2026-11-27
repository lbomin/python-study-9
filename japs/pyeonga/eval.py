total = 0

with open(r'D:\study_9\python-study-9\japs\pyeonga\order.txt', 'r', encoding='utf-8') as f:
    for line in f:
        data = line.strip().split(',')

        if len(data) != 3:
            continue

        name = data[0].strip()
        count = int(data[1].strip())
        price = data[2].strip().replace('원', '')

        if count < 0:
            continue

        price = int(price)

        if price < 0 or price > 10000:
            continue

        total += count * price

print(f'전체 매출: {total}원')