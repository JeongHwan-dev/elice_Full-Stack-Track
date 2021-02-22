"""
[지시사항]
1. 조건식에서 문자열 슬라이싱이 된 것을 startswith() 함수로 수정하세요.
"""

room = "bedroom"

if room.startswith("bath"):
    print("욕실입니다.")
elif room.startswith("bed"):
    print("침실입니다.")
elif room.startswith("living"):
    print("거실입니다.")
