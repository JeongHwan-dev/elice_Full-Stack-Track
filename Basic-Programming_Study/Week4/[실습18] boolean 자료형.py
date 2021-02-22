"""
[지시사항]
1. 코드 8번째 줄에서 is_odd 변수 자체만으로 참 또는 거짓을 판별하도록 비교 연산자를 제거하세요.
"""

number = 3

if number % 2 == 1:
    is_odd = True
else:
    is_odd = False

if is_odd is True:
    print("number는 홀수입니다.")
else:
    print("number는 짝수입니다.")
