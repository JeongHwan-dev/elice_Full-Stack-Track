"""
[지시사항]
1. proverb 모듈을 불러오세요.
2. 문자열을 입력받으세요.
3. 입력받은 문자열을 problem 리스트에서 찾아 인덱스를 저장하세요.
4. answer 리스트에서 저장한 인덱스의 문자를 출력하세요.
"""

from proverb import problem, answer

value = input()

p_index = problem.index(value)
print(answer[p_index])
