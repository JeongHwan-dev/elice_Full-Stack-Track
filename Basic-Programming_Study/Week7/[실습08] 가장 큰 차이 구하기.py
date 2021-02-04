"""
[지시사항]
1. 입력으로 주어지는 크기가 5인 리스트를 저장하세요.
2. 리스트 내 두 원소의 가장 큰 차이를 출력하세요.
"""

# 1번을 해보세요.
num_list = []

for i in range(5):
    num = int(input())
    num_list.append(num)

# 2번을 해보세요.
print(max(num_list) - min(num_list))
