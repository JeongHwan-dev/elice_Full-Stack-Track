"""
[지시사항]
1. 입력으로 주어지는 숫자 num의 2진수를 출력해보세요.
"""

num = int(input())

print(bin(num).replace('0b', ''))