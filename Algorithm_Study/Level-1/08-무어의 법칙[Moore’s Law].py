"""
[입력 예시]
14

[출력 예시]
22
"""

n_list = list(str(2 ** int(input())))
n_intList = list(map(int, n_list))

print(sum(n_intList))

