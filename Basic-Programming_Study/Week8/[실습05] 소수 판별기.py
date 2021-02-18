"""
[지시사항]
1. prime 모듈을 불러오세요.
2. 0보다 큰 정수를 입력받으세요.
3. 입력받은 숫자를 prime 모듈에 있는 prime_number 의 매개변수로 넘겨 반환 값을 출력하세요.
"""

from prime import prime_number

while True:
    n = int(input())
    if n >= 0:
        break
    else:
        print("0보다 큰 정수를 입력해주세요.")

print(prime_number(n))
