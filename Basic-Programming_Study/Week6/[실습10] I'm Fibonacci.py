"""
[지시사항]
1. 정수를 입력받습니다.
2. 초기 리스트를 [0,1]로 설정해줍니다. 만약 0을 입력한다면 [0,1]이 출력되어야 합니다.
3. 피보나치 수열을 구현합니다. n==1이라면 [0]만, n==2라면 [0,1]을 출력해줍니다.
4. 위의 조건에 해당되지 않는다면 2를 넘어가는 수입니다. n보다 작은 수들의 피보나찌 수열을 출력합니다
"""

n = int(input())

num_list = [0, 1]

if n == 0 or n == 2:
    pass
elif n == 1:
    num_list.pop()
else:
    for i in range(0, n):
        if (num_list[i] + num_list[i + 1]) < n:
            num_list.append(num_list[i] + num_list[i + 1])
        else:
            break

print(num_list)
