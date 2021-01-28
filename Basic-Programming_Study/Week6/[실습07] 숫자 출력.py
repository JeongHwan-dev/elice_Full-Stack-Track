"""
[지시사항]
1. 0보다 큰 정수를 입력받으세요.
2. 1부터 해당 숫자까지 출력 예시처럼 출력해보세요.
"""

n = int(input())

if n > 0:
    for i in range(1, n + 1):
        if i != n:
            print(i, end=', ')
        else:
            print(i)
else:
    print("Error: 0보다 큰 정수가 아닙니다.")



