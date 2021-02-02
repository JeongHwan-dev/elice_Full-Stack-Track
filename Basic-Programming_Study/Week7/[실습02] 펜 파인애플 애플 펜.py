"""
[지시사항]
1. words 리스트에서 pop을 이용해 인덱스 4, 4, 5, 5, 5 순서로 원소를 제거하세요.
2. join 함수를 이용해서 공백을 기준으로 리스트를 연결하여 lyrics 변수에 저장하세요.
3. lyrics를 출력하세요.
4. 문자 'p'의 개수를 count 함수를 이용해서 출력하세요.
"""

words = ['i', 'have', 'a', 'pen', 'i', 'have', 'pineapple', 'i', 'have', 'an', 'apple', 'pen']


def pop_function(n, i):
    for j in range(n):
        words.pop(i)


pop_function(2, 4)
pop_function(3, 5)
lyrics = str.join(' ', words)

print(lyrics)
print(lyrics.count('p'))
