"""
[지시사항]
1. 함수 checkname 과 변수 testname 에 스네이크 표기법을 적용하세요.
2. 코드 2번째 줄에서 슬라이싱을 startswith() 함수로 하도록 수정하세요.
3. 코드 4번째 줄에서 len() 함수를 제거하세요.
4. 코드 12번째 줄 not 연산자의 위치를 is 연산자 뒤로 수정하세요.
5. 코드 13번째 줄에서 비교 연산자를 제거하세요.
"""


def check_name(name):
    if name.startswith("e"):
        return True
    elif name:
        return False

    return None


test_name = "elice"
result = check_name(test_name)

if result is not None:
    if result is True:
        print("e로 시작하는 이름입니다.")
    else:
        print("e로 시작하는 이름이 아닙니다.")
else:
    print("빈 문자열입니다.")
