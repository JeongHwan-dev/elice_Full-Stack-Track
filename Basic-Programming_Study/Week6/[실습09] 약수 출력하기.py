"""
[지시사항]
1. 자연수 N(2 이상 100,000 이하)을 입력 받습니다.
2. 한 줄에 10개의 약수씩 한 칸씩 띄워서 출력을 합니다. 즉, 약수를 출력함과 동시에 공백을 같이 넣어주면 됩니다.
"""

count = 0

while True:
    n = int(input())
    if (n >= 2) and (n <= 100000):
        break
    else:
        print("Error: 2 이상 100,000이하를 입력하세요.")

for i in range(1, n+1):
    if n % i == 0:
        count += 1
        print(i, end=' ')
        if count % 10 == 0:
            print('\n')
    elif n < i:
        break
    else:
        continue

