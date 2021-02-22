"""
[지시사항]
1. neverland() 함수가 호출되는 코드의 띄어쓰기를 올바르게 수정해보세요.
"""


def neverland(queue):
    first = queue.pop(2)
    queue.sort()
    queue.insert(0, first)
    return queue


queue = [30, 10, 20, 50, 40, 60]
neverland(queue)
