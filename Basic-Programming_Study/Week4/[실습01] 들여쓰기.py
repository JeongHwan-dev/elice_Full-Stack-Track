"""
[지시사항]
1. 파이썬에서 들여쓰기 방법은 공백(스페이스) 2칸, 탭(tab) 등 여러가지 방법이 있습니다.
다만, 파이썬 코딩 스타일 가이드(PEP 8)에서는 공백 4칸을 가이드로 제시하고 있기 때문에 공백 4칸을 기준으로 작성해봅시다.
"""


def yoonHa(num):
    ansStr = ""
    yoonDict = {"4": "love", "8": "smile", "6": "kiss"}

    for i in str(num):
        ansStr = ansStr + yoonDict[i]

    return ansStr


nums = 486
print(yoonHa(nums))
