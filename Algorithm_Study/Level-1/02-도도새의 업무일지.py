"""
[입력 예시]
5
1 2 2 3 4

[출력 예시]
1 3 2 6 8
"""

day = int(input())
b_record = list(map(int, input().split()))

a_record = []

a_record.append(b_record[0])

for i in range(1, day):
    a_record.append(b_record[i] * (i + 1) - b_record[i - 1] * i)

for i in a_record:
    print(i, end=' ')
