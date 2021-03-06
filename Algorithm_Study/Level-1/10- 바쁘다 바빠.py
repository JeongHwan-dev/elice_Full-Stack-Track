"""
[입력 예시]
100
200
300
400

[출력 예시]
16
40
"""

time = list(int(input()) for _ in range(4))
print(int(sum(time) / 60))
print(sum(time) % 60)