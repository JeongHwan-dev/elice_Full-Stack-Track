"""
[지시사항]
1. 영희와 철수가 숫자를 세는 코드를 하나로 하는 print_number()를 만드세요. 해당 함수는 매개변수로 이름을 입력받습니다.
"""

max_time = 100
count = 0


def print_number(name):
    for number in range(max_time):
        print(f'{name} : {number}')

        if number == 10:
            break

    return None


print_number("영희")
print_number("철수")
