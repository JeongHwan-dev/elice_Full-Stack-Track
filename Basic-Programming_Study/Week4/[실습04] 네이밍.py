"""
[지시사항]
1. 코드 내 i 변수의 이름을 total_num으로 변경하세요.
2. 코드 내 j 변수의 이름을 count로 변경하세요.
"""

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_num = 0
count = 0

for num in num_list:
    total_num += num
    count += 1

print(total_num / count)
