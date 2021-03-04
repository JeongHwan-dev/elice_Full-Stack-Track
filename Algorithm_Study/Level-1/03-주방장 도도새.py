"""
주방장 도도새

[입력 예시]
6 180
45 30 55 20 80 20


[출력 예시]
4
"""
order_num, office_hour = map(int, input().split())
orders_list = list(map(int, input().split()))

use_time = 0
count = 0

for i in range(order_num):
    use_time += orders_list[i]

    if use_time > office_hour:
        break
    else:
        count += 1

print(count)
