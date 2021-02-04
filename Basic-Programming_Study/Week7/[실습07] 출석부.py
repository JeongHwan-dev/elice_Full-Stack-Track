"""
[지시사항]
1. 지시사항을 만족하는 checkRecord 함수를 완성하세요.
2. 출석부에 ‘A’가 2번이상 나올 경우 False 를 return 합니다.
3. 출석부에 ‘L’이 세 번 이상 연속 나올 경우 False 를 return 합니다.
4. 교칙에 위배되지 않는 선에서 결석과 지각을 한 학생에게는 True 를 return 합니다.
"""


# 출석부를 확인하는 함수를 완성하세요.
def check_record(s):
    if (s.count('A') >= 2) or (s.count('LLL') >= 1):
        return False
    else:
        return True


# 아래는 학생들의 출석부입니다. 결과가 잘 나오는지 직접 테스트 해보세요!
students = ['AAPPPPPPPP', 'PPPLLLPPPP', 'APPPPPLLPP', 'PPPLLLAAPP']

for s in students:
    print(check_record(s))
