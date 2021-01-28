"""
[지시사항]
1. 0이상의 정수인 타수와 안타를 입력받으세요.
2. 16타수 6안타인 상태에서 입력받은 타수와 안타를 더한 타율을 구하세요.
3. 구한 타율을 할푼리로 출력하세요. 할푼리 아래의 소수점은 모두 버림하며 값이 0인 경우 생략합니다.
"""
import math

batting = 16  # 기존 타수
hit = 6  # 기존 안타

# 1번. 0이상의 정수인 타수와 안타를 입력받으세요.
while True:
    batting2 = int(input())  # 타수 입력
    if (type(batting2) == int) and (batting2 >= 0):
        break
    else:
        print("Error: 0 이상의 정수를 입력하세요.")

if batting2 != 0:
    while True:
        hit2 = int(input())  # 안타 입력
        if (type(hit2) == int) and (hit2 >= 0) and (hit2 <= batting2):
            break
        else:
            print(f"Error: 0 ~ {batting2} 사이의 정수를 입력하세요.")

    # 2번.16타수 6안타인 상태에서 입력받은 타수와 안타를 더한 타율을 구하세요.
    batting += batting2
    hit += hit2

# 타율(rate) = 안타(hit) / 타수(batting)
rate = math.trunc((hit / batting) * 1000)

first = int((rate) // 100)  # 할
second = int(((rate) / 10) - (first * 10))  # 푼
third = int((rate) % 10)  # 리


# 할 푼 리 출력 함수
def put(num1, num2, num3):
    if num1 != 0:
        print(f'{num1}할')

    if num2 != 0:
        print(f'{num2}푼')

    if num3 != 0:
        print(f'{num3}리')


# 3번.구한 타율을 할푼리로 출력하세요. (할푼리 아래의 소수점은 모두 버림하며 값이 0인 경우 생략합니다.)
put(first, second, third)


