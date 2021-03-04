"""
청팀 백팀

[입력 예시]
100 80 70 60
80 70 80 90

[출력 예시]
320
"""

blue = sum(map(int, input().split()))
white = sum(map(int, input().split()))

print(max(blue, white))
