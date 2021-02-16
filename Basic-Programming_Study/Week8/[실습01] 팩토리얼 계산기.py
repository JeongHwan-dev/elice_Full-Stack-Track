"""
[지시사항]
1. math 모듈을 불러오세요. import 혹은 form ~ import로 factorial 함수를 바로 불러와도 좋습니다.
2. 숫자를 입력받으세요.
3. 입력받은 숫자의 팩토리얼을 계산해서 출력해보세요.
"""

import math

# 숫자 입력 받기
n = int(input())

# 입력받은 숫자의 팩토리얼을 계산
n_factorial = math.factorial(n)
print(n_factorial)
