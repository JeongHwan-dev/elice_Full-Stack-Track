"""
[지시사항]
1. 조건에 따른 출력 결과를 택시, 버스, 지하철, 도보 중에서 정확히 출력하세요.
"""

money = int(input())

if money >= 1000:
    msg = '택시'
elif money >= 500:
    msg = '버스'
elif money >= 300:
    msg = '지하철'
else:
    msg = '도보'

print(msg)
