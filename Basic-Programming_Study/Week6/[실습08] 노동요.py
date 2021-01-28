"""
[지시사항]
1. 한글로 된 임의의 길이의 문자열을 입력합니다.
2. 마법의 규칙들이 적용된 문자열을 출력합니다. 베짱이도 일하게 만드는 노동요를 부르는 프로그램을 작성해 보세요.
"""


def translate(ex_str):
    if ex_str == ' ':
        print('링디기디기\n', end='')
    elif ex_str == '.':
        print('딩딩딩\n', end='')
    else:
        print('링딩동 ', end='')


str1 = input()

for i in range(len(str1)):
    translate(str1[i])

