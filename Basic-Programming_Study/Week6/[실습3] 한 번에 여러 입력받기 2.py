"""
[지시사항]
1. 공백을 기준으로 입력되는 숫자를 리스트에 저장해보세요.
2. 리스트의 모든 수에 대한 평균을 출력해봅시다. 단 소수점 아래는 모두 버림 합니다.
"""

# 1번을 해보세요.
num_list = list(map(int, input().split()))


# 2번을 해보세요.
def avg(ex_list):
    sum = 0
    for i in ex_list:
        sum += i
    return sum / len(ex_list)


print(int(avg(num_list)))