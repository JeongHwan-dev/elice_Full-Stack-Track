"""
[지시사항]
1. 함수명 printstar 를 스네이크 표기법을 이용해 수정하세요.
2. 변수명 starnumber 를 스네이크 표기법을 이용해 수정하세요.
"""


def print_star():
    print("***")

    return None


star_number = 3

if star_number != 100:
    for i in range(0, star_number):
        for j in range(0, i + 1):
            print('*', end='')
        print()
