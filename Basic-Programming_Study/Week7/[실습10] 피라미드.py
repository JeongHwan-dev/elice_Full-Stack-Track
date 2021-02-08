"""
[지시사항]
1. 총 깊이는 N(100이하)이고 맨 윗 줄은 별 한개, 밑 줄 부터는 2개씩 늘어나게 작성하세요.
이때, 맨 윗 별은 맨 밑 줄 별의 가운데에 있어야 합니다.
"""


def pyramid(floor):
    for i in range(1, floor + 1):
        print(" " * (floor - i) + "*" * (2 * i - 1))


var = int(input())
pyramid(var)
