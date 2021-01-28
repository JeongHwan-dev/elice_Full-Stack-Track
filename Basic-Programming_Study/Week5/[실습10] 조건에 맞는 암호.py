"""
[지시사항]
1. 1의 자리 숫자 4개를 공백을 기준으로 입력받으세요.
2. 위의 1, 2, 3, 4의 조건을 동시에 충족하거나 5, 6, 7의 조건을 동시에 충족하는 경우 True를 아니라면 False를 출력합니다.
"""

# 1번을 해보세요.
a, b, c, d = input().split(' ')

a = int(a)
b = int(b)
c = int(c)
d = int(d)

if (a <= b) and (a == d) and (b > c) and (c < 6):
    print("True")

elif (a == b) and (a == c) and (a == d):
    print("True")

else:
    print("False")


