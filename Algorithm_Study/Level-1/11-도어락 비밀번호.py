"""
[입력 예시]
1995 2000

[출력 예시]
5993
"""

y1, y2 = map(str, input().split())

print(int(y1[::-1]) + int(y2[::-1]))
