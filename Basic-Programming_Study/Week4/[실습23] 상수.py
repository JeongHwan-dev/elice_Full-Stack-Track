"""
[지시사항]
1. 0을 이름이 ATTACK_STATUS인 변수로 치환하세요.
2. 1을 이름이 DEFENCE_STATUS인 변수로 치환하세요.
"""

ATTACK_STATUS = 0
DEFENCE_STATUS = 1

status = ATTACK_STATUS

if status == ATTACK_STATUS:
    print("공격!")
elif status == DEFENCE_STATUS:
    print("수비!")
else:
    print("대기")