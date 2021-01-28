"""
[지시사항]
1. N이 5의 배수이면 연산자1만 N번만큼 출력합니다.
2. N이 3의 배수이면 연산자2만 N번만큼 출력합니다.
3. 만약 N이 3의 배수이면서 5의 배수이면 아무것도 출력하지 않습니다.
4. 이외의 경우에는 두 연산자를 각각 N회만큼 출력해줍니다.
5. 입력을 받는 부분에서 o1이 연산자1, o2가 연산자2, num이 연산자가 아닌 숫자입니다.
"""
s = input()

o1 = s[0]   # 연산자 1
o2 = s[-1]  # 연산자 2

num = int(s[1:-1])      # 연산자가 아닌 숫자 부분


def output(op1, op2, n):
    # n이 5의 배수
    if n % 15 == 0:
        return None
    elif n % 5 == 0:
        print(op1 * n)
    # n이 3의 배수
    elif n % 3 == 0:
        print(op2 * n)
    else:
        print(op1 * n, end='')
        print(op2 * n)


output(o1, o2, num)