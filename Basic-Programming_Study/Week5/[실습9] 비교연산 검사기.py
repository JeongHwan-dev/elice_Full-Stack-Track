"""
[지시사항]
1. 공백을 기준으로 입력되는 숫자, 비교 연산자, 숫자를 변수에 저장하세요.
2. 해당 비교 연산의 참, 거짓 여부에 따라 결과를 출력해보세요.
"""
# 1번을 해보세요.
num1, op, num2 = input().split(' ')

num1 = int(num1)
num2 = int(num2)

# 2번을 해보세요.
if op == '>':
    print(num1 > num2)
elif op == '<':
    print(num1 < num2)
elif op == '==':
    print(num1 == num2)
else:
    print('Error')

