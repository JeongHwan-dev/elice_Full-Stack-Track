"""
[입력 예시]
4 2

[출력 예시]
30
"""

n, k = map(int, input().split())
sum = 0

for i in range(1, n + 1):
    sum += i ** k

print(sum % 1000000009)
