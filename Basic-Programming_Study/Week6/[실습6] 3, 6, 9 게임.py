"""
[지시사항]
1. 위 3, 6, 9게임의 규칙에 맞게 1부터 30까지 출력해 보세요.
2. 한줄당 숫자 혹은 “짝!” 하나씩 출력하면 됩니다.
"""

# 반복문을 이용하여 3, 6, 9 게임을 만들어주세요!
num_list = ["3", "6", "9"]

for n in range(1, 31):
    n = str(n)

    if len(n) == 2:
        if (n[0] in num_list) or (n[1] in num_list):
            print("짝!")
        else:
            print(n)

    elif len(n) == 1:
        if n[0] in num_list:
            print("짝!")
        else:
            print(n)

    else:
        None
