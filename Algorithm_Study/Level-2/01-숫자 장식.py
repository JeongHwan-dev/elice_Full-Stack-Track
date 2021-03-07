def solution(arr):
    if len(arr) == m:
        print(' '.join(str(x) for x in arr))
        return

    for i in range(1, n + 1):
        arr.append(i)
        solution(arr)
        arr.pop()


if __name__ == '__main__':
    n, m = map(int, input().split())

    for i in range(1, n + 1):
        solution([i])

