"""
[입력 예시]
300
200
500
20
30

[출력 예시]
230
"""

bottle = list(int(input()) for _ in range(3))
cap = list(int(input()) for _ in range(2))

print(min(bottle) + min(cap) + 10)
